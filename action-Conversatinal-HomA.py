from hermes_python.hermes import Hermes
import socket, time, sys


def action_wrapper(hermes, intent_message):




	hermes.publish_end_session(current_session_id, "no code here")
if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("c0wtschpotato:CouchFarbe", action_wrapper).start()