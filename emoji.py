#!/bin/env python3
import sys
def parseChar(data, char):
	if data["string"] != None:
		if char == "\U0001f4ac": # speech balloon
			data["stack"].append(data["string"])
			data["string"] = None
		else:
			data["string"] += char
	if char == "\U0001f4ac": # speech balloon
		data["string"] = ""
	elif char == "\u27a1": # black rightwards arrow
		print(data["stack"].pop())
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
