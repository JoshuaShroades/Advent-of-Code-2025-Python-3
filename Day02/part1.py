import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	total = 0
	ranges = lines[0].split(",")
	for r in ranges:
		start, end = r.split("-")
		for i in range(int(start), int(end) + 1):
			i_str = str(i)
			if(i_str[len(i_str)//2:] == i_str[:len(i_str)//2]):
				total += i
	return total
