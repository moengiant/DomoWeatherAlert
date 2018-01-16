from __future__ import print_function
import sys
import time
import pychromecast
from gtts import gTTS
import feedparser
import requests

# Set path to Domoticz
URL_DOMOTICZ = 'http://192.168.1.5:8080/'

# Get weather alert information from NOAA

d = feedparser.parse('https://alerts.weather.gov/cap/wwaatmget.php?x=ILC043&y=0')
# Get the title and entry 
title = d.feed.title
#print (d.feed.title)
message = d.entries[0].title 
#print (d.entries[0].title)

#Checks to see if there are any active alerts 
if "There are no active watches, warnings or advisories" not in message:

	#Gets the title subject and summary of any active alerts from NOAA RSS feed
	
	alert = d.entries[0].summary
	alertmessage = title + '.' + message + '.' + alert
	print (alertmessage)

	#Save the alert message as an mp3
	
	tts = gTTS(text=alertmessage, lang='en', slow=False)
	#Saves the mp3 to the www/media directory within Domoticz 
	tts.save("C:/Program Files (x86)/Domoticz/www/media/weather_alert_message.mp3")

	#Cast message to a chromecast speaker or group
	
	# device_name is the name of the chromecast device or group that will play the message
	device_name = "Kitchen speaker"
	chromecasts = pychromecast.get_chromecasts()
	cast = next(cc for cc in chromecasts if cc.device.friendly_name == device_name)
	cast.wait()
	print(cast.device)
	print(cast.status)
	mc = cast.media_controller
	mc.play_media(URL_DOMOTICZ+'media/weather_alert_message.mp3', 'audio/mp3')
	mc.block_until_active()
	#print(mc.status)
	mc.play()

else:
	# Log in Domoticz that there are no activer weather alerts
	print("No Weather Alerts")  
	req = requests.get('http://192.168.1.5:8080/json.htm?type=command&param=addlogmessage&message=No Weather Alerts')
	exit()


