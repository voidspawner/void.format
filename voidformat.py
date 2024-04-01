# V O I D spawner
# voidsp.com
# 2024

import gzip
import base64

class VoidFormat:

	METHOD_SHORT    = 'short'
	METHOD_TABLE    = 'table'
	METHOD_SETTINGS = 'settings'
	METHOD_CODE     = 'code'

	@staticmethod
	def encode(data, method: str = METHOD_SHORT, separator: str = None, indent: str = None):
		method = method.lower()
		if method == VoidFormat.METHOD_CODE:
			if indent == None:
				indent = '\t'
			return VoidFormat.encode_code(data, indent)
		elif method == VoidFormat.METHOD_SETTINGS:
			if indent == None:
				indent = '\t'
			return VoidFormat.encode_settings(data, indent)
		elif method == VoidFormat.METHOD_TABLE:
			if separator == None:
				separator = ' '
			return VoidFormat.encode_table(data, separator)
		if separator == None:
			separator = ' '
		return VoidFormat.encode_short(data, separator)

	@staticmethod
	def decode(text: str, method: str = METHOD_SHORT, separator: str = None, indent: str = None):
		method = method.lower()
		if method == VoidFormat.METHOD_CODE:
			if indent == None:
				indent = '\t'
			return VoidFormat.decode_code(text, indent)
		elif method == VoidFormat.METHOD_SETTINGS:
			if indent == None:
				indent = '\t'
			return VoidFormat.decode_settings(text, indent)
		elif method == VoidFormat.METHOD_TABLE:
			if separator == None:
				separator = ' '
			return VoidFormat.decode_table(text, separator)
		if separator == None:
			separator = ' '
		return VoidFormat.decode_short(text, separator)

	# Encode

	@staticmethod
	def encode_binary(data):
		text_base64 = str(base64.b64encode(data), "utf-8")
		text_gzip = str(base64.b64encode(gzip.compress(data)), "utf-8")
		return '|' + (text_gzip if len(text_gzip) < len(text_base64) else text_base64)

	@staticmethod
	def encode_short(data, separator: str = ' '):
		if len(separator) != 1:
			return
		data_type = type(data)
		if data_type is str:
			return data.replace('\\', '\\\\').replace('|', '\\|').replace('[', '\\[').replace(']', '\\]').replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t').replace('\b', '\\b').replace('\f', '\\f').replace(separator, '\\' + separator)
		elif data_type is int:
			return str(data)
		elif data_type is float:
			return str(data)
		elif data_type is bool:
			return 'true' if data else 'false'
		elif data is None:
			return 'null'
		elif data_type is list:
			result = '['
			first_value = True
			for value in data:
				if not first_value:
					result += separator
				else:
					first_value = False
				result += VoidFormat.encode_short(value, separator)
			result += ']'
			return result
		elif data_type is dict:
			result = '['
			first_value = True
			for name in data:
				value = data[name]
				if not first_value:
					result += separator
				else:
					first_value = False
				name = name.replace('\\', '\\\\').replace(':', '\\:').replace('|', '\\|').replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t').replace('\b', '\\b').replace('\f', '\\f').replace(separator, '\\' + separator)
				result += name + ':' + VoidFormat.encode_short(value, separator)
			result += ']'
			return result
		elif data_type == bytes:
			return VoidFormat.encode_binary(data)

	@staticmethod
	def encode_table(data: list, separator: str = ' '):
		if len(separator) != 1:
			return
		result = ''
		first_row = True
		for row in data:
			if type(row) is not list:
				return
			if not first_row:
				result += '\n'
			else:
				first_row = False
			first_value = True	
			for value in row:
				if not first_value:
					result += separator
				else:
					first_value = False
				data_type = type(value)
				if data_type is str:
					result += value.replace('\\', '\\\\').replace('|', '\\|').replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t').replace('\b', '\\b').replace('\f', '\\f').replace(separator, '\\' + separator)
				elif data_type is int:
					result += str(value)
				elif data_type is float:
					result += str(value)
				elif data_type is bool:
					result += 'true' if value else 'false'
				elif value is None:
					result += 'null'
				elif data_type == bytes:
					result += VoidFormat.encode_binary(data)
		return result

	@staticmethod
	def encode_settings(data, indent: str = '\t', level: int = 0):
		if len(indent) == 0:
			return
		data_type = type(data)
		if data_type is str:
			return (indent * level) + data
		elif data_type is int:
			return (indent * level) + str(data)
		elif data_type is float:
			return (indent * level) + str(data)
		elif data_type is bool:
			return (indent * level) + ('true' if data else 'false')
		elif data is None:
			return (indent * level) + 'null'
		elif data_type is list:
			result = ''
			first_value = True
			for value in data:
				if not first_value:
					result += '\n'
				result += VoidFormat.encode_settings(value, indent, level + 1)
				if first_value:
					first_value = False
			return result
		elif data_type is dict:
			result = ''
			first_value = True
			for name in data: 
				if not first_value:
					result += '\n'
				else:
					first_value = False			
				value = data[name]
				result += (indent * level) + name + '\n' + VoidFormat.encode_settings(value, indent, level + (1 if type(value) is not list else 0))
			return result
		elif data_type == bytes:
			return (indent * level) + VoidFormat.encode_binary(data)

	@staticmethod
	def encode_code(data: str, indent: str = '\t', level: int = 0):
		data_type = type(data)
		if data_type is str:
			result = data.replace('\\', '\\\\').replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t').replace('\b', '\\b').replace('\f', '\\f')
			if ' ' in result or '[' in result or ']' in result or '|' in result:
				result = '"' + result + '"'
			return (indent * level) + result
		elif data_type is int:
			return (indent * level) + str(data)
		elif data_type is float:
			return (indent * level) + str(data)
		elif data_type is bool:
			return (indent * level) + ('true' if data else 'false')
		elif data is None:
			return (indent * level) + 'null'
		elif data_type is list:
			if len(data) == 0:
				return '[]'
			first_value = True
			if len(data) < 4:
				result = (indent * level) + '['
				for value in data:
					if not first_value:
						result += ' '
					else:
						first_value = False
					result += VoidFormat.encode_code(value, indent)
				result += ']'
			else:
				result = ''
				for value in data:
					if not first_value:
						result += '\n'
					else:
						first_value = False
					result += VoidFormat.encode_code(value, indent, level)
			return result
		elif data_type is dict:
			result = ''
			first_value = True
			for name in data:
				value = data[name]
				if not first_value:
					result += '\n'
				else:
					first_value = False
				name = name.replace('\\', '\\\\').replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t').replace('\b', '\\b').replace('\f', '\\f')
				if ' ' in name or '[' in name or ']' in name or '|' in name:
					name = '"' + name + '"'
				result += (indent * level) + name + '\n' + VoidFormat.encode_code(value, indent, level + 1)
			return result
		elif data_type == bytes:
			return VoidFormat.encode_binary(data)


	# Decode

	@staticmethod
	def decode_binary(text: str):
		pass

	@staticmethod
	def decode_short(text: str, separator: str = ' '):
		pass

	@staticmethod
	def decode_table(text: str, separator: str = ' '):
		pass

	@staticmethod
	def decode_settings(text: str, indent: str = '\t'):
		pass

	@staticmethod
	def decode_code(text: str, indent: str = '\t'):
		pass

