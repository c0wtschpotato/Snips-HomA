#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import socket, time, sys
intent_hts = "player"
intent_fertig = "ende"

def action_wrapper(hermes, intent_message):
	current_session_id = intent_message.session_id


	if len(str(intent_message)) <= 0:## switched to string for len
		sentence = "Welches Gerät?"
		print("länge war 0")
	else:
		sentence = "okay, weiter"
		print("message erkannt")
		hermes.publish_continue_session(intent_message.session_id,sentence,[intent_hts,intent_fertig])

	hermes.publish_end_session(intent_message.session_id, sentence)
if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:Conversational", action_wrapper).start()