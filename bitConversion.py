

# Functions to handle input from file
def hexToAscii(fileName):
	f = open(fileName)

	for line in f.readlines():
		result = binascii.a2b_hex("%s" % (line.strip()))

	f.close()
	return result

def binToHex(fileName):
	f = open(fileName)

	for line in f.readlines():
		data = line.strip()

	result = hex(int(data,2))
	return result

def binToAscii(filename):
	hexVal = binToHex(filename)
	asciiVal = hexStringToAscii(hexVal)
	return asciiVal

# Functions to handle input from stdin

# Converts binary input from stdin to hex
def binStringToHex(data):
	result = hex(int(data,2))
	return result

def hexStringToAscii(data):

	data = data[2:].strip()

	if(len(data) % 2 != 0):
		data = data[:-1]



	# result = binascii.unhexlify(data)
	result = data.decode("hex")

	# result = str(base64.b16decode(data))[2:-1]
	
	return result

# Converts hex string to ascii string
def customHexToAscii(data):
	data = data[2:].strip()
	data = data[:-1]
	result = ''.join([chr(int(''.join(c),16)) 
		for c in zip(data[0::2],data[1::2])])
	return result

# Combined process of bin->hex, hex->ascii functions
def binStringToAscii(data):
	hexVal = binStringToHex(data)
	asciiVal = customHexToAscii(hexVal)
	return asciiVal


