#!/usr/bin/env python3
# -*- coding: utf-8 -*-
### useless line for testing 
from hermes_python.hermes import Hermes
import socket, time

def action_wrapper(hermes, intent_message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.107', 10000))
    s.send(b'11001-3-1')
    time.sleep(1)
    s.send(b'11001-3-0')
    s.close()
    result_sentence = "Nein, das sage ich dir nicht"
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("domi:getAddition", action_wrapper).start()

