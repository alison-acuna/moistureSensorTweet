import tweepy

# This is the message that will be sent when moisture IS NOT detected

message_dead = "Muffet says: I am thirsty!  Water please @Alison_Acuna"

# This is the message that will be sent when moisture IS detected again

message_alive = "Muffet says: Thanks! All hydrated and happy @Alison_Acuna"

plant_status = 1

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def set_tweet(plant_status):
	if plant_status == 1:
		tweet = message_dead
	else:
		tweet = message_alive
	return tweet


def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "Fill in to function",
    "consumer_secret"     : "Fill in to function",
    "access_token"        : "Fill in to function",
    "access_token_secret" : "Fill in to function"
    }

  api = get_api(cfg)
  tweet = set_tweet(1)
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
