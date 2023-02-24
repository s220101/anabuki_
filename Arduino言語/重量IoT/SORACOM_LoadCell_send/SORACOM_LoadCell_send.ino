#include "parameters.h"
#include "function.h"

void setup() {
  
  CONSOLE.begin(115200);
  LTE_M_shieldUART.begin(BAUDRATE);

  initialize_LTE_module();

  initialize_sensors();
  
  pinMode(buzzerPin, OUTPUT);

  analogWrite(buzzerPin, 128);
  Serial.print("Put something on the weight sensor!");
  delay(100);
  analogWrite(buzzerPin, 0);
  delay(5000);
  analogWrite(buzzerPin, 128);
  delay(100);
  analogWrite(buzzerPin, 0);
}
  
void loop() {

  weight_load_cell = get_Weight();
  delay(INTERVAL_ONE_SEC);
  weight_load_cell_second_time = get_Weight();

  Filtering_Weight(weight_load_cell, weight_load_cell_second_time);

  int used_weight = LIQUID_WEIGHT - weight_load_cell;

  int pressed_value = used_weight / ONE_PUSH;

  int remain_push_value = weight_load_cell / ONE_PUSH;

  temp = dht.readTemperature();

  dtostrf(temp, 5, 1, temp_buf);

  humi = (int) dht.readHumidity();

  float hPa = bmp280.getPressure() / 100.0;

  dtostrf(hPa, 6, 1, hPa_buf);

  sprintf_P(payload, PSTR("{\"temp\":%s,\"humi\":%d,\"air\":%s,\"gm\":%d,\"rp\":%d,\"used\":%d,\"up\":%d}"),
     temp_buf, humi, hPa_buf, weight_load_cell, used_weight, remain_push_value, pressed_value);

     Sending_Process();
}
