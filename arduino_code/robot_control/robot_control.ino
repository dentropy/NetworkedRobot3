// original source code from https://www.arduino.cc/en/Serial/Read
int incomingByte = 0;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT); 
}

void loop() {

  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    if(incomingByte == byte('O')){
      digitalWrite(13, HIGH);
    }
    if(incomingByte == byte('P')){
      digitalWrite(13, LOW);
    }
    
    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
  }
}


