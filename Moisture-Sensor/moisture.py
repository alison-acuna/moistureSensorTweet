#!/usr/bin/python

# Start by importing the libraries we want to use

import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import tweepy

import time # This is the time library, we need this so we can use the sleep function

# Define some variables to be used later on in our script


message_dead = "Muffet says: I am thirsty!  Water please @Alison_Acuna"

# This is the message that will be sent when moisture IS detected again

message_alive = "Muffet says: Thanks! All hydrated and happy @Alison_Acuna"

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def muffet_status(message):
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "Fill in to function",
    "consumer_secret"     : "Fill in to function",
    "access_token"        : "Fill in to function",
    "access_token_secret" : "Fill in to function"
    }

  api = get_api(cfg)
  tweet = message
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing




# This is our callback function, this function will be called every time there is a change on the specified GPIO channel, in this example we are using 17

def callback(channel):
	if GPIO.input(channel):
		print "LED off"
		sendEmail(message_dead)
	else:
		print "LED on"
		sendEmail(message_alive)

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
channel = 17
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(channel, callback)

# This is an infinte loop to keep our script running
while True:
	# This line simply tells our script to wait 0.1 of a second, this is so the script doesnt hog all of the CPU
	time.sleep(0.1)
