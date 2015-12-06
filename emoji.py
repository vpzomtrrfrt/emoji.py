#!/bin/env python3
import sys
def parseChar(data, char):
	if data["string"] != None:
		if char == "\U0001f4ac": # speech balloon (end string)
			data["stack"].append(data["string"])
			data["string"] = None
		else:
			data["string"] += char
	if char == "\U0001f4ac": # speech balloon (begin string)
		data["string"] = ""
	elif char == "\u27a1": # black rightwards arrow (print)
		print(data["stack"].pop())
	elif char == "\U0001f6b2": # bicycle (true)
		data["stack"].append(True)
	elif char == "\U0001f6b3": # no bicycles (false)
		data["stack"].append(False)
def emojiEval(s, stack=[]):
	data = {
		"string": None,
		"stack": stack
	}
	for c in s:
		parseChar(data, c)
if __name__ == "__main__":
	if len(sys.argv) == 1:
		emojiEval(sys.stdin.read())
	else:
		h = open(sys.argv[1])
		s = h.read()
		h.close()
		emojiEval(s, sys.argv[2:])
