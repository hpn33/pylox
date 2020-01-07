from scanner import Scanner

f = open('script.lox')

s = Scanner(f.read())

for tok in s.scan_tokens():
	print(tok)
	# print(tok.typ, '::', tok.lexeme, '::', tok.line)

f.close()
