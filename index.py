import scanner

fr = scanner.FileReader('script.lox')

print(fr.lines)
s = scanner.Scanner(fr)
del fr

# for tok in s.tokens:
# 	print(tok.type, ' ', tok.source)
