# Controling RF Devices with an ESP8266 Board via MQTT
Controlling RF devices with an [ESP8266](https://www.espressif.com/en/products/socs/esp8266) &amp; a RF transmitter over [MQTT](https://mqtt.org/) and using [Apple HomeKit](https://en.wikipedia.org/wiki/HomeKit) with [Homebridge](https://homebridge.io/) to use the Home app and Siri (Google's Android and Amazon's Alexa can also be used).

This project's primary goal is to use an ESP8266 with an RF transmitter for cost-effective upgrading to control existing standard RF controllable blinds.
For this purpose, Somfy blinds were used to control over a command prompt and Apple's HomeKit via MQTT and the ESP8266 board.

_Further Resources:_
* [Arduino](https://www.arduino.cc/)
* [Homebridge](https://github.com/homebridge/homebridge)

# Step 1: Setting up the ESP8266
In this project, a microcontroller (Wemos mini ESP8266) was equipped with a 433 Mhz radio transmitter.
The board was sketched using the Arduino software to upload the required files. 

1. A ticker will be required to call your functions.
  * [Arduino documentation](https://arduino-esp8266.readthedocs.io/en/latest/libraries.html)
* Example libraries: [Sample Library](https://github.com/sstaub/Ticker), [Arduino Github](https://arduino-esp8266.readthedocs.io/en/latest/libraries.html)

2. In addition, if you wish to communicate over the MQTT protocol, you will  require a pub client such the one form [Nick O'Leary]( https://github.com/spacefolder/esp8266-MQTT-v1). 

3. Finally, a config file will also be required containing information about the MQTT server/ broker to connect (see more details in the next step) and your information to connect to your wifi. 

# Step 2: MQTT Setup 
Setup of MQTT broker.

There are two main ways to approach this. You could either have your server, such as running it in your local network via a Raspberry Pi. 
A popular Python module called [Paho MQTT](https://pypi.org/project/paho-mqtt/) can be used 

```sudo pip install paho-mqtt```

Alternatively, you can use an MQTT broker available such as [CloudMQT](https://www.cloudmqtt.com/) .

# Step 3: Scripts and Usage
In this project, scripts for command line usage were created using the Python paho-mqtt module. 

Depending on the setup and use case, below is an example script (each action, such as stop, up, down has its own message/ script in MQTT):

```python
import paho.mqtt.client as mqtt
 
 
client = mqtt.Client()
client.connect(“MQTT broker address", port, 60)
client.publish(“topic/for/blinds", "desired message to trigger action");
client.disconnect();
```
# Setp 4: Utilizing Homebridge
Homebridge allows non-Apple-certified smart home devices to communicate with HomeKit for personal usage. 
Since the blinds will most likely be controlled throughout the day, it is advisable to run homebridge over raspberry pi; running homebridge over the computer will have the disadvantage of only working when your machine is running. 

One plugin that was used in this project is: [homebridge-blinds](https://github.com/dxdc/homebridge-blinds) designed to control blinds over HTTP requests or the native command line.

The python scripts from the previous step should be used to use this plugin and must be sent (via SCP) to the raspberry pi if used. 
* [Raspberry SCP](https://www.raspberrypi.org/documentation/remote-access/ssh/scp.md)

# Step 5: Control your blinds from your Apple device
Once your blinds are added to your homebridge config, they will appear in your HomeKit app when the bridge is added.
