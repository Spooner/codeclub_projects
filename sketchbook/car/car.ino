/*

 H-bridge control at 1-2ms high (low >= 20ms)
 1ms high => back
 1.5ms high => stop
 2ms high => forward
 
 Arduino PWM frequency is 490Hz (980Hz on 5 & 6)
 Assuming frequency is 500Hz:
 at 1.00 => 2.0 on and 0 off
 at 0.75 => 1.5 on and 0.5 off
 at 0.50 => 1ms on and 1ms off
 at 0.25 => 0.5ms on 1.5 off 
 
 */

const int LEFT =  9;
const int RIGHT = 10;
const int LED = 13;
const float PWM_FREQ = 490.0;

const int FAST_FWD = 255 * 1.0 - 1;
const int SLOW_FWD = 255 * 0.9;
const int STOP = 255 * 0.75;
const int SLOW_BWD = 255 * 0.6;
const int FAST_BWD = 255 * 0.5;

void setup() {
  //pinMode(LEFT, OUTPUT);
  //pinMode(RIGHT, OUTPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  both(FAST_FWD);
  delay(1000);
  both(STOP);
  delay(1000);
  both(SLOW_BWD);
  delay(1000);
  Serial.println("back");
  both(STOP);
  delay(1000);
}

void both(int speed)
{
  analogWrite(RIGHT, speed);
  analogWrite(LEFT, speed);
}


