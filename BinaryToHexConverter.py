
from bitConversion import binStringToAscii, binStringToHex
from dataFormat import formatBinary



def main():
	
	print("Enter data as bits:")
	binary1 = int(raw_input(),2)
	

	binaryFormatted = formatBinary(binary1)

	print("Formatted Binary:")
	print(binaryFormatted)

	print("Converted to Hex:")
	print(binStringToHex(binaryFormatted))

	print("Converted to Ascii:") 
	print(binStringToAscii(binaryFormatted))

	


if __name__ == "__main__":main()





















