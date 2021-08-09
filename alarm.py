""" PY TO ESP (LED CONTROLLER) """
# Written by Junicchi - https://github.com/Kebablord

import urllib.request
root_url = "http://10.50.132.58"  # ESP's url, ex: http://192.168.102 (Esp prints it to serial console when connected to wifi)

def sendRequest(url):
        try:
                n = urllib.request.urlopen(url) # send request to ESP
        except:
                pass

def triggerAlarm():
        sendRequest(root_url + "/ALARM")
        
def triggerReset():
        sendRequest(root_url + "/RESET")
