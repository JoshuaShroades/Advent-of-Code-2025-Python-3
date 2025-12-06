import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	total = 0
	for line in lines:
		tens = sorted(line[:-1])[-1]
		ones = sorted(line[line.find(tens)+1:])[-1]
		total += int(tens + ones)
	return total
