
// For testing the Ultrasonic Sensor

#define trigPin 11
#define echoPin 12
#define LEDPin 13 

int maximumRange = 200; 
int minimumRange = 0; 
long duration, distance; 

void setup() {
 Serial.begin (9600);
 pinMode(trigPin, OUTPUT);
 pinMode(echoPin, INPUT);
 pinMode(LEDPin, OUTPUT); 
}

void loop() {
 digitalWrite(trigPin, LOW); 
 delayMicroseconds(2); 

 digitalWrite(trigPin, HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPin, LOW);
 duration = pulseIn(echoPin, HIGH);
 
 //Calculate the distance (in cm) based on the speed of sound.
 distance = duration/58.2;
 
 if (distance >= maximumRange || distance <= minimumRange){
 Serial.println("Out of Range!");
 digitalWrite(LEDPin, HIGH); 
 }
 else {
 Serial.println(distance);
 digitalWrite(LEDPin, LOW); 
 }
 
 delay(50);
}
