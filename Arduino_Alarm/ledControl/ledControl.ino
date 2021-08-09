/* LED CONTROLLING WITH PYTHON
   Written by Junicchi
   https://github.com/Kebablord

   It's a ESP management through Python example
   It simply fetches the path from the request
   Path is: https://example.com/this -> "/this"
   You can command your esp through python with request paths
   You can read the path with getPath() function
*/


#include "ESP_MICRO.h"

#define LED D0

void setup() {
  Serial.begin(9600);
  start("WCGuest 2", "froglegs"); // Wifi details connec to

  pinMode(LED, OUTPUT);
}

void loop() {
  waitUntilNewReq();  //Waits until a new request from python come

  if (getPath() == "/ALARM") {
    digitalWrite(LED, HIGH);
  }
  if (getPath() == "/RESET") {
    digitalWrite(LED, LOW);
  }
}
