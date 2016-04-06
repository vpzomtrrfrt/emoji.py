# Unit Tests for Emoji interpreter
import emoji
import unittest
def getResults(s, stack=None):
	if stack == None:
		stack = []
	emoji.emojiEval(s, stack)
	if len(stack) == 1:
		return stack[0]
	else:
		tr = ""
		for i in range(0, len(stack)):
			if i != 0:
				tr += ", "
			tr += str(stack[i])
		return tr
# constants for readability
SPEECH = "\U0001f4ac"
PUMP = "\u26fd"
CAR = "\U0001f698"
RUN = "\U0001f3c3"
TO_PHONE = "\U0001f4f2"
PHONE = "\U0001f4f1"
NUMBERS = "\U0001f522"
HOLD_HANDS = "\U0001f46b"
WAVE = "\U0001f30a"
FAMILY = "\U0001f46a"
FORK_KNIFE = "\U0001f374"
FLYING_MONEY = "\U0001f4b8"
BICYCLE = "\U0001f6b2"
NO_BICYCLES = "\U0001f6b3"
BICYCLIST = "\U0001f6b4"
DISC = "\U0001f4bf"
INBOX = "\U0001f4e5"
OUTBOX = "\U0001f4e4"
END = "\U0001f51a"
BACK = "\U0001f519"
PENGUIN = "\U0001f427"
CHICK = "\U0001f423"
CHICKEN = "\U0001f414"
OX = "\U0001f402"
LOOP = "\U0001f503"
BUSTS = "\U0001f465"
TWO_MEN = "\U0001f46c"
SYMBOLS = "\U0001f523"
MAGNIFIER = "\U0001f50d"
CURL_PAGE = "\U0001f4c3"
SCISSORS = "\u2702"
LOUD_SPEAKER = "\U0001f50a"
QUIET_SPEAKER = "\U0001f509"
BOOKS = "\U0001f4da"
PUSHPIN = "\U0001f4cc"
KEY = "\U0001f511"
TWISTED_ARROWS = "\U0001f500"
class EmojiTests(unittest.TestCase):
	def testStrings(self):
		self.assertEqual(getResults(SPEECH+"test"+SPEECH), "test")
	def testFunctionString(self):
		self.assertEqual(getResults(PUMP+"test"+CAR), "test")
	def testNestedFunctionString(self):
		self.assertEqual(getResults(PUMP+PUMP+"nested"+CAR+CAR), PUMP+"nested"+CAR)
	def testRunFunction(self):
		self.assertEqual(getResults(PUMP+SPEECH+"test"+SPEECH+CAR+RUN), "test")
	def testVariables(self):
		self.assertEqual(getResults(SPEECH+"test"+SPEECH+SPEECH+"a"+SPEECH+TO_PHONE+SPEECH+"a"+SPEECH+PHONE), "test")
	def testNumbers(self):
		self.assertEqual(getResults(SPEECH+"42"+SPEECH+NUMBERS), 42)
	def testAdd(self):
		self.assertEqual(getResults(SPEECH+"9"+SPEECH+NUMBERS+SPEECH+"10"+SPEECH+NUMBERS+HOLD_HANDS), 19)
	def testSubtract(self):
		self.assertEqual(getResults(SPEECH+"9"+SPEECH+NUMBERS+SPEECH+"10"+SPEECH+NUMBERS+WAVE), -1)
	def testMultiply(self):
		self.assertEqual(getResults(SPEECH+"9"+SPEECH+NUMBERS+SPEECH+"10"+SPEECH+NUMBERS+FAMILY), 90)
	def testDivide(self):
		self.assertEqual(getResults(SPEECH+"10"+SPEECH+NUMBERS+SPEECH+"2"+SPEECH+NUMBERS+FORK_KNIFE), 5)
	def testModulo(self):
		self.assertEqual(getResults(SPEECH+"9"+SPEECH+NUMBERS+SPEECH+"2"+SPEECH+NUMBERS+FLYING_MONEY), 1)
	def testBooleanTrue(self):
		self.assertTrue(getResults(BICYCLE))
	def testBooleanFalse(self):
		self.assertFalse(getResults(NO_BICYCLES))
	def testNot(self):
		self.assertTrue(getResults(NO_BICYCLES+BICYCLIST))
		self.assertFalse(getResults(BICYCLE+BICYCLIST))
	def testRound(self):
		self.assertEqual(getResults(SPEECH+"4.7"+SPEECH+NUMBERS+DISC), 5)
		self.assertEqual(getResults(SPEECH+"4.3"+SPEECH+NUMBERS+DISC), 4)
	def testFloor(self):
		self.assertEqual(getResults(SPEECH+"4.7"+SPEECH+NUMBERS+INBOX), 4)
		self.assertEqual(getResults(SPEECH+"4.3"+SPEECH+NUMBERS+INBOX), 4)
	def testCeil(self):
		self.assertEqual(getResults(SPEECH+"4.7"+SPEECH+NUMBERS+OUTBOX), 5)
		self.assertEqual(getResults(SPEECH+"4.3"+SPEECH+NUMBERS+OUTBOX), 5)
	def testIf(self):
		self.assertEqual(getResults(BICYCLE+END+SPEECH+"test"+SPEECH+PENGUIN), "test")
		self.assertEqual(getResults(NO_BICYCLES+END+SPEECH+"test"+SPEECH+PENGUIN), "")
	def testElse(self):
		func = END+SPEECH+"test"+SPEECH+PENGUIN+BACK+SPEECH+"hi"+SPEECH+PENGUIN
		self.assertEqual(getResults(func, [False]), "hi")
		self.assertEqual(getResults(func, [True]), "test")
	def testLessThan(self):
		self.assertTrue(getResults(SPEECH+"5"+SPEECH+NUMBERS+SPEECH+"6"+SPEECH+NUMBERS+CHICK))
		self.assertFalse(getResults(SPEECH+"5"+SPEECH+NUMBERS+SPEECH+"4"+SPEECH+NUMBERS+CHICK))
		self.assertFalse(getResults(SPEECH+"5"+SPEECH+NUMBERS+SPEECH+"5"+SPEECH+NUMBERS+CHICK))
	def testGreaterThan(self):
		self.assertFalse(getResults(SPEECH+"5"+SPEECH+NUMBERS+SPEECH+"6"+SPEECH+NUMBERS+CHICKEN))
		self.assertTrue(getResults(SPEECH+"5"+SPEECH+NUMBERS+SPEECH+"4"+SPEECH+NUMBERS+CHICKEN))
		self.assertFalse(getResults(SPEECH+"5"+SPEECH+NUMBERS+SPEECH+"5"+SPEECH+NUMBERS+CHICKEN))
	def testToHex(self):
		self.assertEqual(getResults(SPEECH+"16"+SPEECH+NUMBERS+OX), "0x10")
	def testWhile(self):
		self.assertEqual(getResults(SPEECH+"0"+SPEECH+NUMBERS+SPEECH+"i"+SPEECH+TO_PHONE+PUMP+SPEECH+"i"+SPEECH+PHONE+BUSTS+SPEECH+"5"+SPEECH+NUMBERS+CHICK+CAR+PUMP+SPEECH+"i"+SPEECH+PHONE+SPEECH+"1"+SPEECH+NUMBERS+HOLD_HANDS+SPEECH+"i"+SPEECH+TO_PHONE+CAR+LOOP), "0.0, 1.0, 2.0, 3.0, 4.0, 5.0")
	def testEquals(self):
		self.assertTrue(getResults(TWO_MEN, [4, 4]))
		self.assertFalse(getResults(TWO_MEN, [19, 21]))
	def testToCharCode(self):
		self.assertEqual(getResults(PUMP+SPEECH+CAR+SYMBOLS), 0x1f4ac)
		self.assertEqual(getResults(SPEECH+" "+SPEECH+SYMBOLS), 32)
	def testFromCharCode(self):
		self.assertEqual(getResults(SPEECH+"0x1f4ac"+SPEECH+NUMBERS+MAGNIFIER), SPEECH)
		self.assertEqual(getResults(SPEECH+"32"+SPEECH+NUMBERS+MAGNIFIER), " ")
	def testLength(self):
		self.assertEqual(getResults(SPEECH+"test message!"+SPEECH+CURL_PAGE), 13)
		self.assertEqual(getResults(SPEECH+SPEECH+CURL_PAGE), 0)
	def testSubstring(self):
		self.assertEqual(getResults(SPEECH+"hello"+SPEECH+SPEECH+"2"+SPEECH+SPEECH+"4"+SPEECH+SCISSORS), "ll")
	def testCapitalize(self):
		self.assertEqual(getResults(SPEECH+"It's over 9000"+SPEECH+LOUD_SPEAKER), "IT'S OVER 9000")
	def testLowercase(self):
		self.assertEqual(getResults(SPEECH+"Hi"+SPEECH+QUIET_SPEAKER), "hi")
	def testArray(self):
		var = SPEECH+"v"+SPEECH
		self.assertEqual(getResults(BOOKS+var+TO_PHONE+var+PHONE+BICYCLE+PUSHPIN+var+PHONE+SPEECH+"hi"+SPEECH+PUSHPIN+var+PHONE+SPEECH+"0"+SPEECH+KEY), True)
	def testStringChar(self):
		self.assertEqual(getResults(SPEECH+"test"+SPEECH+SPEECH+"2"+SPEECH+KEY), "s")
	def testSwap(self):
		self.assertEqual(getResults(SPEECH+"1"+SPEECH+SPEECH+"2"+SPEECH+TWISTED_ARROWS), "2, 1")
	def testNesting(self):
		func = END+END+SPEECH+"hello"+SPEECH+PENGUIN+SPEECH+"world"+SPEECH+PENGUIN
		self.assertEqual(getResults(func, [True, True]), "hello, world")
		self.assertEqual(getResults(func, [True, False]), True)
		self.assertEqual(getResults(func, [False, True]), "world")
		self.assertEqual(getResults(func, [False, False]), False)
	def testConcat(self):
		self.assertEqual(getResults(SPEECH+"test "+SPEECH+SPEECH+"message"+SPEECH+HOLD_HANDS), "test message")
if __name__ == "__main__":
	unittest.main()
