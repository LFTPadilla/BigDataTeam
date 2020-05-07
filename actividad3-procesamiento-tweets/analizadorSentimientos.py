from textblob import TextBlob


#  actualiza el analizador de sentimientos con la polaridad
def analizar(sentiment_dict, tweet_text):
        blob = TextBlob(tweet_text)
        if blob.sentiment.polarity > 0:
            sentiment = '+'
            sentiment_dict['positive'] += 1
        elif blob.sentiment.polarity == 0:
            sentiment = ' '
            sentiment_dict['neutral'] += 1
        else:
            sentiment = '-'
            sentiment_dict['negative'] += 1
        # print(f'{sentiment}: {tweet_text}\n')
