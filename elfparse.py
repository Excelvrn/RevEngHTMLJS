import sys, os, re, string, io
from html.parser import HTMLParser as HP

import buchuchet, os1
tags = [0,0,0]
print(os1.find_attrs(sys.argv, 'kk'))
# How-to:
# python3 elfparse.py <filename> <text>
#print(sys.version)
print("Start\nsys.argv\t", len(sys.argv),":\n\t\t", sys.argv )

#print(len(sys.argv))
#print([ sys.argv, len(sys.argv) ])
vDebug=0

if (len(sys.argv)>3)and (vDebug==1):
	for i in range(0, len(sys.argv)):
		print([i, sys.argv[i]])
		pass
	print("---------")
	for i in range(0, len(sys.argv[3]), 2):
		print([ i, sys.argv[3], type(bytes.fromhex(sys.argv[3][i:i+2])), bytes.fromhex(sys.argv[3][i:i+2]), ord(bytes.fromhex(sys.argv[3][i:i+2])) ])
	print([sys.argv[3][0:2]])
	print(bytes.fromhex(sys.argv[3][0:2]))
	print(["ord", ord(bytes.fromhex(sys.argv[3][0:2]))])
	pass

def getattr(find, attrs):
	k=""
	for i in range(len(attrs)):
		if attrs[i][0] == find:
			k = attrs[i][1]
			print(attrs[i][0], k, sep = "\t")
		else:
			k="not_string"
	return k
	
def f4(s, f,lens):
	print("f4")
	sum = 0
	print([f,lens, len(f)])
	if (len(f)>1):
		for i in range(0, lens):
			if (s[i] == ord(f[0])):
				for i2 in range(1, len(f)):
					if (s[i+i2] != ord(f[i2])):
#						ret=-1
						break
					if (i2==(len(f)-1)):
						print([f, i])
						sum+=1
	else:		
		for i in range(0, lens):
			if (s[i] == ord(f)):
				sum+=1
				print([f, s[i], i])
	print(["sum", sum])
	pass

def f5(s, f,lens):
	print("---f5---")
	sum = 0
	print(["find", f,lens, len(f)])
#	print([f,lens, len(f)>>1])
#	print([f,lens, len(f)<<1])
#	ord(bytes.fromhex(f))
#	print(len(f))
#	for i in range(0, len(f), 2):
#		print([f[i:i+2], bytes.fromhex(f[i:i+2]), ord(bytes.fromhex(f[i:i+2]))])
#		pass
	for i in range(0, lens):
		for i2 in range(0, len(f)>>1):
			if (s[i+i2] != ord(bytes.fromhex(f[i2*2:i2*2+2])) ):
				break
			elif (i2 == (len(f)>>1)-1):
				sum+=1
				print([f, i, sum])
			else:
#				print(["equ", i])
				pass

			pass
		pass
	print(["sum", sum])
	pass

def cmpf(s, lens):
	print("cmpf")
	ret = -1;
	for i in range(0, 256):
		k=0
		for i2 in range(0, lens):
			if (s[i2]==i):
				k=k+1
		if k>0:
			print([i, k, chr(i)])
			pass
	print("\tPrint f:")
	return ret

def strings(s, f):
	sum = 0
	for i in range(0, len(s)):
		if (s[i] == f):
			sum+=1
			print([f, i])
			pass
		pass
	print(["sum is ", sum])
	return sum

def strings_cmp(s1, s2):
	for i1 in range(0, len(s1)):
		for i2 in range(0, len(s2)):
			if (s1[i1] == s2[i2]):
				print([i2, i1, s1[i1]])
				break
			pass
		pass
	pass

def strings_out(s1, s2):
	flag1 = 0
	for i1 in range(0, len(s1)):
		for i2 in range(0, len(s2)):
			if (s1[i1] == s2[i2]):
				print([i2, i1, s1[i1]])
				flag1 += 1
				break
			elif (len(s2) - i2 == 1):
				flag = 0
			pass
		pass
	pass

def chars(s1, s2, len1):
	ofs1 = 0
	ofs2 = 0
	for i1 in range(0, len1):
		for i2 in range(0, len(s2)):
			if (s1[i1] == s2[i2]):
