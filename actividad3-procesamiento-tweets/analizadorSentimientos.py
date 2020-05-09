from textblob import TextBlob


#  actualiza el analizador de sentimientos con la polaridad
def analizar(tweet_text,df):

        blob = TextBlob(tweet_text)
        if blob.sentiment.polarity > 0:
            df=df.append({'tweet' : tweet_text , 'clase' : 'Positivo' } , ignore_index=True)
        elif blob.sentiment.polarity == 0:
            df=df.append({'tweet' : tweet_text , 'clase' : 'Neutro' } , ignore_index=True)
        else:
            df=df.append({'tweet' : tweet_text , 'clase' : 'Negativo'} , ignore_index=True)
        return df
