import os
import glob
import time
from twilio.rest import Client
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def send_message(message):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

     
    my_message = message
    message = client.messages \
                    .create(
                         body= my_message,
                         from_='+18064294286',
                         to='+14089814670'
                     )

    print(message.sid)

    
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f
    
def alert_temp(temp):
    
    if temp >= 70:
        str(temp)
        message = "*ALERT* Temp is %s" %(temp)
        send_message(message)
    elif temp <=45:
        str(temp)
        message = "*ALERT* Temp is %s" %(temp)
        send_message(message)
        
        
def main():
    while True:
        temp_data = read_temp()
        print(temp_data)
        alert_temp(temp_data)
        
        time.sleep(1800) #delay 30 min
    
# Download the helper library from https://www.twilio.com/docs/python/install

if __name__== "__main__":
    main()
   
    


