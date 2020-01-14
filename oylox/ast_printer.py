from oylox.grammar.Expr import *
from oylox.util.token import Token
from oylox.util.token_type import TokenType


class AstPrinter(ExprVisitor):
	
	def print(self, expr: Expr) -> str:
		return expr.accept(self)
	
	def parenthesize(self, name: str, *exprs) -> str:
		string = f'({name}'
		for expr in exprs:
			string += ' '
			string += expr.accept(self)
		
		string += ')'
		
		return string
	
	def visit_binary_expr(self, expr: Binary) -> str:
		return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)
	
	def visit_grouping_expr(self, expr: Grouping) -> str:
		return self.parenthesize('group', expr.expression)
	
	def visit_literal_expr(self, expr: Literal) -> str:
		if expr.value is None:
			return 'nil'
		
		return f'{expr.value}'
	
	def visit_unary_expr(self, expr: Unary) -> str:
		return self.parenthesize(expr.operator.lexeme, expr.right)


if __name__ == '__main__':
	expression = Binary(
		Unary(
			Token(TokenType.MINUS, '-', None, 1),
			Literal(123)),
		Token(TokenType.STAR, '*', None, 1),
		Grouping(Literal(45.67))
	)
	
	print(AstPrinter().print(expression))
