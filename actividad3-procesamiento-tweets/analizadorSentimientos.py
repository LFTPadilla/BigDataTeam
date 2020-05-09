from textblob import TextBlob


#  actualiza el analizador de sentimientos con la polaridad
def analizar(sentiment_dict, tweet_text,df):

        blob = TextBlob(tweet_text)
        if blob.sentiment.polarity > 0:
            #sentiment = '+'
            sentiment_dict['positive'] += 1
            df=df.append({'tweet' : tweet_text , 'clase' : 1 } , ignore_index=True)
        elif blob.sentiment.polarity == 0:
            #sentiment = ' '
            sentiment_dict['neutral'] += 1
            df=df.append({'tweet' : tweet_text , 'clase' : 0 } , ignore_index=True)
        else:
            #sentiment = '-'
            sentiment_dict['negative'] += 1
            df=df.append({'tweet' : tweet_text , 'clase' : -1} , ignore_index=True)
        # print(f'{sentiment}: {tweet_text}\n')
        return df
