import preprocessor as p
import tweepy

import keys
import cleaning
import analizadorSentimientos
import charts


class TweetPreprocessor(tweepy.StreamListener):
    """Controla la transmision del tweet entrante"""

    tweets = []

    def __init__(self, api, tweets, topics, limit=10):
        """Configura el analizador de sentimientos"""
        self.tweets = tweets
        self.tweet_count = 0
        self.topics = topics
        self.TWEET_LIMIT = limit

        # se configura el procesador de tweets para descartar
        # URLs y palabras reservadas
        p.set_options(p.OPT.URL, p.OPT.RESERVED) 
        super().__init__(api)  # efectua el llamado al init de la superclase

    def on_status(self, status):
        """Llamado cuando Tweeter envia un nuevo tweet"""

        # Obtiene el texto del tweet
        try:  
            tweet_text = status.extended_tweet["full_text"]
        except: 
            tweet_text = status.text

        # Ignora retweets
        if tweet_text.startswith('RT'):
            return

        # ignora el tweet si no contiene el topico de interes
        count = 0
        for topic in self.topics:
            if topic.lower() in tweet_text.lower():
                count = count+1
        if count == 0:
            return
        
        # Obtiene el texto del tweet
        # print("Antes del preprocessor")
        # print(tweet_text)

        tweet_text = p.clean(tweet_text)  # limpia el tweet
        tweet_text = cleaning.clean_tweets(tweet_text) #elimina stopwords emoticones hashtags

        self.tweets.append(tweet_text)

            
        # Despliega el tweet
        #print("despues del preprocessor")
        #print(f'{sentiment} {status.user.screen_name}: {tweet_text}\n')
        
        self.tweet_count += 1  # track number of tweets processed

        # Si se llega a  TWEET_LIMIT, se retorna falso para terminar la transmision
        return self.tweet_count <= self.TWEET_LIMIT


def autenticarse():
    # Se crea y se configura OAuthHandler para autenticarse en Twitter
    auth = tweepy.OAuthHandler(keys.consumer_key,
                               keys.consumer_secret)
    
    auth.set_access_token(keys.access_token,
                          keys.access_token_secret)
    
    # Se configura el API
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                     wait_on_rate_limit_notify=True)
                 
    return api


def procesar_tweets(tweets,limite, criteriosBusqueda, api ):
    sentiment_listener = TweetPreprocessor(api,
        tweets, criteriosBusqueda, limite)

    # Se configura el stream
    stream = tweepy.Stream(auth=api.auth, listener=sentiment_listener, tweet_mode='extended')

    # si filtran los tweets en espanol que tienen el criterio de busqueda
    stream.filter(track=criteriosBusqueda, languages=['en'], is_async=False)  


def main():
    api= autenticarse()
                 
    # Se fija el criterio de busqueda
    criteriosBusqueda = ["coronavirus", "covid-19", "covid19", "covid", "quarantine", "lockdown"]
    #se fija la cantidad de tweets a extraer
    limite = int(50)  #cantidad e tweets para contar
    #lista donde se almacenaran los tweets
    tweets = []
    #se extraen y limpian los tweets
    procesar_tweets(tweets, limite, criteriosBusqueda, api)
    #diccionario de sentimientos donde se separaran los tweets por sentimiento
    diccionarioSentimientos = {'positive': 0, 'negative': 0, 'neutral': 0}

    #se analiza el sentimiento de cada tweet
    for tweet in tweets:
        analizadorSentimientos.analizar(diccionarioSentimientos,tweet)


    print(f'Analisis de sentimientos de los tweets "{criteriosBusqueda}"')
    print('Positivo:', diccionarioSentimientos['positive'])
    print('Negativo:', diccionarioSentimientos['negative'])
    print(' Neutro:', diccionarioSentimientos['neutral'])

    palabras = ""

    #se almacenan todos los tweeets en un solo string para hacer la nube de palabras
    for tw in tweets:
        tw=tw.lower()
        palabras= palabras+" "+tw

    charts.generarNube(palabras)

# Metodo main
if __name__ == '__main__':
    main()




