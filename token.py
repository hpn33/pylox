from enum import Enum, auto


class Token(object):
    def __init__(self, token_type, lexeme, literal, line):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f'{self.token_type} {self.lexeme} {self.literal}'


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
