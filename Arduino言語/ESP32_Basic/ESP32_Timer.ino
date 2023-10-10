#include <WiFi.h>
#include <time.h>

#define JST     3600* 9

const char* ssid = "";
const char* password = "";

void setup() {
  Serial.begin(115200);
  delay(100);
 // Serial.print("\n\nStart\n");

  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(500);
  }
  Serial.println();
  Serial.printf("Connected, IP address: ");
  Serial.println(WiFi.localIP());

  configTime( JST, 0, "ntp.nict.jp", "ntp.jst.mfeed.ad.jp");
}

void Timer_function() {
  time_t t;
  struct tm *tm;

  t = time(NULL);
  tm = localtime(&t);
    delay(1000);
}


void loop()
{

  
}
