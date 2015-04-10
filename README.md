doorSensors
===========

scripts for sensing doors opening &amp; posting that to play services

Heavily borrows from https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/script

Make sure you serial port is not being used for anything else.  See http://elinux.org/RPi_Serial_Connection#Preventing_Linux_using_the_serial_port

You'll need to add a "keys.py" file to get this working.  It needs 2 lines:

```python
registration_ids="XXX"
authorization="YYY"
```

See http://developer.android.com/google/gcm/http.html for details of those values.  Right now, the registration ID is hardcoded to the value that's being logged to the eclipse console when I run the android client.  Eventually, I'll handle registrations automatically, but it's a TODO for now.
