#include <SPI.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <HX711_ADC.h>

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define JST     3600* 9
#define SEALEVELPRESSURE_HPA (1013.25)

const int HX711_dout = 14;
const int HX711_sck = 12;
HX711_ADC LoadCell(HX711_dout, HX711_sck);

Adafruit_BME280 bme;
  /* WiFiのssidとパスワードを記入 */
const char* ssid = "";
const char* pass = "";
WiFiServer server(80);
//環境データの計測
const String host = "";

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
  LoadCell.begin();
  LoadCell.setCalFactor();
  LoadCell.start(2000);

}

void loop() {
  HTTPClient http;
  float temp = bme.readTemperature();
  float humi = bme.readHumidity();
  float hPa  = bme.readPressure()/100.0F;
  LoadCell.update();
  float gram = LoadCell.getData();
  Serial.print(temp);
  Serial.print(humi);
  Serial.print(hPa);
  Serial.print(gram);

  //http.begin(host + "?temp=" + String(temp) + "&humi=" + String(humi) + "&hPa=" + String(hPa));//URLにデータを乗せてアクセス先へ送信
  http.begin(host + "?temp=" + String(temp) + "&humi=" + String(humi) + "&hPa=" + String(hPa) + "&gram=" + String(gram));//URLにデータを乗せてアクセス先へ送信
  
  int status_code = http.GET();
  Serial.printf("get request: status code = %d\r\n", status_code);
  http.end();
  delay(1000);

}