#				print(s1[i1], i1)
				if (ofs1==0):
					ofs1 = i1
				else:
					ofs2+=1
				break
			elif (i2 == (len(s2) - 1)):
				if (ofs1!=0):
					if (ofs2>7):
						print(s1[ofs1:(ofs1+ofs2+1)], [ofs1, ofs2])
						ofs1=0
						ofs2=0
						
class MyHTMLParser(HP):
	buf = io.BufferedIOBase()
	file_name1 = io.TextIOWrapper(buf)	
	def handle_starttag(self, tag, attrs):
		if ((tag == "div")):
			tags[0]+=1
			print("\t", tag, "\t", tags[0], self.getpos()[1])
		elif ((tag == "span")):
			tags[1]+=1
			print("\t", tag, "\t", tags[1])
		elif ((tag == "a")):
			#tags[2]+=1
			print(len(attrs), getattr('href', attrs))
			if getattr('href', attrs) != "not_string":
				print(buchuchet.addr[0] + getattr('href', attrs), file = self.file_name1)
		else:
			print("\t", tag)
		pass
#		elif(tag=="p"):
#			print("\t\t", tag)			
	def handle_endtag(self, tag):
		if ((tag == "div")):
			print("****", tag, "\t", tags[0])
			tags[0]-=1
		elif ((tag == "span")):
			print("****", tag, "\t", tags[1])
			tags[1]-=1
		else:
			print("****", tag)
	#def handle_data(self, data):
	#	print("Encountered some data  :", data)

parser = MyHTMLParser()
#parser.feed('<html><head><title>Test</title></head>'
#			'<body><h1>Parse me!</h1></body></html>')

if len(sys.argv)==3:
	File = sys.argv[1]
	OpF = os.open(File, os.O_RDONLY)
	if (OpF>0):
		OpFsize = os.stat(File)[6]
		if OpFsize>0:
			OpFstr=os.read(OpF, os.stat(File)[6])	
			Root=sys.argv[2]
			pos = 0	
			f4(OpFstr, Root, OpFsize)
#			cmpf(OpFstr, OpFsize)
#			strings_cmp(str(OpFstr), string.punctuation)
#			strings_cmp(str(OpFstr), string.ascii_letters)
			chars(str(OpFstr), string.ascii_letters + string.digits + "."+"_"+"-", OpFsize)
			print("\tSmall size\n")
		os.close(OpF)
	else:
		print("Not Op")
elif (len(sys.argv)==4) or (strings(sys.argv, "d")>0) :
	File = sys.argv[1]
	# 1. python
	# 2. filename
	# 3. being opened
	# 4. operation
	# 5. parced
	OpF = os.open(File, os.O_RDONLY)
	if (OpF>0):
		OpFsize = os.stat(File)[6]
		if OpFsize>0:
			OpFstr=os.read(OpF, os.stat(File)[6])	
			Root=sys.argv[3]
			if (sys.argv[2] == 'd' ):
				f5(OpFstr, Root, OpFsize)
			elif (sys.argv[2] == 'h' ):
				parser.feed(str(OpFstr))
#			cmpf(OpFstr, OpFsize)
		else:
			print("\tSmall size\n")
		os.close(OpF)
	else:
		print("Not Op")
		pass
	pass
elif (strings(sys.argv, "html")>0):
	print("\thtml is:\t", os1.find_attrs(sys.argv, "html")[0])
	pass
elif(os1.find_attrs(sys.argv, "-stat")[0]):
	print("-stat:\t", sys.argv[2])
	#File = sys.argv[3]
	#OpF = os.open(File, os.O_RDONLY)
	#print(OpF)
	pass
else:
	print("not argument")
#	print("%(s)s" %{"s": "100", })
#	print(os1.find_attrs1(sys.argv, "ass"))
	pass


#print(string.ascii_letters+"-")
#print(sys.path)
def site():
	"asdfasdf"
	FD = open("a.txt", mode = 'a')
	parser.file_name1 = FD
	parser.feed(str(buchuchet.work2(buchuchet.addr, buchuchet.req2, "data_3.html")))
	#	print(data2[2: (len(data1) - 1)], file=FD)
	print(type(FD))
	#print(parser.file_name1)
	print(type(parser))
	FD.close()
	pass

print(site.__doc__)
print(os1.email_cut("execel8@ya.ru"))

