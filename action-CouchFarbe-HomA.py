#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###make it executable, maybe git desktop overwrites
from hermes_python.hermes import Hermes
import socket, time, sys, configparser, os,json
import paho.mqtt.client as mqtt
syn_smooth = ["weich","smooth","sanfter wechsel"]
syn_blinken =["blinken", "flash"]
config = configparser.ConfigParser()
cfgpath = "cfg.ini"
#/home/pi/HomeAutomation-python-Base/
HOST = '192.168.1.107'
PORT = 1883
client = mqtt.Client()

def action_wrapper(hermes, intent_message):

	config.read(cfgpath)
	# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# s.connect(('192.168.1.107', 10000))
	client.connect(HOST, 1883, 60)
	try:
		info = intent_message.slots.GiveInfo.first().value
		result_sentence = "Ich kenne rot, grün und blau 1 bis 5  Außerdem pink lila violett türkis  gelb und orange. Außerdem kannst du mit mir HTS und den PC steuern"
		current_session_id = intent_message.session_id
		hermes.publish_end_session(current_session_id, result_sentence)
		# s.close()
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
		colorcomb = {"r":"10","g":"255","b":"60"}

	if first == "grün 2" or first == "grün zwei":
		# s.send(b'couchled-color-green2')
		config.read(cfgpath)
		config["couchled"]["color"] = "green2"
		colorcomb = {"r":"0","g":"255","b":"10"}
	if first == "grün 1" or first == "grün eins" or first == "grün" or first == "grünes":
		# s.send(b'couchled-color-green1')
		config.read(cfgpath)
		config["couchled"]["color"] = "green1"
		colorcomb = {"r":"0","g":"255","b":"0"}

	if first == "grün 5" or first == "grün fünf" or first == "türkis" or first == "türkises":
		# s.send(b'couchled-color-green5')
		config.read(cfgpath)
		config["couchled"]["color"] = "green5"
		colorcomb = {"r":"10","g":"255","b":"60"}
	if first == "blau 5" or first == "blau fünf" or first == "pink" or first == "pinkes":
		# s.send(b'couchled-color-blue5')
		config.read(cfgpath)
		config["couchled"]["color"] = "blue5"
		colorcomb = {"r":"230","g":"0","b":"80"}

	if first == "blau 4" or first == "blau vier":
		# s.send(b'couchled-color-blue4')
		config.read(cfgpath)
		config["couchled"]["color"] = "blue4"
		colorcomb = {"r":"230","g":"0","b":"60"}

	if first == "blau 3" or first == "blau drei" or first == "lila":
		# s.send(b'couchled-color-blue3')
		config.read(cfgpath)
		config["couchled"]["color"] = "blue3"
		colorcomb = {"r":"230","g":"0","b":"115"}

	if first == "blau 2" or first == "blau zwei" or first == "violett" or first == "violettes":
		# s.send(b'couchled-color-blue2')
		config.read(cfgpath)
		config["couchled"]["color"] = "blue2"
		colorcomb = {"r":"204","g":"0","b":"153"}

	if first == "blau 1" or first == "blau eins" or first == "blau" or first == "blaues":
		# s.send(b'couchled-color-blue1')
		config.read(cfgpath)
		config["couchled"]["color"] = "blue1"
		colorcomb = {"r":"50","g":"0","b":"255"}

	if first == "rot 5" or first == "rot fünf":
		# s.send(b'couchled-color-red5')
		config.read(cfgpath)
		config["couchled"]["color"] = "red5"
		colorcomb = {"r":"255","g":"180","b":"0"}
	if first == "rot 4" or first == "rot vier" or first == "gelb" or first == "gelbes":
		# s.send(b'couchled-color-red4')
		config.read(cfgpath)
		config["couchled"]["color"] = "red4"
		colorcomb = {"r":"255","g":"130","b":"0"}
	if first == "rot 3" or first == "rot drei":
		# s.send(b'couchled-color-red3')
		config.read(cfgpath)
		config["couchled"]["color"] = "red3"
		colorcomb = {"r":"255","g":"100","b":"0"}
	if first == "rot 2" or first == "rot zwei" or first == "orange" or first == "oranges" or first == "orangenes":
		# s.send(b'couchled-color-red2')
		config.read(cfgpath)
		config["couchled"]["color"] = "red2"
		colorcomb = {"r":"255","g":"50","b":"0"}
	if first == "rot 1" or first == "rot eins" or first == "rot" or first == "rotes":
		# s.send(b'couchled-color-red1')
		config.read(cfgpath)
		config["couchled"]["color"] = "red1"
		colorcomb = {"r":"255","g":"0","b":"0"}
	if first == "weiß":
		# s.send(b'couchled-color-white1')
		config.read(cfgpath)
		config["couchled"]["color"] = "white1"
		colorcomb = {"r":"255","g":"120","b":"60"}
			#### Programme

	if first in syn_blinken:
		config.read(cfgpath)
		
	if first == "strobe" or first == "smooth" or first == "fade":
		# s.send(b'couchled-programm-strobe')
		config["couchled"]["color"] = first
	
	if first == "heller":
		# s.send(b'couchled-brightness_up-1')
		# time.sleep(0.1)
		# s.send(b'couchled-brightness_up-1')
		config["couchled"]["brightness_up"] = "1"
	if first == "dunkler":
		# s.send(b'couchled-brightness_down-1')
		# time.sleep(0.1)
		# s.send(b'couchled-brightness_down-1')
		config["couchled"]["brightness_down"] = "1"
	if first == "regenbogen":
		payload= {"function":"rainbow_colors"}
		data = json.dumps(payload)
		client.publish("HomA/ledstrip1/set_status",data)
		return

	if first == "white 1":
		config["couchled"]["color"] = "white1"
		colorcomb = {"r":"255","g":"120","b":"60"}

	with open(cfgpath, 'w') as configfile:
		config.write(configfile)
	# s.close()
	try :
		payload ={"function":"setalltocolor",
			"basecolor":colorcomb,
			"runningcolor":{"r":"255","g":"0","b":"0"},
			"number_of_running":"5",
			"sleep_time":"0.1"}
		data = json.dumps(payload)
		client.publish("HomA/ledstrip1/set_status",data)
	except:
		pass
	
	
	current_session_id = intent_message.session_id
	result_sentence = ""
	hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:CouchFarbe", action_wrapper).start()