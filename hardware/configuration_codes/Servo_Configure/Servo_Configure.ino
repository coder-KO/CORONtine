#include <Servo.h>  
int servoPin = 3;  
int vcc = 7;
Servo Servo1; 
void setup() { 
   Servo1.attach(servoPin);
   pinMode(vcc, OUTPUT);
   digitalWrite(vcc, HIGH);
 
}
void loop(){ 
   // Make servo go to 0 degrees 
   Servo1.write(180); 
   delay(1000); 
//   // Make servo go to 90 degrees 
//   Servo1.write(90); 
//   delay(1000); 
//   // Make servo go to 180 degrees 
//   Servo1.write(180); 
//   delay(1000); 
}
