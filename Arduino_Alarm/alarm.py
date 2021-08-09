""" PY TO ESP (LED CONTROLLER) """
# Written by Junicchi - https://github.com/Kebablord

import urllib.request
root_url = "http://192.168.1.238"  # ESP's url, ex: http://192.168.102 (Esp prints it to serial console when connected to wifi)

def sendRequest(url):
	n = urllib.request.urlopen(url) # send request to ESP

def triggerAlarm():
        sendRequest(root_url + "/ALARM")
        
def triggerRESET():
        sendRequest(root_url + "/RESET")
triggerAlarm()
