#include <WiFi.h>

#include <ESP_Line_Notify.h>

// WiFi 設定
const char *WIFI_SSID = "";        //  *** 書き換え必要 ***
const char *WIFI_PASSWORD = "";  //  *** 書き換え必要（8文字以上）***
LineNotifyClient line;
WiFiServer server(80);
 
void setup()
{
  Serial.println("setup start");
  Serial.begin(115200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED)
  { 
    delay(200);
    Serial.println(".");
  }
  Serial.println(WiFi.localIP());
  server.begin();
  Serial.println("OK!");

// LINEトークンの入力
  line.token = "";
  Serial.println("setup OK");
}
 
 
void loop()
{
  line.message = "Connected to Line";
  LineNotifySendingResult result = LineNotify.send(line);
  delay(5000);
  Serial.println("loop end");

}
