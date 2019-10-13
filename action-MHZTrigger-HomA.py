#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import socket, time
syn_couch = ["couch","sofa","led", "LED","kautsch"]
syn_iiyama = ["bildschirm","screen", "ijama","iiyama","iyama","iljama","kleiner"]

def action_wrapper(hermes, intent_message):

    first = intent_message.slots.Geraet.first().value
    second = intent_message.slots.AnAus.first().value
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.107', 10000))
    if first in  syn_couch:
        if second == "an":
            s.send(b'11001-3-1')
            result_sentence = first+" an"
        if second == "aus":
            s.send(b'11001-3-0')
            result_sentence = first+" aus"
    else:
        result_sentence = "Da ist was schief gelaufen"
   




        
    s.close()
    
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id)##kein result sentence für silent mode, schnellere abwicklung und tests
    #hermes.publish_end_session(current_session_id, result_sentence) #nicht silent mode

if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:MHZTrigger", action_wrapper).start()


