from scanner import Scanner

f = open('script.lox')

s = Scanner(f.read())
s.scan_tokens()

f.close()