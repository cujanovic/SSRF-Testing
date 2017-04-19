#!/usr/bin/python

from __future__ import print_function
from random import *
from io import open
import datetime
import string
import os
import sys
import platform

def RANDOM_TEXT_SPEC():
	min_char = 12
	max_char = 16
	chars = string.ascii_letters + string.digits + "!$%^&*()<>;:,.|\~`"
	return "".join(choice(chars) for x in range(randint(min_char, max_char)))

def RANDOM_TEXT():
	min_char = 12
	max_char = 16
	chars = string.ascii_letters + string.digits
	return "".join(choice(chars) for x in range(randint(min_char, max_char)))

def DECIMAL_SINGLE(NUMBER,STEP):
	return int(NUMBER)*(256**STEP)

def HEX_SINGLE(NUMBER,ADD0X):
	if ADD0X == "yes":
		return str(hex(int(NUMBER)))
	else:
		return str(hex(int(NUMBER))).replace("0x","")

def OCT_SINGLE(NUMBER):
	return str(oct(int(NUMBER))).replace("o","")

def DEC_OVERFLOW_SINGLE(NUMBER):
	return str(int(NUMBER)+256)

def validIP(address):
	parts = address.split(".")
	if len(parts) != 4:
		return False
	for item in parts:
		if not 0 <= int(item) <= 255:
			return False
	return True

if len(sys.argv) < 2 or len(sys.argv) >= 4:
	print("\nUsage: python "+sys.argv[0]+" IP EXPORT(optional)\nUsage: python "+sys.argv[0]+" 169.254.169.254\nUsage: python "+sys.argv[0]+" 169.254.169.254 export")
	exit(1)

redcolor='\x1b[0;31;40m'
greencolor='\x1b[0;32;40m'
yellowcolor='\x1b[0;33;40m'
bluecolor='\x1b[0;36;40m'
resetcolor='\x1b[0m'
arg1 = str(sys.argv[1])

if validIP(arg1) == False:
	print("\n",yellowcolor,arg1,resetcolor,redcolor," is not a valid IPv4 address in dotted decimal format, example: 123.123.123.123",resetcolor,sep='')
	print("\nUsage: python "+sys.argv[0]+" IP EXPORT(optional)\nUsage: python "+sys.argv[0]+" 169.254.169.254\nUsage: python "+sys.argv[0]+" 169.254.169.254 export")
	exit(1)

ipFrag3, ipFrag2, ipFrag1, ipFrag0 = arg1.split(".")
RANDPREFIXTEXT=RANDOM_TEXT()
RANDPREFIXTEXTSPEC=RANDOM_TEXT_SPEC()
RANDOMPREFIXVALIDSITE='www.google.com'
FILENAME=''

try:
	sys.argv[2]
except IndexError:
	EXPORTRESULTS=''
else:
	EXPORTRESULTS=str(sys.argv[2])

if EXPORTRESULTS == 'export':
	FILENAME = "export-" + arg1 + "-" + str(datetime.datetime.now().strftime("%H-%M-%d-%m-%Y"))+'.txt'
	pythonversion = (platform.python_version())
	major, minor, patchlevel = pythonversion.split(".")
	if major == "3":
		f = open(FILENAME, 'w')
	else:
		f = open(FILENAME, 'wb')

