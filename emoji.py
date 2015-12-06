#!/bin/env python3
import sys
def parseChar(data, char):
	if data["string"] != None:
		if char == "\U0001f4ac": # speech balloon (end string)
			data["stack"].append(data["string"])
			data["string"] = None
		else:
			data["string"] += char
	elif char == "\U0001f4ac": # speech balloon (begin string)
		data["string"] = ""
	elif char == "\u27a1": # black rightwards arrow (print)
		print(data["stack"].pop())
	elif char == "\U0001f6b2": # bicycle (true)
		data["stack"].append(True)
	elif char == "\U0001f6b3": # no bicycles (false)
		data["stack"].append(False)
	elif char == "\U0001f46b": # man and woman holding hands (add)
		data["stack"].append(data["stack"].pop()+data["stack"].pop())
	elif char == "\U0001f46a": # family (multiply)
		data["stack"].append(data["stack"].pop()*data["stack"].pop())
	elif char == "\U0001f30a": # water wave (subtract)
		data["stack"].append(-(data["stack"].pop()-data["stack"].pop()))
	elif char == "\U0001f374": # fork and knife (divide)
		data["stack"].append(1/(data["stack"].pop()/data["stack"].pop()))
	elif char == "\U0001f4b8": # money with wings (modulo)
		a = data["stack"].pop()
		data["stack"].append(data["stack"].pop()%a)
	elif char == "\U0001f522": # input symbol for numbers (parse float)
		data["stack"].append(float(data["stack"].pop()))
def emojiEval(s, stack=[]):
	data = {
		"string": None,
		"stack": stack
	}
	try:
		for c in s:
			parseChar(data, c)
	except Exception as e:
		print(e)
		print(data)
if __name__ == "__main__":
	if len(sys.argv) == 1:
		emojiEval(sys.stdin.read())
	else:
		h = open(sys.argv[1])
		s = h.read()
		h.close()
		emojiEval(s, sys.argv[2:])
