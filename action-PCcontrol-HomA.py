#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
from hermes_python.hermes import Hermes

client = mqtt.Client()


def action_wrapper(hermes, intent_message):
	client.connect("192.168.1.103", 1883, 60)
	print("publishing message to"+str(intent_message.slots.message.first().value))
	if not intent_message.slots.message.first():
		current_session_id = intent_message.session_id
		hermes.publish_end_session(current_session_id, "Mediasteuerung abgebochen")

	client.publish(intent_message.slots.channel.first().value,intent_message.slots.message.first().value)
	print("published message"+ intent_message.slots.channel.first().value+" "+intent_message.slots.message.first().value)
	current_session_id = intent_message.session_id
	hermes.publish_end_session(current_session_id, "")







if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:PCcontrol", action_wrapper).start()