#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###make it executable
from hermes_python.hermes import Hermes
import socket, time


def action_wrapper(hermes, intent_message):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.1.107', 10000))
	s.send(b'couchled-color-red1')


	s.close()
	current_session_id = intent_message.session_id
	result_sentence = "Farbe geändert"
	hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:CouchFarbe", action_wrapper).start()