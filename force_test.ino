#include <Servo.h>

int sensor_pin = A0;
int value = 0;
unsigned long time = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  value = analogRead(sensor_pin);
  time = millis()
  Serial.write(time);
  Serial.write(value);
}
