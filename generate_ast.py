import os

output_dir = lambda file_name: f'grammar/{file_name}.py'


def define_ast(writer, base_name: str, types: []):
	writer.write(f'''from scanner import Scanner
from token import Token


class {base_name}:
	def accept(self, visitor):
		pass
''')
	
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
	
	define_visitor(writer, base_name, class_name)


def define_visitor(writer, base_name: str, class_name: str):
	writer.write(
		f'''
	def accept(self, visitor):
		visitor.visit{class_name + base_name}(self)
'''
	)


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
	
	path = 'grammar'
	name = 'Expr'
	
	if not os.path.isdir(path):
		os.mkdir(path)
	
	if not os.path.isfile(f'{name}.py'):
		os.mkdir(path + f'{name}.py')
	
	f = open(output_dir(name), 'w+')
	
	define_ast(f, name, base_desc)
