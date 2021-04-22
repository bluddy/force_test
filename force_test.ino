#include <Servo.h>

int sensor_pin = A0;
int value = 0;
unsigned long time = 0;
int do_send = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    do_send = Serial.read();
    digitalWrite(LED_BUILTIN, LOW);
  }
  if (do_send != 0) {
    digitalWrite(LED_BUILTIN, HIGH);
    value = analogRead(sensor_pin);
    time = millis();
    Serial.write((byte *)&time, sizeof(time));
    Serial.write((byte *)&value, sizeof(value));
  }
}
