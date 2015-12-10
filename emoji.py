#!/bin/env python3
import sys
import traceback
def parseChar(data, char):
	blockStarts = (
		"\U0001f51a" # end with arrow (if)
	)
	if data["string"] != None: # parsing a string
		if char == "\U0001f4ac": # speech balloon (end string)
			data["stack"].append(data["string"])
			data["string"] = None
		else:
			data["string"] += char
	elif data["func"] != None:
		if char == "\U0001f698": # oncoming automobile (end function)
			if data["skip"] > 0:
				data["skip"] -= 1
				data["func"] += char
			else:
				data["stack"].append(data["func"])
				data["func"] = None
		else:
			if char == "\u26fd": # fuel pump (begin function)
				data["skip"] += 1
			data["func"] += char
	elif data["skip"] > 0:
		if char == "\U0001f427": # penguin (end block)
			data["skip"] -= 1
		elif char in blockStarts:
			data["skip"] += 1
	elif char == "\U0001f4ac": # speech balloon (begin string)
		data["string"] = ""
	elif char == "\u27a1": # black rightwards arrow (print)
		print(data["stack"].pop())
	elif char == "\U0001f6b2": # bicycle (true)
		data["stack"].append(True)
	elif char == "\U0001f6b3": # no bicycles (false)
		data["stack"].append(False)
	elif char == "\U0001f6b4": # bicyclist (not)
		data["stack"].append(not data["stack"].pop())
	elif char == "\U0001f46b": # man and woman holding hands (add)
		a = data["stack"].pop()
		data["stack"].append(data["stack"].pop()+a)
	elif char == "\U0001f46a": # family (multiply)
		data["stack"].append(data["stack"].pop()*data["stack"].pop())
	elif char == "\U0001f30a": # water wave (subtract)
		data["stack"].append(-(data["stack"].pop()-data["stack"].pop()))
	elif char == "\U0001f374": # fork and knife (divide)
		data["stack"].append(1/(data["stack"].pop()/data["stack"].pop()))
	elif char == "\U0001f4b8": # money with wings (modulo)
		a = data["stack"].pop()
		data["stack"].append(data["stack"].pop()%a)
	elif char == "\U0001f4bf": # optical disc (round)
		data["stack"].append(int(round(data["stack"].pop())))
	elif char == "\U0001f4e5": # inbox (round down)
		data["stack"].append(int(data["stack"].pop()))
	elif char == "\U0001f4e4": # outbox (round up)
		data["stack"].append(int(data["stack"].pop()+1))
	elif char == "\U0001f402": # ox (convert to hex string)
		data["stack"].append(hex(int(data["stack"].pop())))
	elif char == "\U0001f522": # input symbol for numbers (parse float)
		data["stack"].append(float(data["stack"].pop()))
	elif char == "\U0001f46c": # two men holding hands (equal)
		data["stack"].append(data["stack"].pop()==data["stack"].pop())
	elif char == "\U0001f423": # hatching chick (less than)
		a = data["stack"].pop()
		data["stack"].append(data["stack"].pop()<a)
	elif char == "\U0001f414": # chicken (greater than)
		a = data["stack"].pop()
		data["stack"].append(data["stack"].pop()>a)
	elif char == "\U0001f51a": # end with arrow (if)
		if not data["stack"].pop():
			data["skip"] += 1
	elif char == "\U0001f503": # clockwise circle arrows (while)
		b = data["stack"].pop()
		c = data["stack"].pop()
		while True:
			emojiEvalSub(c, data)
			if not data["stack"].pop():
				break
			emojiEvalSub(b, data)
	elif char == "\U0001f465": # busts in silhouette (duplicate)
		a = data["stack"].pop()
		data["stack"].append(a)
		data["stack"].append(a)
	elif char == "\U0001f523": # input symbol for symbols (char code)
		data["stack"].append(ord(data["stack"].pop()))
	elif char == "\U0001f50d": # left-pointing magnifying glass (from char code)
		data["stack"].append(chr(int(data["stack"].pop())))
	elif char == "\U0001f4f2": # mobile phone with arrow (save to variable)
		n = data["stack"].pop()
		data["vars"][n] = data["stack"].pop()
	elif char == "\U0001f4f1": # mobile phone (get variable content)
		data["stack"].append(data["vars"][data["stack"].pop()])
	elif char == "\U0001f4c3": # page with curl (length)
		data["stack"].append(len(data["stack"].pop()))
	elif char == "\u2702": # scissors (substring)
		b = data["stack"].pop()
		a = data["stack"].pop()
		data["stack"].append(data["stack"].pop()[int(a):int(b)])
	elif char == "\u26fd": # fuel pump (begin function)
		data["func"] = ""
	elif char == "\U0001f3c3": # runner (run function)
		emojiEvalSub(data["stack"].pop(), data)
	elif char == "\U0001f50a": # speaker with three waves (capitalize)
		data["stack"].append(data["stack"].pop().upper())
	elif char == "\U0001f509": # speaker with one wave (lowercase)
		data["stack"].append(data["stack"].pop().lower())
	elif char == "\U0001f4da": # books (create array)
		data["stack"].append([])
	elif char == "\U0001f4cc": # pushpin (push element to array)
		e = data["stack"].pop()
		data["stack"].pop().append(e)
	elif char == "\U0001f511": # key (get array element / string character)
		i = data["stack"].pop()
		data["stack"].append(data["stack"].pop()[i])
	elif char == "\U0001f500": # twisted rightwards arrows (swap)
		b = data["stack"].pop()
		a = data["stack"].pop()
		data["stack"].append(b)
		data["stack"].append(a)
def emojiEvalSub(s, data):
	c = ""
	stackThen = []
	try:
		for i in range(0,len(s)):
			c = s[i]
			stackThen = data["stack"][:]
			parseChar(data, c)
	except:
		traceback.print_exc()
		print(data)
		print(stackThen)
		print(c)
def emojiEval(s, stack=[]):
	data = {
		"string": None,
		"stack": stack,
		"skip": 0,
		"vars": {},
		"func": None
	}
	emojiEvalSub(s, data)
if __name__ == "__main__":
	if len(sys.argv) == 1:
		emojiEval(sys.stdin.read())
	else:
		h = open(sys.argv[1])
		s = h.read()
		h.close()
		emojiEval(s, sys.argv[2:])
