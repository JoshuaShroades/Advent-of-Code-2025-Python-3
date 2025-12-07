import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

global lines
with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	global lines
	old_lines = lines
	rolls = "\n".join(lines).count("@")
	new_lines = remove_rolls(old_lines)
	while(new_lines != old_lines):
		old_lines = new_lines
		new_lines = remove_rolls(old_lines)
	return rolls - "\n".join(old_lines).count("@")

def remove_rolls(source):
	width = len(source[0])
	height = len(source)
	diagram = ""
	for y in range(height):
		line = ""
		for x in range(width):
			if(source[y][x] == "@"):
				blocking = -1
				for pos_y in range(max(y-1,0),min(y+1,height-1)+1):
					for pos_x in range(max(x-1,0),min(x+1,width-1)+1):
						if(source[pos_y][pos_x] == "@"):
							blocking += 1
				if(blocking < 4):
					line += "."
				else:
					line += "@"
			else:
				line += "."
		diagram += line + "\n"

	return diagram.split("\n")[:-1]
