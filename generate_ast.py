def define_ast(output_dir: str, base_name: str, types: []):
	writer = open(output_dir, 'w+')
	
	writer.write(
		f'''from scanner import Scanner
from token import Token


class {base_name}:
	pass
'''
	)
	
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
	define_ast('grammar.py', 'Expr', base_desc)
