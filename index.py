import util
import scanner
import grammer

fr = scanner.file_reader('script.lox')

s = scanner.scanner(fr.lines)
del fr


#s.get_tokens()



for a in grammer.assignment.keys():
	print(a, ' ', grammer.assignment[a])