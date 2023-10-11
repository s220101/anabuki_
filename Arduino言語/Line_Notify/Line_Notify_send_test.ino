#include <WiFi.h>
//バージョン2.1.0
#include <ESP_Line_Notify.h>

// WiFi 設定
const char *WIFI_SSID = "";        //  *** 書き換え必要 ***
const char *WIFI_PASSWORD = "";  //  *** 書き換え必要（8文字以上）***
LineNotifyClient line;
WiFiServer server(80);
//LINEへの通知フラフ[0:通知する,1:通知しない]
int send_flag = 0;
//LINEへの通知期間[10:10秒間隔,155:55秒間隔]
int send_interval = 10;
 
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
  Serial.println("setup OK!");
}
 
 
void loop()
{
  if (send_flag == 0)
  {
    line.message = "test A";
    LineNotifySendingResult result = LineNotify.send(line);
    
    Serial.print("通知フラグ:");
    Serial.println(send_flag);

    send_flag = 1;
  }
  else if (send_flag != 0)
  {
    Serial.print("通知フラグ:");
    Serial.println(send_flag);
  }
  else
  {
   Serial.println("send errer"); 
  
  }
  delay(1000*send_interval);

}
