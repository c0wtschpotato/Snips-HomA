#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import socket, time

def action_wrapper(hermes, intent_message):

    first = int(intent_message.slots.Geraet.first().value)
    second = int(intent_message.slots.AnAus.first().value)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.107', 10000))
    s.send(b'11001-'+int(first)+'-'+int(second))
    s.close()
    result_sentence = "Okay"+first+" "+second
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("domi:getAddition", action_wrapper).start()
