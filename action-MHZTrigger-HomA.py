#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import socket, time

def action_wrapper(hermes, intent_message):

    first = intent_message.slots.Geraet.first().value
    second = intent_message.slots.AnAus.first().value
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.107', 10000))
    if first == "couch" or first == "sofa"  and second == 1:

        s.send(b'11001-3-1')
        result_sentence = "An wurde gesendet"
    else:
        result_sentence = ""
    time.sleep(3)
    s.send(b'11001-3-0')
    s.close()
    result_sentence = result_sentence + " " + first
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:MHZTrigger", action_wrapper).start()


