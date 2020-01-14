import os


def define_ast(writer, base_name: str, types: []):
	writer.write(f'''from scanner import Scanner
from token import Token


''')
	
	define_visitor(writer, base_name, types)
	
	writer.write(f'''

class {base_name}:
	def accept(self, visitor: ExprVisitor):
		raise NotImplementedError''')
	
	for typ_key in types:
		class_name = typ_key
		fields = types[typ_key]
		
		define_type(writer, base_name, class_name, fields)
	
	writer.close()


def define_type(writer, base_name: str, class_name: str, fields: []):
	store_temp = lambda key: f'\t\tself.{key} = {key}\n'
	
	# fields in constructor.
	all_fields = ''
	for key, value in fields.items():
		all_fields += f', {key}: {value}'
	
	# store fields.
	store_fields = ''
	for key in fields:
		store_fields += store_temp(key)
	
	writer.write(
		f'''


class {class_name}({base_name}):
	def __init__(self{all_fields}):
{store_fields}'''
	)
	
	# visitor pattern.
	writer.write(
		f'''
	def accept(self, visitor: ExprVisitor):
		return visitor.visit_{class_name.lower()}_{base_name.lower()}(self)''')


def define_visitor(writer, base_name: str, types: []):
	writer.write('class ExprVisitor:')
	for key, value in types.items():
		writer.write(
			f'''

	def visit_{key.lower()}_{base_name.lower()}(self, expr):
		raise NotImplementedError''')
	
	writer.write('\n')
	

base_desc = {
	'Binary': {
		'left': "Expr",
		'operator': 'Token',
		'right': 'Expr'
	},
	"Grouping": {'expression': 'Expr'},
	"Literal": {'value': 'object'},
	"Unary": {'operator': 'Token', 'right': 'Expr'}
}

if __name__ == '__main__':
	
	path = '../grammar'
	file_name = 'Expr'
	
	if not os.path.isdir(path):
		os.mkdir(path)
	
	if not os.path.isfile(f'{path}/{file_name}.py'):
		os.mkdir(path + f'{file_name}.py')
	
	f = open(f'grammar/{file_name}.py', 'w+')
	
	define_ast(f, file_name, base_desc)
