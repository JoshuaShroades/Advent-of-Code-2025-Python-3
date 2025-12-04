import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	pos = 50
	zeroes = 0
	for line in lines:
		if(line[0] == "L"):
			zeroes += abs((pos - int(line[1:])) // 100)
			if(pos == 0):
				zeroes -= 1
			pos -= int(line[1:])
			pos %= 100
			if(pos == 0):
				zeroes += 1
		elif(line[0] == "R"):
			zeroes += (pos + int(line[1:])) // 100
			pos += int(line[1:])
			pos %= 100
	return zeroes
