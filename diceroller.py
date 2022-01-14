import RPi.GPIO as GPIO
import time
import os
import discord
import subprocess
from dotenv import load_dotenv
from picamera import PiCamera

#Get GPIOS setup
IR_SENSOR = 11
SERVO = 8

#GPIO Seupt
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SERVO, GPIO.OUT)
p = GPIO.PWM(SERVO, 50)
p.start(12)
time.sleep(1)
p.ChangeDutyCycle(0)
time.sleep(1)
p.ChangeDutyCycle(10)
time.sleep(1)
p.ChangeDutyCycle(12)
time.sleep(1)
p.ChangeDutyCycle(0)

#get camera setup
camera = PiCamera()
camera.resolution = (2592,1944)
camera.exposure_mode = 'night'

#Wi-fi Checker
ps = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

#get discord setup
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

while True:
    #check for a wifi connection, if none, operate as a normal dice tower, loop forever
    try:
        output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
        print("Connected to")
        print(output)
        print('attempting to connect to discord')
        client = discord.Client()
        #discord Stuff
        @client.event
        async def on_ready():
            p.ChangeDutyCycle(10)
            time.sleep(0.25)
            p.ChangeDutyCycle(12)
            time.sleep(0.25)
            p.ChangeDutyCycle(10)
            time.sleep(0.25)
            p.ChangeDutyCycle(12)
            time.sleep(0.25)
            p.ChangeDutyCycle(0)
            client.loop.create_task(rolling())

        async def rolling():
            while(True):
               if(GPIO.input(IR_SENSOR) != 1):
                    time.sleep(1)
                    p.ChangeDutyCycle(10)
                    time.sleep(1)
                    camera.capture('/home/pi/Documents/diceroller/temp.jpg')
                    channel = client.get_channel(630996652311969793)
                    p.ChangeDutyCycle(12)
                    await channel.send(file=discord.File('/home/pi/Documents/diceroller/temp.jpg'))
                    time.sleep(1)
                    p.ChangeDutyCycle(0)
                    os.remove('/home/pi/Documents/diceroller/temp.jpg')
           
        client.run(TOKEN)
    except:
        print('no wifi connection')
        for i in range(100):
            if(GPIO.input(IR_SENSOR) != 1):
                time.sleep(1)
                p.ChangeDutyCycle(10)
                time.sleep(1)
                p.ChangeDutyCycle(12)
                time.sleep(1)
                p.ChangeDutyCycle(0)
            time.sleep(0.1)


