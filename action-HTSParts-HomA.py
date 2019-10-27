#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes
import socket, time, sys, configparser, os
syn_smooth = ["weich","smooth","sanfter wechsel"]
syn_blinken =["blinken", "flash"]
config = configparser.ConfigParser()
cfgpath = "cfg.ini"


def action_wrapper(hermes, intent_message):
	config.read(cfgpath)
	try:
		first = intent_message.slots.HTSParts.first().value
	except:
		result_sentence = "Fehler"
		current_session_id = intent_message.session_id
		hermes.publish_end_session(current_session_id, result_sentence)

	

	if first == "an":
		if config["philips"]["power"] != "1":
			config['philips']['power'] = '1'
			result_sentence = "HTS bereits an"
	if first == "aus":
		if config["philips"]["power"] != "0":
			config['philips']['power'] = '0'
			result_sentence = "HTS bereits aus"

	if first == "lauter":
		config["philips"]["vol_up"] = "1"
		result_sentence = ""
	if first == "leiser":
		config["philips"]["vol_down"] = "1"
		result_sentence = ""
	if first == "HDMI":
		config["philips"]["targetchannel"] = "0"
		result_sentence = "schalte um"
	if first == "bluetooth":
		config["philips"]["targetchannel"] = "2"
		result_sentence = "schalte um"
	if first == "pc an":
		config["11001"]["1"] = "1"
		time.sleep(0.2)
		config["11001"]["2"] = "1"
		time.sleep(0.2)
		config["philips"]["power"] = "1"
		result_sentence = "pc läuft"
		

	with open(cfgpath, 'w') as configfile:
		config.write(configfile)
	current_session_id = intent_message.session_id
	result_sentence = ""
	hermes.publish_end_session(current_session_id, result_sentence)








if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:SamsungHTSSteuerung", action_wrapper).start()