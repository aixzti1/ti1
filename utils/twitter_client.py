import tweepy

def tweet_signal(api_key, api_key_secret, access_token, access_token_secret, message):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    client = tweepy.API(auth)
    client.update_status(status=message)
