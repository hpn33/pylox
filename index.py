import scanner
import grammer

fr = scanner.FileReader('script.lox')

print(fr.lines)
s = scanner.Scanner(fr)
del fr



for a in grammer.assignment.keys():
	print(a, ' ', grammer.assignment[a])
