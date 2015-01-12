#!/usr/bin/python

import json 
import commands

end = "\033[0m"
blue = "\033[0;34m"
red = "\033[1;91m"
green = "\033[92m"

commands.getoutput("wget https://onionoo.torproject.org/summary?search=flag:Authority -O data.json")

authorities = open("data.json")
data = json.load(authorities)


print blue + "Information Gathering... \n" + end

for names in range (0,10):
	hostname = commands.getoutput('host ' + str(data['relays'][names]['a'][0]) + ' | grep "pointer" | cut -d " " -f 5 ')[:-1] 
	print data['relays'][names]['n'] + " has IP " + data['relays'][names]['a'][0] + " and hostname " + hostname

print "\n"
print blue + "Trying to connect to Authorities by dns... \n" + end

for pingdns in range (0,10):
	dnstest = commands.getoutput('host ' + str(data['relays'][pingdns]['a'][0]) + ' | grep "pointer" | cut -d " " -f 5 ')[:-1]
	response = commands.getoutput("ping -c 1 " + dnstest)
	if "1 received" in response:
		print dnstest + green + " is up" + end
	else:
		print dnstest + red + " is down" + end

print "\n"
print blue + "trying to connect to Authorities by IP... \n" + end

for pingip in range (0,10):
	pingtest = data['relays'][pingip]['a'][0]
	response = commands.getoutput("ping -c 1 " + pingtest)
	if "1 received" in response:
		print pingtest + green + " is up" + end
	else:
		print pingtest + red + " is down" + end
