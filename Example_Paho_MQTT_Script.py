import paho.mqtt.client as mqtt

# Copyright David Haunschild

client = mqtt.Client()
client.username_pw_set(username="username", password="password") #username & pw payload 
client.publish(“topic/for/blinds", "desired message to trigger action");
client.disconnect();

