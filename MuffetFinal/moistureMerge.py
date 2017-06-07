#!/usr/bin/python

# Start by importing the libraries we want to use

import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import smtplib # This is the SMTP library we need to send the email notification
import time # This is the time library, we need this so we can use the sleep function
import tweepy 

# Define some variables to be used later on in our script

# This is the message that will be sent when moisture IS NOT detected

message_dead = "Muffet says: I am thirsty!  Water please @Alison_Acuna"

# This is the message that will be sent when moisture IS detected again

message_alive = "Muffet says: Thanks! All hydrated and happy @Alison_Acuna"

cfg = {

            }



# This is our sendTweet function

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)


def callback(channel):  
	if GPIO.input(channel):
		print "LED off"
		tweet = message_dead
	else:
		print "LED on"
		tweet = message_alive
	return tweet	
                        
	
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
	api = get_api(cfg)
        tweet = callback(channel)
        status = api.update_status(status=tweet)

	time.sleep(0.1)
