#!/usr/bin/python

import poplib
import string, random
import StringIO, rfc822
import logging
import sys
import re

def matchLine(line):
	match = re.search("([^=]+)= ?(.*)", line)
	matchb = re.search("\(([^)]+)\)", line)
	if match:
		return [match.group(1), match.group(2)]
	if matchb:
		return [matchb.group(1), matchb.group(1)]
	return False


if len(sys.argv) > 1 and sys.argv[1] == "test":
	test = "test(some value)"
	testb = "key=another kind of value"
	match = re.search("test\(([^)]+)\)", test)
	if match:
		print "A: %s\n"% match.group(1)
	matchb = re.search("([^=]+)=(.*)", testb)
	if matchb:
		print "B: KEY(%s) = VALUE(%s)\n"% (matchb.group(1), matchb.group(2))
	def matchLine(line):
		match = re.search("([^=]+)= ?(.*)", line)
		if match:
			print "kv pair: %s = %s\n"% (match.group(1), match.group(2))
			return [match.group(1), match.group(2)]
		matchb = re.search("\(([^)]+)\)", line)
		if matchb:
			print "basic paren enclosure: (%s)\n"% matchb.group(1)
			return ["code", matchb.group(1)]
		return False 
	with open('samplemail') as mailbody:
		lines = mailbody.readlines( )
		matches = list(map(matchLine, lines))
		print "matches:\n"
		print matches
	sys.exit(2)


SERVER = "pop.gmail.com"

with open('.nosec/gmail') as gm:
	lines = gm.readlines( )
	USERNAME = lines[0].strip( )
	PASSWORD = lines[1].strip( )

pop = poplib.POP3_SSL(SERVER, 995)
pop.set_debuglevel(1)
pop.user(USERNAME)
pop.pass_(PASSWORD)

print pop.stat( )
resp, items, octets = pop.list( )

def item( it ):
	id, size = string.split(it)
	resp, text, octets = pop.retr(id)
	msg = string.join(text, "\n")
	message = rfc822.Message(StringIO.StringIO(string.join(text,"\n")))
	subject = message['Subject']
	match = re.match("Xxyy", subject)
	if match:
		body = message.fp.read( )
		matches = list(map(matchLine, body.split("\n")))
		if len(matches):
			print matches

		#return message.fp.read( )
		return message['Subject']

items = list(map(lambda x: item(x), items[-5:]))

sys.exit(2)