if __name__ == "__main__":
	
	import sys
	import os
	import json

	class App:

		@staticmethod
		def run():
			if len(sys.argv) > 1:
				method = sys.argv[1].lower()
				data = {
					'short': [1, 2, 3, True, False, None, 23.94, "text", "text text", [11, 22], {"name": "value 1", "name 2": "value 2", "other":"other", "another":123}, b"abc"],
					'table': [[1, "text", 10.1], [2, "text 2", 10.2], [3, "text\t3", 10.3]],
					'settings': {
						"Product": {
							"Name": "Bread",
							"Price": "$0.8",
							"Count": 200,
							"Weight": 800,
							"Tax": "10%",
							"Image": b"abc",
							"Payment Method": ["VISA", "MasterCard", "PayPal"]
						}
					},
					'code': {
						'settings': {
							'cli': {
								'color': True
							}
						},
						'run': [
							['.', 'Hi!'],
							['=', 'value', 100],
							['+', 'value', 1],
							['.', '{value}']
						]
					}
				}
				if method == 'encode.short':
					data_short = data['short'].copy()
					data_short[-1] = 'binary data `abc`'
					separator = App.separator()
					App.show('short', data_short, VoidFormat.encode(data['short'], method=VoidFormat.METHOD_SHORT, separator=separator))
				elif method == 'encode.table':
					separator = App.separator()
					App.show('table', data['table'], VoidFormat.encode(data['table'], method=VoidFormat.METHOD_TABLE, separator=separator))
				elif method == 'encode.settings':
					data_settings = data['settings'].copy()
					data_settings['Product'] = data_settings['Product'].copy()
					data_settings['Product']['Image'] = 'binary data `abc`'
					indent = App.indent()
					App.show('settings', data_settings, VoidFormat.encode(data['settings'], method=VoidFormat.METHOD_SETTINGS, indent=indent))
				elif method == 'encode.code':
					indent = App.indent()
					App.show('code', data['code'], VoidFormat.encode(data['code'], method=VoidFormat.METHOD_CODE, indent=indent))
				elif method == 'encode.short.json':
					file_data = App.file_data()
					separator = App.separator(True)
					App.show('short', file_data, VoidFormat.encode(file_data, method=VoidFormat.METHOD_SHORT, separator=separator))
				elif method == 'encode.table.json':
					file_data = App.file_data()
					separator = App.separator(True)
					App.show('table', file_data, VoidFormat.encode(file_data, method=VoidFormat.METHOD_TABLE, separator=separator))
				elif method == 'encode.settings.json':
					file_data = App.file_data()
					indent = App.indent(True)
					App.show('settings', file_data, VoidFormat.encode(file_data, method=VoidFormat.METHOD_SETTINGS, indent=indent))
				elif method == 'encode.code.json':
					file_data = App.file_data()
					indent = App.indent(True)
					App.show('code', file_data, VoidFormat.encode(file_data, method=VoidFormat.METHOD_CODE, indent=indent))
				elif method == 'decode.short.file':
					return
				elif method == 'decode.table.file':
					return
				elif method == 'decode.settings.file':
					return
				elif method == 'decode.code.file':
					return
			App.help()

		@staticmethod
		def help():
			file = os.path.basename(sys.argv[0])
			print('V O I D format')
			print('Types')
			print('    short')
			print('        separator')
			print('    table')
			print('        separator')
			print('    settings')
			print('        indent')
			print('    code')
			print('        indent')
			print('Use')
			print(f'    Encode short format')
			print(f'        python {file} encode.short\n')
			print(f'    Encode short format with comma separator')
			print(f'        python {file} encode.short ,\n')
			print(f'    Encode short format with tab separator')
			print(f'        python {file} encode.short \\t\n')
			print(f'    Encode short format from JSON')
			print(f'        python {file} encode.short.json example.json\n')
			print(f'    Encode table format with comma separator from JSON')
			print(f'        python {file} encode.table.json example.json ,\n')
			print(f'    Decode short format from file')
			print(f'        python {file} decode.short.file example.void')

		@staticmethod
		def show(method: str, data, text):
			print('JSON')
			print(json.dumps(data, indent=4))
			print()
			print('V O I D format ' + method)
			print(text)
			exit()
			
		@staticmethod
		def file_data():
			path = sys.argv[2] if len(sys.argv) > 2 else 'example.json'
			return App.json_read(path)

		@staticmethod
		def separator(file: bool = False):
			index = 2 if not file else 3
			separator = sys.argv[2] if len(sys.argv) > index else ' '
			if separator == '\\t':
				separator = '\t'
			return separator

		@staticmethod
		def indent(file: bool = False):
			index = 2 if not file else 3
			indent = sys.argv[index] if len(sys.argv) > index else '  '
			if indent == '\\t':
				indent = '\t'
			return indent

		@staticmethod
		def json_read(path: str):
			if os.path.exists(path):
				file = open(path, 'r')
				text = file.read()
				file.close()
				data = json.loads(text)
				if data != None:
					return data
				else:
					return {"error": "JSON not decoded"}
			return {"error": "File not found"}

	App.run()