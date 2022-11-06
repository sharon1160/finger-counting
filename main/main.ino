#include <LiquidCrystal.h>

const int RS_pin = 3;
const int E_pin = 2;
const int D4_pin = 4;
const int D5_pin = 5;
const int D6_pin = 6;
const int D7_pin = 7;
const int max_columnas = 16;
const int max_filas = 2;

LiquidCrystal lcd(RS_pin, E_pin, D4_pin, D5_pin, D6_pin, D7_pin);

String temp = "";
String number = "";

void setup() {
  lcd.begin(max_columnas, max_filas);
  Serial.begin(9600);
}

void printMsg(String msg) {
  lcd.clear();
  lcd.setCursor(2, 0);
  lcd.print(msg);
}

void loop() {
  if (Serial.available()) {
    temp = Serial.readString();
    if (number != temp) {
      number = temp;
    }
  }

  printMsg(number);
  delay(100);
}
