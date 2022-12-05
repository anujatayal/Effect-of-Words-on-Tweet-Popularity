import tweepy as tw
import csv  

#Add in the necessary access token of the tweet app
accesstoken = ''
accesstokensecret = "" 
apikey = '' 
apisecretkey = ''

auth = tw.OAuthHandler(apikey,apisecretkey) 
auth.set_access_token(accesstoken,accesstokensecret) 
api = tw.API(auth)

client = tw.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAFIoigEAAAAA5Rj%2FSBOTux14V75eX2O8Evml2kw%3DxRZa5lhafpUdUmawOlTwcvWsaZHJ42Y7wsEnXXK8K0enHbEvn3')

# Replace with your own search query. Using english 'en' as the language for the required tweets
query = 'Donald Trump lang:en'

#querying tweets and requesting the necessary attribute fields in the results
tweets = client.search_recent_tweets(query=query, tweet_fields=['public_metrics','created_at','author_id'], max_results=100)

field_names = ['ID', 'CREATED', 'AUTHOR',
               'TEXT', 'RETWEET','LIKES']
 
#Writing the tweets into a CSV file
with open('tweets.csv', 'a', encoding='UTF8') as f:
    writer = csv.writer(f)
    
    dictwriter_object = csv.DictWriter(f, fieldnames=field_names)
 
    for tweet in tweets.data:

        #Creating the dictionary of tweets
        dict = {'ID': tweet.id, 'CREATED': tweet.created_at, 'AUTHOR': tweet.author_id,
        'TEXT': tweet.text, 'RETWEET':tweet.public_metrics['retweet_count'], 'LIKES':tweet.public_metrics['like_count']}

        #Writing dictionary into the CSV file
        dictwriter_object.writerow(dict)
 
    # Close the file object
    f.close()
    
