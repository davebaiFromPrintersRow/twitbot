import tweepy as tp
import time
import os

consumer_key = '8NeXCov8m56kXAztNCpSBNoAN'
consumer_secret = 'eqJ0SOSra2qToz0KcF1VY0selS2RBPNf0yDEsKLGAkKOglMj2c'

access_token= '952578890081423360-fRPnFX4W8Q1XMJOwgFTNImnjKK6y4oP'
access_secret = 'gGSvLcaeu5sHV7kVgEVsoxofpvPBvlUvbgRiYLtW3Apxc'

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir ('pics')
for model_image in os.listdir('.'): 
	api.update_with_media(model_image)
	time.sleep(15)