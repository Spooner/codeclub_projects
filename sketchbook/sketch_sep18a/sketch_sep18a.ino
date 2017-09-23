#include <Servo.h> 

Servo middle, left, right, claw ;  // creates 4 "servo objects"

void setup() 
{ 
  Serial.begin(9600);
  middle.attach(11);  // attaches the servo on pin 11 to the middle object
  left.attach(10);  // attaches the servo on pin 10 to the left object
  right.attach(9);  // attaches the servo on pin 9 to the right object
  claw.attach(3);  // attaches the servo on pin 6 to the claw object
} 

int m_pos = 90;
int l_pos = 90;
int r_pos = 90;
int c_pos = 25;

void loop() 

{
  m_pos = analogRead(0);
  
  middle.write(m_pos);
  left.write(l_pos);
  right.write(r_pos);
  claw.write(c_pos)
  ;
//  delay(300); // doesn't constantly update the servos which can fry them
  Serial.print("middle: ");
  Serial.print(m_pos);
  delay(300);
} 
