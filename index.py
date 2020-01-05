import util
import scanner

fr = scanner.file_reader('script.lox')

s = scanner.scanner(fr.lines)
del fr

print(fr)

s.get_tokens()
