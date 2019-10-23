#include <SoftwareSerial.h> // import bluetooth
#include <Servo.h>          //import servo
SoftwareSerial mySerial(2, 3);// TX, RX
Servo servo1; //กำหนด servo
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
    void setup() // set ขา servo
    {
      Serial.begin(9600);
      servo1.attach(8);  
      servo2.attach(9);
      servo3.attach(10);
      servo4.attach(11);
      servo5.attach(12);
      servo6.attach(13);
      while (!Serial) ;
      mySerial.begin(9600);
    }
    int angle;
    void loop()
    {  
      if(mySerial.available()){ // อ่านค่าจาก Bluetooth
        angle = mySerial.read();
      if (angle >= 0 && angle <=36){ // ช่วงมุมของ servo1
        angle = angle * 5;
        servo1.write(angle);
       }
      else if(angle >=37 && angle <= 73){ // ช่วงมุมของ servo2
        angle = angle - 37;
        angle = angle * 5;
        servo2.write(angle);
      }
      else if(angle >=74 && angle <= 110){ // ช่วงมุมของ servo3
        angle = angle - 74;
        angle = angle * 5;
        servo3.write(angle);
      }
      else if(angle >=111 && angle <= 147){ // ช่วงมุมของ servo4
        angle = angle - 111;
        angle = angle * 5;
        servo4.write(angle);
      }
      else if(angle >=148 && angle <= 184){ // ช่วงมุมของ servo5
        angle = angle - 148;
        angle = angle * 5;
        servo5.write(angle);
      }
      else if(angle >=185 && angle <= 221){ // ช่วงมุมของ servo6 ** servo6 ไม่ได้ใช้เพราะนำออกไป
        angle = angle - 185;
        angle = angle * 5;
        servo6.write(angle);
      }
      }
    }
