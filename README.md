# eyeofthebeholder

DISCLAIMER: I am not a professional software developer. This is hobbyist code; you get hobbyist level robustness and security. use at your own risk.

These are the python files for the robotic diceroller featured in my youtube video:
https://youtu.be/l3omaHxsk84

which is where you can also find the thingiverse link for the 3D printed portion.
I used a raspberry pi 3, which if you're not familiar with raspberry pi, I strongly suggest familiarizing yourself
before trying to take on this project. The camera is the type that plugs directly into the board.
For the final version I used a solderable breadboard, but the prototype was a rat's nest.
you should be able to see what pins go where from the python code. the power and ground
for the beam break and servo are straight from the RPi; this project is low enough power that 
it can run them. If you do want to implement the discord functionality you should read through this tutorial:
https://realpython.com/how-to-make-a-discord-bot-python/

That will run you through the discord bot creation and the program basics.
don't forget that your discord bot credentials go in the .env
file, and you will need to look up channel id#s because I'm not letting
ya'll post to the fleece and furnace.
