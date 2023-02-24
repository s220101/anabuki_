#include <WiFi.h>

const char *ssid = "";   //  *** 書き換え必要 ***
const char *pass = "";  //  *** 書き換え必要（8文字以上）***

WiFiServer server(80);

void setup() {

  Serial.begin(115200);

  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println(".");
  }

  Serial.println(WiFi.localIP());
  server.begin();
  Serial.println("OK!");
}

void loop() {

}
