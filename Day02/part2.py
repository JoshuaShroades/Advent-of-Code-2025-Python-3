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
			for j in range(len(i_str)//2+1):
				if(
					i_str.count(i_str[:j]) > 1
					and i_str.count(i_str[:j]) * len(i_str[:j]) == len(i_str)
				):
					total += i
					break
	return total
