int trig =7;
int echo =8;
int duration, distance ;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(trig,OUTPUT);
pinMode(echo,INPUT);

}
// this is test 

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(trig,LOW);
delayMicroseconds(2);
digitalWrite(trig,HIGH);
delayMicroseconds(10);
digitalWrite(trig,LOW);

duration = pulseIn(echo,HIGH);

distance = duration / 29 / 2 ;

if ( distance < 10 ) {
  Serial.println("C");
  delay(4000);
}
else {
  Serial.println("S");
}
delay(10);
}
