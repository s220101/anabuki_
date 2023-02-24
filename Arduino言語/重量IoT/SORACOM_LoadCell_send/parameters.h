#define CONSOLE Serial

#define INTERVAL_ONE_SEC (1000)
#define INTERVAL_ONE_HOUR (3600000)
#define INTERVAL_ONE_MIN (60 * 1000)
#define RESET_DURATION 86400000UL

#define ENDPOINT ""
#define SKETCH_NAME ""
#define VERSION ""

#define ONE_PUSH (2.6)
#define BOTTLE_TOTAL_WEIGHT (1055)
#define BOTTLE_WEIGHT (77)
#define LIQUID_WEIGHT (BOTTLE_TOTAL_WEIGHT - BOTTLE_WEIGHT)
#define FILTERING_WEIGHT (100)
#define MAX_PUSH_NUMBER (LIQUID_WEIGHT / ONE_PUSH)

#define RX (10)
#define TX (11)
#define BAUDRATE (9600)
#define BG96_RESET (15)
char payload[130];
char hPa_buf[10];
char temp_buf[10];

#define TINY_GSM_MODEM_BG96
#include <TinyGsmClient.h>
#include <SoftwareSerial.h>
SoftwareSerial LTE_M_shieldUART(RX, TX);
TinyGsm modem(LTE_M_shieldUART);
TinyGsmClient ctx(modem);

#include <DHT.h>
#define dht11Pin (3)
DHT dht(dht11Pin, DHT11);
#include <Seeed_BMP280.h>
BMP280 bmp280;

#include <HX711_ADC.h>
const int HX711_dout = 9;
const int HX711_sck = 8;
HX711_ADC LoadCell(HX711_dout, HX711_sck);

#define buzzerPin 5

static int weight_load_cell = 0;//Load Cell range is 5000g
static int weight_load_cell_second_time = 0;
static int old_weight = 0;
static int humi = -1;
static float temp = -1.0;
