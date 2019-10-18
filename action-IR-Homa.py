from hermes_python.hermes import Hermes
import socket, time, sys

intent_choose_device = "player"
intent_command = "Befehl"


def action_wrapper(hermes, intent_message):

	hermes.publish_continue_session(intent_message.session_id, sentence, [        INTENT_ANSWER,        INTENT_INTERRUPT,        INTENT_DOES_NOT_KNOW    ])



if __name__ == "__main__":
    with Hermes(MQTT_ADDR) as h:
        h.subscribe_intent("c0wtschpotato:ControlPart", conversational_control).start()