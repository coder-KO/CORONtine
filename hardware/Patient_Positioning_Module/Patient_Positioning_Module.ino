/*
Final hardware code for Patient Postioning Module
HackCovid19
Team    :-  Dev.ino
Code by :-  Krishna Ojha
            Ekta Arora
*/
#include <Servo.h>
Servo My_servo;

// Defining Ultrasnoic Sensor Pins
int trig=11;
int echo=12;

// Arrays for angles and distance measurement
float min_val=0;
float ultra_distance[180]={0};
int angle[180]={0};

// Variables for setting mean values
int mean_distance = 20;
int detection_distance = 30;

// Variable for calculating live distance of person from sensor
int person_distance = 0;

void setup() {
  My_servo.attach(3,600,2300);
  My_servo.write(600);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  digitalWrite(trig,LOW);
  digitalWrite(echo,LOW);
  
  Serial.begin(9600);
}

void loop() {
  // Initializing servo with refrence point (Horizontal Zero)
  My_servo.write(0);
  delay(1000);
  
  int i=0, j=0;
  int dist_flag = 0;  // To acknowledge, person is positioned correctly
  int index = -2;
  
  int person_flag = 0;
  int conf = 0;

  // Starting scan (0-180 degrees)
  for(i=0; i<=180; i++){
    My_servo.write(i);
    angle[j] = i;
    
    //    Serial.print(F("Servo is at angle :")); // debugging
    //    Serial.print(angle[j]);                 // debugging

    ultra_distance[j]=measure_distance_cm();  // Measuring distance corresponding to each angle
    
    // Serial.print(F("Object is at distance :")); // debugging
    // Serial.println(ultra_distance[j]);          // debugging
    
    if(ultra_distance[j] <= detection_distance){
      //Serial.println(F("Person detected!"));
      person_distance = ultra_distance[j];  // Updating live position of person
      person_flag = position_person();      
      break;
    }
    delay(100);
  }

  if(person_flag == 1){
    conf = 1;  
  }
  Serial.println(conf); // Send confirmation to run ML script to serial port
}



int position_person(){
  int dist_flag = 0;
  //  Serial.println(F("position_person called"));  // debugging
  
  person_distance = measure_distance_cm();
  int diff = abs(person_distance - mean_distance); // Calculate person's distance from desired position
  
  //  Serial.print(F("Starting difference = "));    // debugging
  //  Serial.println(diff);                         // debugging      

  // To check wether person is in desired range                     
  if(diff >= 3){
  while(diff >= 3){
      person_distance = measure_distance_cm();
      diff = abs(person_distance - mean_distance);  // recalculate difference for while loop
     
      if(person_distance > mean_distance){
        // Person is behind the mark
        Serial.println(F("1111"));
        delay(1000);
        Serial.println(person_distance - mean_distance);
        delay(5000);
      }
      else if (person_distance < mean_distance){
        // Person is ahead of the mark  
        Serial.println(F("2222"));
        delay(1000);
        Serial.println(abs(person_distance - mean_distance));
        delay(5000);        
      }    
    }    
  }
  else{
    dist_flag = 1;
    Serial.println(F("0000"));
    delay(1000);
    //Serial.println(F("Person is at right distance.!")); // debugging
  }
}

// Function for measuring distance through ultrasonic sensor.
float measure_distance_cm(){
  float distance =0;
  long time_value=0;
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  time_value=pulseIn(echo,HIGH);
  distance=.033*time_value/2;
  return distance;
}
