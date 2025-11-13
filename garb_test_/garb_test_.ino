
void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.print("F6 ");
  Serial.print("8E ");
  Serial.print("87 ");
  Serial.print("32 ");
  Serial.print("FA ");
  Serial.print("26 ");
  Serial.print("8E ");
  Serial.print("BE ");
  Serial.println(analogRead(A0));
  delay(100);
}
