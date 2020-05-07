import re  # regular expression
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer


def clean_tweets(tweet):

        # HappyEmoticons
        emoticons_happy = {':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}', ':^)', ':-D',
                           ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D', '=-3', '=3', ':-))', ":'-)", ":')",
                           ':*', ':^*', '>:P', ':-P', ':P', 'X-P', 'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b',
                           '>:)', '>;)', '>:-)', '<3'}

        # Sad Emoticons
        emoticons_sad = {':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<', ':-[', ':-<', '=\\',
                         '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c', ':c', ':{', '>:\\', ';('}

        # combine sad and happy emoticons
        emoticons = emoticons_happy.union(emoticons_sad)

        # Emoji patterns
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   "]+", flags=re.UNICODE)

        # configuring stopwords and stemmer
        stop_words = set(stopwords.words('english'))
        ps = PorterStemmer()
        word_tokens = word_tokenize(tweet)
    # after tweepy preprocessing the colon symbol left remain after      #removing mentions
        tweet = re.sub(r':', '', tweet)
        tweet = re.sub(r'‚Ä¶', '', tweet)
    # replace consecutive non-ASCII characters with a space
        tweet = re.sub(r'[^\x00-\x7F]+', ' ', tweet)
    # remove emojis from tweet
        tweet = emoji_pattern.sub(r'', tweet)
    # filter using NLTK library append it to a string
        filtered_tweet = [w for w in word_tokens if not w in stop_words]
        filtered_tweet = []
    # looping through conditions
        for w in word_tokens:
            # check tokens against stop words , emoticons and punctuations
            if w not in stop_words and w not in emoticons and w not in string.punctuation:
                stemmed_w = ps.stem(w)
                filtered_tweet.append(stemmed_w)
        return ' '.join(filtered_tweet)
        # print(word_tokens)
        # print(filtered_sentence)return tweet
