#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import socket, time, configparser
syn_couch = ["couch","sofa","led", "LED","kautsch"]## eigentlich sinnlos, von snips wird nur die eingestellte intent übertragen. synonyme müssen in der console gepflegt werden.
syn_iiyama = ["bildschirm","screen", "ijama","iiyama","iyama","iljama","kleiner","monitor"]
syn_fernseher =["fernseher", "großer", "groß", "gross", "philips","filips"]
syn_schlafzimmerlampe = ["schlafzimmerlampe","salzlampe","bettlampe"]

config = configparser.ConfigParser()
cfgpath = "cfg.ini"

def action_wrapper(hermes, intent_message):

    
    try:
        first = intent_message.slots.Geraet.first().value
    except:
        result_sentence = "Welches Gerät?"
        # s.close()
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)

    try:
        second = intent_message.slots.AnAus.first().value
    except:
        result_sentence = "Aktion nicht erkannt"
        current_session_id = intent_message.session_id
        hermes.publish_end_session(current_session_id, result_sentence)    
        
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(('192.168.1.107', 10000))
    config.read(cfgpath)
    if first in  syn_couch: ###steuerung der Couch An/Aus
        if second == "an" or second == "":
            # s.send(b'11001-3-1')
            result_sentence = first+" an"
            config['11001']['3'] = '1'
        if second == "aus":
            # s.send(b'11001-3-0')
            config['11001']['3'] = '0'
            result_sentence = first+" aus"
    
    if first in  syn_iiyama: ###steuerung der syn_iiyama An/Aus
        if second == "an" or second == "":
            # s.send(b'11001-2-1')
            config['11001']['2'] = '1'
            result_sentence = first+" an"
        if second == "aus":
            # s.send(b'11001-2-0')
            config['11001']['2'] = '0'
            result_sentence = first+" aus"
    
    if first in  syn_fernseher: ###steuerung der syn_fernseher An/Aus
        if second == "an" or second == "":
            # s.send(b'11001-1-1')
            config['11001']['1'] = '1'
            result_sentence = first+" an"
        if second == "aus":
            # s.send(b'11001-1-0')
            config['11001']['1'] = '0'
            result_sentence = first+" aus"
    
    if first in  syn_schlafzimmerlampe: ###steuerung der syn_schlafzimmerlampe An/Aus
        if second == "an" or second == "":
            # s.send(b'11001-4-1')
            config['11001']['4'] = '1'
            result_sentence = first+" an"
        if second == "aus":
            # s.send(b'11001-4-0')
            config['11001']['4'] = '0'
            result_sentence = first+" aus"  


    with open(cfgpath, 'w') as configfile:
        config.write(configfile)
    current_session_id = intent_message.session_id
    # s.close()
    result_sentence = ""## andere möglichkeit für silent mode 
    #current_session_id = intent_message.session_id
    #hermes.publish_end_session(current_session_id)##kein result sentence für silent mode, schnellere abwicklung und tests
    hermes.publish_end_session(current_session_id, result_sentence) #nicht silent mode



if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:MHZTrigger", action_wrapper).start()


