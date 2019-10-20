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
	first = intent_message.slots.Farbe.first().value

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
	if first == "hdmi":
		config["philips"]["channel"] = "0"
		result_sentence = ""
	if first == "bluetooth":
		config["philips"]["channel"] = "2"
		result_sentence = ""



	current_session_id = intent_message.session_id
	result_sentence = ""
	hermes.publish_end_session(current_session_id, result_sentence)








if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:HTSParts", action_wrapper).start()