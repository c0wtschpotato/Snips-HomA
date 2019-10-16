	
from hermes_python.hermes import Hermes
import socket, time, sys


def action_wrapper(hermes, intent_message):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.1.107', 10000))


	try:
		first = intent_message.slots.LEDProgramm.first().value
	# 	if programm == "heller" or programm == "hell":
	# 		s.send(b"couchled-brightness_up-1")
	# 		s.close()
	# 		return
	# 	if programm == "dunkel" or programm == "dunkler":
	# 		s.send(b"couchled-brightness_down-1")
	# 		s.close()
	# 		return
		if first == "flash":
			#why the fuck
			s.send(b'couchled-programm-flash')
			s.close()
			current_session_id = intent_message.session_id
			hermes.publish_end_session(current_session_id, result_sentence)
			
	# 	if programm == "strobe":
	# 		s.send(b"couchled-programm-strobe")
	# 		s.close()
	# 		return
	# 	if programm == "smooth":
	# 		s.send(b"couchled-programm-smooth")
	# 		s.close()
	# 		return
	# 	if programm == "fade":
	# 		s.send(b"couchled-programm-fade")
	# 		s.close()
	# # 		return
	except:
		result_sentence = "!"

if __name__ == "__main__":
	with Hermes("localhost:1883") as h:
		h.subscribe_intent("c0wtschpotato:CouchFarbe", action_wrapper).start()