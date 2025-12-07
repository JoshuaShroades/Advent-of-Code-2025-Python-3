import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	width = len(lines[0])
	height = len(lines)
	total = 0
	for y in range(height):
		for x in range(width):
			if(lines[y][x] == "@"):
				blocking = -1
				for pos_y in range(max(y-1,0),min(y+1,height-1)+1):
					for pos_x in range(max(x-1,0),min(x+1,width-1)+1):
						if(lines[pos_y][pos_x] == "@"):
							blocking += 1
				if(blocking < 4):
					total += 1

	return total
