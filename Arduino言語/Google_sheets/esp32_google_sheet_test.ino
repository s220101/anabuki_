#include <SPI.h>
#include <WiFi.h>
#include <DHT.h>
#include <HTTPClient.h>

WiFiServer server(80);
const String host = "";

void setup() 
{

  /* WiFiのssidとパスワードを記入 */
  const char* ssid = "";
  const char* pass = "";
  
  Serial.print("Connecting to ");
  Serial.print(ssid);
  WiFi.begin(ssid, pass);
  
  /* Wi-Fi接続確認 */
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("connected");

  server.begin();
  Serial.print("server: ");
  Serial.println(WiFi.localIP());

  Serial.begin(115200);
}

void loop() {

  HTTPClient http;
  //記述形式:文字型のURLに文字型のデータ名の初めに？をつけて終りに＝をつける。そして、データの入った変数をプラスする
  http.begin(host + "?data_A=" + data_A);//URLにデータを乗せてアクセス先へ送信
  
  int status_code = http.GET();
  Serial.printf("get request: status code = %d\r\n", status_code);
  http.end();
  
  delay(2000);

}
