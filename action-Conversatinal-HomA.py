#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import socket, time, sys
intent_hts = "player"
intent_fertig = "ende"
intent_PC = "computer"
intent_command = "controlpart"

intent_filter_get_command = [intent_command,intent_fertig]

SessionsStates = {}

def action_wrapper(hermes, intent_message):
	current_session_id = intent_message.session_id


	if len(str(intent_message)) <= 0:## switched to string for len
		sentence = "Welches Gerät?"
		print("länge war 0")
	else:
		sentence = "okay, weiter"
		print("message erkannt")
	hermes.publish_continue_session(intent_message.session_id, sentence, intent_filter_get_command)
	

def control_hts(hermes, intent_message):
	current_session_id = intent_message.session_id


	if len(str(intent_message)) <= 0:## switched to string for len
		sentence = "Welches Gerät?"
		print("länge war 0")
	else:
		sentence = "okay, HTS Steuerung aktiv"
		print(" HTS message erkannt")



def control_pc(hermes, intent_message):
	current_session_id = intent_message.session_id


	if len(str(intent_message)) <= 0:## switched to string for len
		sentence = "Welches Gerät?"
		print("länge war 0")
	else:
		sentence = "okay, PC Steuerung aktiv"
		print(" PC message erkannt")



def control_fertig(hermes, intent_message):
	current_session_id = intent_message.session_id
	hermes.publish_end_session(intent_message.session_id, "Homecontrol Ende")




if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:Conversational", action_wrapper)\
        .subscribe_intent(intent_hts, control_hts) \
        .subscribe_intent(intent_PC, control_pc) \
        .subscribe_intent(intent_fertig, control_pc)\
        .start()