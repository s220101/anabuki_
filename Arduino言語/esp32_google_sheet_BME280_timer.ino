#include <SPI.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define JST     3600* 9
#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme;
  /* WiFiのssidとパスワードを記入 */
const char* ssid = "";
const char* pass = "";
int i = 0;
WiFiServer server(80);
//環境データの計測
const String host = "";
//const String host = "";
void setup() {
  Serial.begin(115200);

  
  Serial.print("Connecting to ");
  Serial.print(ssid);
  WiFi.begin(ssid, pass);
  
  /* Wi-Fi接続確認 */
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("connected");

  server.begin();
  Serial.print("server: ");
  Serial.println(WiFi.localIP());

  if (!bme.begin(0x76)) 
  {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
    //日本時間
  configTime( JST, 0, "ntp.nict.jp", "ntp.jst.mfeed.ad.jp");

}

void loop() {

      time_t t;
  struct tm *tm;
  t = time(NULL);
  tm = localtime(&t);

  //時間を取得
  int time_hour = tm->tm_hour;
  int time_min = tm->tm_min;
  int time_sec = tm->tm_sec;

  if(time_min == 15 * i && time_sec == 0)
  {
    HTTPClient http;
    float temp = bme.readTemperature();
    float humi = bme.readHumidity();
    float hPa  = bme.readPressure()/100.0F;

    Serial.print(temp);
    Serial.print(humi);
    Serial.print(hPa);
  
    http.begin(host + "?temp=" + String(temp) + "&humi=" + String(humi) + "&hPa=" + String(hPa));//URLにデータを乗せてアクセス先へ送信
    
    int status_code = http.GET();
    Serial.printf("get request: status code = %d\r\n", status_code);
    http.end();
    i++;
  }
  else if(i > 3)
  {
    i = 0;
  }
  else
  {
    Serial.println("ereer");
  }


}
