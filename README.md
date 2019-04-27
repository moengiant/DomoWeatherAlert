# DomoWeatherAlert

Script Prerequisites:
Google Chromecast device(s)
Python 3.x installed
Python modules: sys, time, pychromecast, gTTS, feedparser, requests, smtplib and email  

The weatheralert.py script pulls data from a NOAA  rss feed and is parsed using the feedparser module.  
NOAA's website:  https://alerts.weather.gov/
The script checks to see if there is an active alert for the area defind by the rss feed. 
If there is an active alert the script will send a text message in addition to announcing the weather alert message via a Googlecast device or cast group. 
The script generates an mp3 file using the python gTTS module.
The mp3 file, weather_alert_message.mp3, is saved in the www/media directory.
Once the mp3 file is created the script then uses the pychromecast module to play the file to a Chromecast device or group on the network.
As this script runs every minute - if there is an active alert the alert message can become rather annoying. However the weather alert can be turned on or off via a dummy switch.
The on/off scripts that are used rename the weatheralert.py file that the lua script is executing thus breaking the lua script and turning off the alert. 
While it is not the most elegant way - like checking to see if the file is there - it works.

To get this up and running:

1) Create a dummy X10 light switch - not sure how to do this check the FAQ, https://www.domoticz.com/wiki/FAQ  
2) Place the lua script in the /scripts/lua directory
3) Place the weatheralert.py, turn_on_weather_alert.py and turn_off_weather_alert.py files in the /scripts/python directory
4) Add the script paths to the on and off actions to the weather alert switch created in step one -  reference fig1.jpeg
5) Edit the from address on line 13 of the weatheralert.py script
6) Edit the to address on line 14 of the weatheralert.py script
7) Edit line 17 of the weatheralert.py script to point to the IP and port of the device Domoticz is installed
8) Edit the URL in line 21 of the weatheralert.py script. The URL for your area can be found at NOAA website's - https://alerts.weather.gov/
9) Edit line 46 of the weatheralert.py script for your smtp server and port settings
10) Edit line 49 of the weatheralert.py script for your username and password to connect to you smtp server
11) Edit line 58 to reflect the path to the www/media directory for your Domoticz location
12) Edit the device_name varible to a Chromecast device on the network

With some small edits this script could work with other IoT devices or software like Sonos or Logitech Media Server. 

Running on Windows 10 | Domoticz Version: 3.8153 | Nest/z-wave/milights/Kodi/LMS/Google Home
