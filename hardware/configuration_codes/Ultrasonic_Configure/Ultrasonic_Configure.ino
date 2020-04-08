
// For testing the Ultrasonic Sensor
// This code also sends data to python shell for testing

int trigPin = 11;    // Trigger
int echoPin = 12;    // Echo
long duration, cm, inches;
 
void setup() {
  Serial.begin (9600);
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
 
void loop() {

  
  Serial.println(distance());

  /*--------------------------------*/

//  if(abs(distance()-20) >= 6){
//    while(abs(distance()-20) >= 6){
//      if(distance() > 20)
//        Serial.println("1");
//      else
//        Serial.println("2");      
//      delay(5000);
//    }
//  }
//  else{
//    Serial.println("3");
//  }

  delay(5000);

  /*--------------------------------*/
}

int distance(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
 
  // Convert the time into a distance
  cm = (duration/2) / 29.1;     // Divide by 29.1 or multiply by 0.0343
  inches = (duration/2) / 74;   // Divide by 74 or multiply by 0.0135

  delay(100);
  return cm;
}
