#include <Wire.h>
#define SLAVE_ADDRESS 0x04
void setup()
{
    Serial.begin(115200); // start serial for output
    Wire.begin(SLAVE_ADDRESS);
    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);
}
int val,flag=0;
void loop()
{
  if(flag==1)
   {
     Serial.print(val);
     flag=0;
   }
}
void receiveData(int byteCount)
{
    while(Wire.available()>0)
    {
      val=Wire.read();
      flag=1;
    }
}
// callback for sending data
void sendData()
{
  char a = Serial.read();
if(a > 0){
  Wire.write(a);
}
}
