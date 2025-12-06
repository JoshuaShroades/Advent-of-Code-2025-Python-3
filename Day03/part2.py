import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	total = 0
	for line in lines:
		digits = ""
		start = 0
		for i in range(12):
			end = len(line)-11+i
			digit = sorted(line[start:end])[-1]
			start += line[start:end].find(digit) + 1
			digits += digit
		total += int(digits)
	return total
