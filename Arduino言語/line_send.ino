#if defined(ESP32)
#include <WiFi.h>
#endif
#include <ESP_Line_Notify.h>
#include <DHT.h>
 
#define DHT_PIN 14
#define DHT_MODEL DHT11
DHT dht(DHT_PIN, DHT_MODEL);

//int trig = 27;
//int echo = 26;
 
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
 
  dht.begin();

  //pinMode(trig,OUTPUT);
  //pinMode(echo,INPUT);
 
// LINEトークンの入力
  //line.token = "";
  Serial.println("setup OK");
}
 
 
void loop()
{
// 温湿度データの取得
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  Serial.println("loop now");

   // 超音波の出力終了
  //digitalWrite(trig,LOW);
  //delayMicroseconds(1);
  // 超音波を出力
 // digitalWrite(trig,HIGH);
  //delayMicroseconds(11);
  // 超音波を出力終了
 // digitalWrite(trig,LOW);
  // 出力した超音波が返って来る時間を計測
  //int T = pulseIn(echo,HIGH);
  // 計測した時間と音速から反射物までの距離を計算
  //float distance = T*0.017;
 
// LINEへ通知する
  if(t>28){
      line.message = " 温度が上がり過ぎています"" 温度: " 
      +  String(t,1) + "  湿度: "+ String(h,1);
  }
  else if(t<24){
      line.message = " 温度が下がり過ぎています"" 温度: " 
      + String(t,1) + "  湿度: "+ String(h,1);
    }
    else if(h>70){
      line.message = " 湿度が上がり過ぎています"" 温度: " 
      + String(t,1) + "  湿度: "+ String(h,1);
    }
    else if(h<30){
      line.message = " 湿度が下がり過ぎています"" 温度: " 
      + String(t,1) + "  湿度: "+ String(h,1);
    }
    else if(isnan(h) || isnan(t)){
      line.message = "エラー:温湿度のデータを取得出来ません";
    }
   //if(T>50){
    //line.message = "亀がライト付近にいます"+ String(T,2);
  // }
  LineNotifySendingResult result = LineNotify.send(line);
  delay(5000);
  Serial.println("loop end");

}
