import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "Fill in to function",
    "consumer_secret"     : "Fill in to function",
    "access_token"        : "Fill in to function",
    "access_token_secret" : "Fill in to function"
    }

  api = get_api(cfg)
  tweet = "My first Twitter App is tweeting Successfully"
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
