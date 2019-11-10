#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

def action_wrapper(hermes, intent_message):
	client.connect("192.168.1.103", 1883, 60)
	print("publishing message to"+str(intent_message.slots.message.first().value))
	client.publish(intent_message.slots.message.first().value,intent_message.slots.channel.second().value)









if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:PCcontrol", action_wrapper).start()