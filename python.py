import time
import serial
import smtplib
import sys

TO = 'receiver@xyz.com'
FROM = 'user@gmail.com'
PASS = 'user_password'

SUBJECT1 = 'ALERT'
SUBJECT2 = 'DISARMED'

BODY1 = 'Movement has been detected in your room'
BODY2 = 'Your device has been disarmed'

message1 = "SUBJECT : %s\n\n%s" % (SUBJECT1,BODY1)
message2 = "SUBJECT : %s\n\n%s" % (SUBJECT2,BODY2)

k =0

ser = serial.Serial('port',9600)   #replace port name here
print("serial port set...\n")

smtpserver = smtplib.SMTP('smtp.gmail.com',587)
smtpserver.starttls()
smtpserver.login(FROM,PASS)

print("logged in...\n")


def email1() :
    print ("sending intrusion mail")
    smtpserver.sendmail(FROM,TO,message1)
    print ("mail sent...\n")
   
def email2() :
   print ("sending disarmed mail")
   smtpserver.sendmail(FROM,TO,message2)
   print("email sent...\n")
   
while True :  

    try:
       
          msg = ser.readline()
          if msg[0] == 'C' :
              email1()
          k = 0 
              
    except (IOError,serial.serialutil.SerialException):
       if k== 0:
           email2(); 
       else:
           time.sleep(2)
       k=k+1    
         
