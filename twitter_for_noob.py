#####
# twitter_for_noob.py
# This script rips Twitter data in real time using the streaming API
# It is adapted from 
#     http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#####
# You will be editing fairly sophisticated code that uses concepts like 
#    classes and methods that we are not going to explore in depth in this 
#    class session. Don't worry! You don't need to know about this stuff 
#    in depth to make this example.


####
#    IMPORTANT: PAY ATTENTION!
#    We will search on these terms in the Twitter stream
OUR_SEARCH_TERMS=['python', 'javascript', 'ruby']


#Import the necessary methods from tweepy library
from tweepy import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import pprint

#Variables that contains the user credentials to access Twitter API 
access_token = "1191469117-xFOhqh8LvQKAsSVmQyo0wKPXQCubedOKdgcGZ7J"
access_token_secret = "sHEDgbYwmXOMSlNlEHGSBMtyNAIjkIreU6S5vxDozKe81"
consumer_key = "NHrfJjbi6KHpIx1D7zY5hPGcN"
consumer_secret = "hBIXH4POzJKRLV0VGVQ0FFSmI8g5XFXeKYMFlJl49juArpAMBY"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    """This is what's called a Listener class. The Twitter stream calls the on_data on 
    this class, so we implement on_data. In this case, on_data writes to standard
    output (the console), not to a persistent file."""
    
    def on_data(self, data):
    	if data is None: 
    		print "We have no data"
    	else:
            print data
        return True

    def on_error(self, status):
        print status

class FileOutListener(StreamListener):
    """This another Listener class. Instead of sending the stream to the console, 
    this will write it to a file."""

    def __init__(self): 
        """Write a header to the file"""
        
        self.output_file = open("twitter_output.txt", "r+")
        self.output_file.write("TWITTER STREAM\n")
        self.output_file.write("===\n")
        
        #It's important to close the file because close() flushes out the contents, i.e.
        # makes them write to the file.
        self.output_file.close()

    def on_data(self, data):
        """This method is what happens when the listener receives data from Twitter"""
        
        self.output_file = open("twitter_output.txt", "a")
        if data is None: 
            print "We have no data"
        else:
            print "Now we will write data to the file."
            self.output_file.write("data")
            
        self.output_file.close()
        return True

    def on_error(self, status):
        """This method is what happens when an error occurs after streaming data from Twitter"""
        print status

def do_twitter_streaming():
    """This is our main execution function"""
    
    #####
    #    PAY ATTENTION TO THIS!!!!
    #This next line is key to our lesson. We will change this class instatiation from a StdOutListener to 
    # a FileOutListener.
    our_listener = StdOutListener()
    
    #Now, using our new listener object, we will pass it to the Twitter API and receive a stream as a result.
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, our_listener)

    #This line filters Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=OUR_SEARCH_TERMS)


#By wrapping things with this if statement, we only execute this functionality if this file is called as 
#    the top-level call in Python. 
#    Don't worry too much about what that means.

if __name__ == '__main__':
    do_twitter_streaming()
