#include <Servo.h>
Servo My_servo;

int trig=11;
int vcc=10;
int echo=12;

float min_val=0;
float ultra_distance[180]={0};
int angle[181]={0};

void setup(){
  My_servo.attach(3,600,2300);
  My_servo.write(600);
  pinMode(trig,OUTPUT);
  pinMode(vcc,OUTPUT);
  pinMode(echo,INPUT);
  digitalWrite(trig,LOW);
  digitalWrite(vcc,HIGH);
  digitalWrite(echo,LOW);
  Serial.begin(9600);
  delay(1000);
}

void loop(){
  My_servo.write(0);
  delay(600);
  int j=0;
  int index=-2;// check index value
  
  for (int i=0; i<=200;i+=1){
    My_servo.write(i);
    angle[j]=i;
    ultra_distance[j]=distance();
    delay(20);
    j+=1;   
    if (i==180){break;} 
  }
  for (j=0;j<=180;j+=1){
    min_val=max(min_val,ultra_distance[j]);
  }
  for (j=0;j<=180;j+=1){
    if (min_val>ultra_distance[j]){
      min_val=ultra_distance[j];
      index=j;
    }
  }       
  My_servo.write(angle[index]);
//  Serial.println(int(distance()));
  while(true){
    if(distance() >= 1000){
      break;
    }
    Serial.println(int(distance()));
  }
  delay(1000);  
//  while(true){
//    if (abs(ultra_distance[index]-distance()) >= 80){
//      break;
//    }
//    Serial.println(int(distance()));
//  }             
}


float distance()
{
  int distance =0;
  long time_value=0;
  
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  
  time_value=pulseIn(echo,HIGH);
  distance=.033*time_value/2;
  
  return distance;
}
