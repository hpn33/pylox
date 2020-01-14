from enum import Enum, auto


class TokenType(Enum):
	# single character tokens
	LEFT_PAREN = auto()
	RIGHT_PAREN = auto()
	LEFT_BRACE = auto()
	RIGHT_BRACE = auto()
	COMMA = auto()
	DOT = auto()
	MINUS = auto()
	PLUS = auto()
	SEMICOLON = auto()
	SLASH = auto()
	STAR = auto()
	COLON = auto()
	
	# one or two character tokens
	BANG = auto()
	BANG_EQUAL = auto()
	EQUAL = auto()
	EQUAL_EQUAL = auto()
	GREATER = auto()
	GREATER_EQUAL = auto()
	LESS = auto()
	LESS_EQUAL = auto()
	
	# literals
	IDENTIFIER = auto()
	STRING = auto()
	NUMBER = auto()
	
	# keywords
	AND = auto()
	CLASS = auto()
	ELSE = auto()
	FALSE = auto()
	FUN = auto()
	FOR = auto()
	IF = auto()
	NIL = auto()
	OR = auto()
	PRINT = auto()
	RETURN = auto()
	SUPER = auto()
	THIS = auto()
	TRUE = auto()
	VAR = auto()
	WHILE = auto()
	
	EOF = auto()


class Hook:
	keyword = {
		'and': TokenType.AND,
		'class': TokenType.CLASS,
		'else': TokenType.ELSE,
		'false': TokenType.FALSE,
		'for': TokenType.FOR,
		'fun': TokenType.FUN,
		'if': TokenType.IF,
		'nil': TokenType.NIL,
		'or': TokenType.OR,
		'print': TokenType.PRINT,
		'return': TokenType.RETURN,
		'super': TokenType.SUPER,
		'this': TokenType.THIS,
		'true': TokenType.TRUE,
		'var': TokenType.VAR,
		'while': TokenType.WHILE
	}
	
	symbol = {
		'(': TokenType.LEFT_PAREN,
		')': TokenType.RIGHT_PAREN,
		'{': TokenType.LEFT_BRACE,
		'}': TokenType.RIGHT_BRACE,
		',': TokenType.COMMA,
		'.': TokenType.DOT,
		'-': TokenType.MINUS,
		'+': TokenType.PLUS,
		';': TokenType.SEMICOLON,
		':': TokenType.COLON,
		'*': TokenType.STAR,
		
		'!': TokenType.BANG,
		'=': TokenType.EQUAL,
		'<': TokenType.LESS,
		'>': TokenType.GREATER,
		'!=': TokenType.BANG_EQUAL,
		'==': TokenType.EQUAL_EQUAL,
		'<=': TokenType.LESS_EQUAL,
		'>=': TokenType.GREATER_EQUAL
	}
	
	statement = [
		TokenType.CLASS, TokenType.FUN,
		TokenType.VAR, TokenType.VAR,
		TokenType.FOR, TokenType.IF,
		TokenType.WHILE, TokenType.PRINT,
		TokenType.RETURN
	]
	
	liner = [' ', '\r', '\t', '\n']
	string = ['"', "'"]
