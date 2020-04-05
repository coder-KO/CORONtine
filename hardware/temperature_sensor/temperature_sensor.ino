#define obstaclePin A0  // This is our input pin

void setup() {
  pinMode(obstaclePin, INPUT);
  Serial.begin(9600);  
}
void loop() {
  Serial.print("Value :");
  Serial.println(analogRead(obstaclePin));
  delay(200);
}