#Case 1 - Dotted hexadecimal
print("\n",sep='')
print(bluecolor,"Dotted hexadecimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP1 = HEX_SINGLE(ipFrag3,"yes") + "." + HEX_SINGLE(ipFrag2,"yes") + "." + HEX_SINGLE(ipFrag1,"yes") + "." + HEX_SINGLE(ipFrag0,"yes")
print('http://',IP1,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP1,sep='')
print('http://',RANDPREFIXTEXT,'@',IP1,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP1,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP1,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP1,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP1,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP1,file=f,sep='')

#Case 2 - Dotless hexadecimal
print(bluecolor,"Dotless hexadecimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP2 = HEX_SINGLE(ipFrag3,"yes") + HEX_SINGLE(ipFrag2,"no") + HEX_SINGLE(ipFrag1,"no") + HEX_SINGLE(ipFrag0,"no")
print('http://',IP2,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP2,sep='')
print('http://',RANDPREFIXTEXT,'@',IP2,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP2,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP2,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP2,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP2,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP2,file=f,sep='')

#Case 3 - Dotless decimal
print(bluecolor,"Dotless decimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP3 = str(DECIMAL_SINGLE(ipFrag3,3) + DECIMAL_SINGLE(ipFrag2,2) + DECIMAL_SINGLE(ipFrag1,1) + DECIMAL_SINGLE(ipFrag0,0))
print('http://',IP3,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP3,sep='')
print('http://',RANDPREFIXTEXT,'@',IP3,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP3,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP3,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP3,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP3,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP3,file=f,sep='')

#Case 4 - Dotted decimal with overflow(256)
print(bluecolor,"Dotted decimal with overflow(256) IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP4 = DEC_OVERFLOW_SINGLE(ipFrag3) + "." + DEC_OVERFLOW_SINGLE(ipFrag2) + "." + DEC_OVERFLOW_SINGLE(ipFrag1) + "." + DEC_OVERFLOW_SINGLE(ipFrag0)
print('http://',IP4,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP4,sep='')
print('http://',RANDPREFIXTEXT,'@',IP4,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP4,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP4,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP4,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP4,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP4,file=f,sep='')

#Case 5 - Dotted octal
print(bluecolor,"Dotted octal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP5 = OCT_SINGLE(ipFrag3) + "." + OCT_SINGLE(ipFrag2) + "." + OCT_SINGLE(ipFrag1) + "." + OCT_SINGLE(ipFrag0)
print('http://',IP5,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP5,sep='')
print('http://',RANDPREFIXTEXT,'@',IP5,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP5,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP5,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP5,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP5,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP5,file=f,sep='')

#Case 6 - Dotted octal with padding
print(bluecolor,"Dotted octal with padding IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP6 = '0' + OCT_SINGLE(ipFrag3) + "." + '00' + OCT_SINGLE(ipFrag2) + "." + '000' + OCT_SINGLE(ipFrag1) + "." + '0000' + OCT_SINGLE(ipFrag0)
print('http://',IP6,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP6,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP6,sep='')
print('http://',RANDPREFIXTEXT,'@',IP6,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP6,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP6,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP6,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP6,file=f,sep='')

#Case 7 - IPv6 compact version
print(bluecolor,"IPv6 compact version IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP7 = '[::' + ipFrag3 + "." + ipFrag2 + "." + ipFrag1 + "." + ipFrag0 + ']'
print('http://',IP7,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP7,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP7,sep='')
print('http://',RANDPREFIXTEXT,'@',IP7,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP7,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP7,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP7,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP7,file=f,sep='')

#Case 8 - IPv6 mapped version
print(bluecolor,"IPv6 mapped version IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP8 = '[::ffff:' + ipFrag3 + "." + ipFrag2 + "." + ipFrag1 + "." + ipFrag0 + ']'
print('http://',IP8,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP8,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP8,sep='')
print('http://',RANDPREFIXTEXT,'@',IP8,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP8,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP8,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP8,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP8,file=f,sep='')

#Case 9 - Dotted hexadecimal + Dotted octal + Dotless decimal
print(bluecolor,"Dotted hexadecimal + Dotted octal + Dotless decimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP9 = HEX_SINGLE(ipFrag3,"yes") + "." + OCT_SINGLE(ipFrag2) + "." + str(DECIMAL_SINGLE(ipFrag1,1) + DECIMAL_SINGLE(ipFrag0,0))
print('http://',IP9,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP9,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP9,sep='')
print('http://',RANDPREFIXTEXT,'@',IP9,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP9,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP9,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP9,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP9,file=f,sep='')

#Case 10 - Dotted hexadecimal + Dotless decimal
print(bluecolor,"Dotted hexadecimal + Dotless decimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP10 = HEX_SINGLE(ipFrag3,"yes") + "." + str(DECIMAL_SINGLE(ipFrag2,2) + DECIMAL_SINGLE(ipFrag1,1) + DECIMAL_SINGLE(ipFrag0,0))
print('http://',IP10,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP10,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP10,sep='')
print('http://',RANDPREFIXTEXT,'@',IP10,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP10,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP10,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP10,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP10,file=f,sep='')

#Case 11 - Dotted octal with padding + Dotless decimal
print(bluecolor,"Dotted octal with padding + Dotless decimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP11 = '0' + OCT_SINGLE(ipFrag3) + "." + str(DECIMAL_SINGLE(ipFrag2,2) + DECIMAL_SINGLE(ipFrag1,1) + DECIMAL_SINGLE(ipFrag0,0))
print('http://',IP11,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP11,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP11,sep='')
print('http://',RANDPREFIXTEXT,'@',IP11,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP11,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP11,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP11,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP11,file=f,sep='')

#Case 12 - Dotted octal with padding + Dotted hexadecimal + Dotless decimal
print(bluecolor,"Dotted octal with padding + Dotted hexadecimal + Dotless decimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP12 = '0' + OCT_SINGLE(ipFrag3) + "." + HEX_SINGLE(ipFrag2,"yes") + "." + str(DECIMAL_SINGLE(ipFrag1,1) + DECIMAL_SINGLE(ipFrag0,0))
print('http://',IP12,sep='')
print('http://',RANDOMPREFIXVALIDSITE,'@',IP12,sep='')
print('http://',RANDPREFIXTEXTSPEC,'@',IP12,sep='')
print('http://',RANDPREFIXTEXT,'@',IP12,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IP12,file=f,sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IP12,file=f,sep='')
	print('http://',RANDPREFIXTEXT,'@',IP12,file=f,sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IP12,file=f,sep='')

if EXPORTRESULTS == 'export':
	f.close()
	print("\n",bluecolor,'-----------------------------------------------------------------------------------------------------------------------------------------',resetcolor,sep='')
	print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
	print("Results are exported to: " + FILENAME,sep='')
	print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
	print(bluecolor,'-----------------------------------------------------------------------------------------------------------------------------------------',resetcolor,sep='')
	print("\n",sep='')
