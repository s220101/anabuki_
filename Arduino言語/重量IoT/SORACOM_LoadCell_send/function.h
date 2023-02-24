void initialize_LTE_module(void)
{
  CONSOLE.print(F("Welcome to ")); 
  CONSOLE.print(SKETCH_NAME); 
  CONSOLE.print(F(" "));
  CONSOLE.println(VERSION);
  delay(100);

  CONSOLE.print(F("resetting module "));
  pinMode(BG96_RESET,OUTPUT);
  digitalWrite(BG96_RESET,LOW);
  delay(300);
  digitalWrite(BG96_RESET,HIGH);
  delay(300);
  digitalWrite(BG96_RESET,LOW);
  CONSOLE.println(F(" done."));

  modem.restart();
  delay(500);
  
  String modemInfo = modem.getModemInfo();
  
  int modem_info_len = modemInfo.length() + 1;
  char modem_info_buf[modem_info_len];
  modemInfo.toCharArray(modem_info_buf, modem_info_len);
  delay(200);
  while(!modem.waitForNetwork())
  {
    Serial.println(".");
  }
  delay(500);
  modem.gprsConnect("soracom.io", "sora", "sora");
  delay(500);
  while(!modem.isNetworkConnected());
  delay(500);
  IPAddress ipaddr = modem.localIP();
  CONSOLE.println(ipaddr);
  char ip_addr_buf[20];
  sprintf_P(ip_addr_buf, PSTR("%d.%d.%d.%d"), ipaddr[0], ipaddr[1], ipaddr[2], ipaddr[3]);
}

void software_reset(){
  asm volatile("  jmp 0");
}

void initialize_sensors(void)
{
  dht.begin();
  bmp280.init();
  LoadCell.begin();
  LoadCell.setCalFactor(471.24);
  LoadCell.start(2000);
}

int get_Weight(void)
{
  int num = 0;
  while(num < 35)
  {
   LoadCell.update();
   num++;
   delay(100);
  }
   int weight_load_cell = round(LoadCell.getData()) - BOTTLE_WEIGHT;

   return weight_load_cell;
}

void Filtering_Weight(int wight_load_cell, int weight_load_cell_second_time)
{
  while( abs(weight_load_cell_second_time - weight_load_cell) >= FILTERING_WEIGHT)
  {
    weight_load_cell = get_Weight();
    delay(INTERVAL_ONE_SEC);
    weight_load_cell_second_time = get_Weight();
    CONSOLE.println("Big Gap error");
  }
  
  if(weight_load_cell <= 0)
  {
    weight_load_cell = 0;
  }
  else if(weight_load_cell >= LIQUID_WEIGHT)
  {
    weight_load_cell = -1;
  }
  else 
  {
    weight_load_cell = weight_load_cell;
  }
}

void Sending_Process(void)
{
  CONSOLE.println(payload);
  CONSOLE.print(F("Send..."));
  if (!ctx.connect(ENDPOINT, 80)) {
    CONSOLE.println(F("failed."));
    delay(3000);
    return;
  }
  char hdr_buf[40];
  ctx.println(F("POST / HTTP/1.1"));
  sprintf_P(hdr_buf, PSTR("Host: %s"), ENDPOINT);
  ctx.println(hdr_buf);
  ctx.println(F("Content-Type: application/json"));
  sprintf_P(hdr_buf, PSTR("Content-Length: %d"), strlen(payload));
  ctx.println(hdr_buf);
  ctx.println();
  ctx.println(payload);
  ctx.stop();
  CONSOLE.println(F("done."));
  delay(INTERVAL_ONE_HOUR);

  #ifdef INTERVAL_ONE_HOUR*24*30
  //if(millis() > RESET_DURATION*30)
  if(millis() > INTERVAL_ONE_HOUR*24*30)
  {
    CONSOLE.println("Execute software reset...");
    delay(1000);
    software_reset();
  }
#endif

}
