# DomoWeatherAlert


Prerequisites:
Google Chromecast device(s)
Python 3.x installed
Python modules: sys, time, pychromecast, gTTS, feedparser and requests 

The weatheralert.py script pulls data from an rss feed provided by NOAA's website, https://alerts.weather.gov/, using python's feedparser module. The script checks to see if there is an active alert for an area. If so the script generates a mp3 file using the python gTTS module. The mp3 file, weather_alert_message.mp3, is saved in the www/media directory. Once the mp3 file is created the script then uses the pychromecast module to play the file to a chromecast device or group on the network.
As this script runs every minute if there is an actice alert it can become rather annoying. However the weather alert can be turned off via a dummy switch.

The on/off scripts that are used rename the weatheralert.py file that the lua script is executing thus breaking the lua script and turning off the alert. 
While its not the most elegant way - like checking to see if the file is there - it works.

To get this up and running:

1) Create a dummy X10 light switch - not sure how to do this check the FAQ, https://www.domoticz.com/wiki/FAQ  
2) Place the lua script in the /scripts/lua directory
3) Place the weatheralert.py, turn_on_weather_alert.py and turn_off_weather_alert.py files in the /scripts/python directory
4) Add the script paths to the on and off actions to the weather alert switch created in step one -  reference fig1.jpeg
5) Edit line 10 of the weatheralert.py script to point to the IP and port of the device Domoticz is installed
6) Edit the URL in line 14 of the weatheralert.py script. The URL for your area can be found at NOAA website's - https://alerts.weather.gov/

With some small edits this script could work with other IoT devices or software like Sonos or Logitech Media Server. 

Running on Windows 10 | Domoticz Version: 3.8153 | Nest/z-wave/milights/Kodi/LMS/Google Home