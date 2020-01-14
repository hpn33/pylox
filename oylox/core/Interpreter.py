from abc import ABC

from oylox.grammar.Expr import ExprVisitor, Expr, Grouping, Unary


class Interpreter(ExprVisitor, ABC):
	
	def visit_literal_expr(self, expr):
		return expr.value
	
	def visit_unary_expr(self, expr: Unary):
		right = self.evaluate(expr.right)
	
	
	def visit_grouping_expr(self, expr: Grouping):
		return self.evaluate(expr.expression)
	
	
	
	def evaluate(self, expr: Expr):
		return expr.accept(self)
