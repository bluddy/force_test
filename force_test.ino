#include <Servo.h>

int sensor_pin = A0;
int value = 0;
unsigned long time = 0;
int do_send = 1;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() >= sizeof(do_send)) {
    Serial.readBytes((byte *)&do_send, sizeof(do_send));
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
  }
  if (do_send != 0) {
    digitalWrite(LED_BUILTIN, HIGH);
    value = analogRead(sensor_pin);
    time = millis();
    Serial.write((byte *)&time, sizeof(time));
    Serial.write((byte *)&value, sizeof(value));
  }
}
