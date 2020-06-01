#   Author: Gianna Miggins
#   Using Prof. Dugas code to set up the API
#  This program accesses data from a twitter user site (hard-coded as Stevens)

#  To run in a terminal window:  twitter_data.py
#  you will be prompted for a twitter user name until you enter STOP to end the program


import tweepy
import datetime

### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = ""
CONSUMER_KEY_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# Authentication

authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#  use wait_on_rate_limit to avoid going over Twitter's rate limits
api = tweepy.API(authenticate, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)
app = True
while app == True:          
    # Get Information About a Twitter User Account
    user = input("Enter a username you would like to access: ")
    if user == 'STOP':
        app = False
        print("Thank you for using the Twitter API, goodbye")
        break
    try: twitter_user = api.get_user(user)
    except: 
        print('user not valid')
        continue

    # Get Basic Account Information
    print("id: ", twitter_user.id)
    print("name: ", twitter_user.name)
    print("screen name: ", twitter_user.screen_name)
    print("description: ", twitter_user.description)
    #print("followers: ", twitter_user.followers) #printed all info 
    print("number of followers: ", twitter_user.followers_count)
    print("number of friends: ", twitter_user.friends_count)
    print("members since: ", twitter_user.created_at.date())
    print("verified account: ", twitter_user.verified)
    print("number of tweets: ", twitter_user.statuses_count)

    print()
    print('most recent tweet: ', twitter_user.status._json['text'])

    print('number of favorites: ', twitter_user.status._json['favorite_count'])

    # Determine an Account’s Friends 
    friends = []

    print("\nFirst 5 friends:")

    # Creating a Cursor
    cursor = tweepy.Cursor(api.friends, screen_name=user)

    # Get and print 5 friends
    for account in cursor.items(5):
        print(account.screen_name)

    
#print('test: ',  api.trends_closest(30.8, 40.6))

data = api.trends_place(1)[0]
trend = data['trends']
names = [t['name'] for t in trend]
trendsName = ' '.join(names)
#print(trendsName) #global trending words (not great)

search_term = "#dreams -filter:retweets"
tweets = tweepy.Cursor(api.search, q=search_term, lang="en", since='2020-04-10').items(100)

all_t = []
for tweet in tweets:
    all_t.append(tweet.text)
    print(tweet.text)
    #print(tweet.author)
    author = tweet.user._json['name']
    print(author)
