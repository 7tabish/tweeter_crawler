import tweepy

# Authenticate to Twitter
CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""

class Twitter_crawler():
    def __init__(self,CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET):
        self.CONSUMER_KEY=CONSUMER_KEY
        self.CONSUMER_SECRET=CONSUMER_SECRET
        self.ACCESS_TOKEN=ACCESS_TOKEN
        self.ACCESS_TOKEN_SECRET=ACCESS_TOKEN_SECRET
        self.auth=None
        self.api=None
        self.query=[]
    def authentication(self):
        try:
            self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
            self.auth.set_access_token(self.ACCESS_TOKEN,self.ACCESS_TOKEN_SECRET)
            self.api = tweepy.API(self.auth)
            self.api.verify_credentials()
            return True
        except:
            return  False
    def get_tweets(self,query):
        self.query=query
        for tweet in tweepy.Cursor(self.api.search, q=self.query,lang="en").items():
            print(tweet.text)



query=['corona','disease']
ts=Twitter_crawler(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
if(ts.authentication()):
    ts.get_tweets(query)

