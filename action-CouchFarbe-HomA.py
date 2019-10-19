#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###make it executable, maybe git desktop overwrites
from hermes_python.hermes import Hermes
import socket, time, sys, configparser, os
syn_smooth = ["weich","smooth","sanfter wechsel"]
syn_blinken =["blinken", "flash"]
config = configparser.ConfigParser()
cfgpath = "cfg.ini"
#/home/pi/HomeAutomation-python-Base/

def action_wrapper(hermes, intent_message):
	config.read(cfgpath)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.1.107', 10000))
		
	try:
		info = intent_message.slots.GiveInfo.first().value
		result_sentence = "Ich kenne rot, grün und blau 1 bis 5  Außerdem pink lila violett türkis  gelb und orange."
		current_session_id = intent_message.session_id
		hermes.publish_end_session(current_session_id, result_sentence)
		s.close()
		return
	except:
		result_sentence = ""
	try:
		first = intent_message.slots.Farbe.first().value
	except:
		
		result_sentence = "Das hab ich nicht verstanden"
		current_session_id = intent_message.session_id
		hermes.publish_end_session(current_session_id, result_sentence)
	if first == "grün 4" or first == "grün vier":
		config.read(cfgpath)
		config['couchled']['color'] = 'green4'
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
	if first == "weiß":
		s.send(b'couchled-color-white1')

	#### Programme

	if first in syn_blinken:
		s.send(b'couchled-programm-flash')
		
	if first == "strobe" or first == "strobo":
		s.send(b'couchled-programm-strobe')
		
	if first in syn_smooth:
		s.send(b'couchled-programm-smooth')
		
	if first == "heller":
		s.send(b'couchled-brightness_up-1')
		time.sleep(0.1)
		s.send(b'couchled-brightness_up-1')
		
	if first == "dunkler":
		s.send(b'couchled-brightness_down-1')
		time.sleep(0.1)
		s.send(b'couchled-brightness_down-1')
		
	if first == "fade":
		s.send(b'couchled-programm-fade')

	with open(cfgpath, 'w') as configfile:
		config.write(configfile)
	s.close()
	current_session_id = intent_message.session_id
	result_sentence = ""
	hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:CouchFarbe", action_wrapper).start()