#include <Servo.h>
Servo My_servo;

int trig=11;
int vcc=10;
int echo=12;


float min_val=0;
float ultra_distance[180]={0};
int angle[181]={0};

int min_distance = 40;
int dection_distance = 25;

void setup() {
  My_servo.attach(3,600,2300);
  My_servo.write(600);
 pinMode(trig,OUTPUT);
 pinMode(vcc,OUTPUT);
 pinMode(echo,INPUT);
 digitalWrite(trig,LOW);
 digitalWrite(vcc,HIGH);
 digitalWrite(echo,LOW);
 Serial.begin(9600);
 delay(13000);
}

void loop(){
  My_servo.write(0);
  delay(600);
  int j=0;
  int index=-2;// check index value
  
    for (int i=0; i<=200;i+=1){
      My_servo.write(i);
      angle[j]=i;
      ultra_distance[j]=measure_distance_cm();
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
    delay(1000);  
    while(true){
      int new_val=0;  
      new_val= measure_distance_cm();
      
      if(abs(new_val-25) >= 4){
        while(abs(new_val-25) >= 4){
          Serial.println("Move");
        }
      }
      else{
        Serial.println("scan");
      }
      
//      Serial.println(new_val);
//      delay(1000);
//      if (abs(ultra_distance[index]-new_val)>=2.0){
//        Serial.println(new_val);
//        Serial.flush();
//      }
    }   
}



float measure_distance_cm()
{
  float distance =0;
  long time_value=0;
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  time_value=pulseIn(echo,HIGH);
  distance=.033*time_value/2;
  return distance;
    }
