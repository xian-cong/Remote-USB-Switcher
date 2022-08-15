int SWITCH = 13;

void setup() {
  Serial.begin(9600);
  pinMode(SWITCH, OUTPUT);

}

void loop() {
  char data = Serial.read();
  switch(data) {
    case 's': 
      digitalWrite(SWITCH, LOW);
      delay(1000);
      break;
//    case 'test':
//      digitalWrite(SWITCH, HIGH);
//      break;
  }
  digitalWrite(SWITCH, HIGH);
}
