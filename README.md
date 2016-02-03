doorSensors
===========

scripts for sensing doors opening &amp; posting that to play services

Heavily borrows from https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/script

Make sure you serial port is not being used for anything else.  See http://elinux.org/RPi_Serial_Connection#Preventing_Linux_using_the_serial_port

I've switched over to messaging via [pushbullet](https://www.pushbullet.com/) as the web API was a bit easier/more flexible.  You'll need an account for authorization keys.  Add them to a "keys.py" file to get this working.  It needs 2 lines:

```python
pushbullet_key=="XXX"
pushbullet_device="YYY"
```

See [https://docs.pushbullet.com/] for details of those values.  Right now, the registration ID is hardcoded to the value that's being logged to the eclipse console when I run the android client.  Eventually, I'll handle registrations automatically, but it's a TODO for now.
