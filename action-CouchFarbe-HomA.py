#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###make it executable, maybe git desktop overwrites
from hermes_python.hermes import Hermes
import socket, time


def action_wrapper(hermes, intent_message):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.1.107', 10000))
	try:
		first = intent_message.slots.Geraet.first().value
	except:
		result_sentence = "Das hab ich nicht verstanden?"
		current_session_id = intent_message.session_id
		hermes.publish_end_session(current_session_id, result_sentence)
    if first == "grün 4" or first == "grün vier":
		s.send(b'couchled-color-green4')
	if first == "grün 3" or first == "grün drei":
		s.send(b'couchled-color-green3')
	if first == "grün 2" or first == "grün zwei":
		s.send(b'couchled-color-green2')
	if first == "grün 1" or first == "grün eins" or first == "grün" or first == "grünes":
		s.send(b'couchled-color-green1')
	if first == "grün 5" or first == "grün fünf" or first == "türkis" or first == "türkises":
		s.send(b'couchled-color-green5')
	if first == "blau 5" or first == "blau fünf" or first == "pink" or first == "pinkes":
		s.send(b'couchled-color-blue5')
	if first == "blau 4" or first == "blau vier":
		s.send(b'couchled-color-blue4')
	if first == "blau 3" or first == "blau drei" or first == "lila":
		s.send(b'couchled-color-blue3')
	if first == "blau 2" or first == "blau zwei" or first == "violett" or first == "violettes":
		s.send(b'couchled-color-blue2')
	if first == "blau 1" or first == "blau eins" or first == "blau" or first == "blaues":
		s.send(b'couchled-color-blue1')
	if first == "rot 5" or first == "rot fünf":
		s.send(b'couchled-color-red5')
	if first == "rot 4" or first == "rot vier" or first == "gelb" or first == "gelbes":
		s.send(b'couchled-color-red4')
	if first == "rot 3" or first == "rot drei":
		s.send(b'couchled-color-red3')
	if first == "rot 2" or first == "rot zwei" or first == "orange" or first == "oranges" or first == "orangenes":
		s.send(b'couchled-color-red2')
	if first == "rot 1" or first == "rot eins" or first == "rot" or first == "rotes":
		s.send(b'couchled-color-red1')



	s.close()
	current_session_id = intent_message.session_id
	result_sentence = "Farbe geändert"
	hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:CouchFarbe", action_wrapper).start()