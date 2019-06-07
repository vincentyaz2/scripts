
# simple script to find a good set of colors

# representing a list with 6 ints
# hexadecimal notation here is represented as ints ranging from 0 to 15
# will be reconverted later on to 0-9 A-F notation
init = [0,0,0,0,0,0]


def converter(hex):
	'''returns a color in proper hexadecimal form'''

	if(hex < 0 or hex > 15):
		raise Exception('Hexadecimal values need to be between 0 and 15')
	
	# an alternative to generating alphabet btw
	# li = list(map(chr, range(ord('a'), ord('z')+1)))

	# list built from joining 0-9 and A-F
	standard_hex = [n for n in range(10)] + ([chr(n).upper() for n in range(ord('a'), ord('f')+1)])
	switcher = dict(zip(range(16),standard_hex))

	return switcher[hex]



def get_primary():
	'''returns a list with all three primary colors, red green blue'''
	return ['FF0000', '00FF00', '0000FF']


def get_complementary():
	'''
	returns a list with all three complementary colors

	cyan for red
	magenta for green
	yellow for blue

	'''
	return ['00FFFF', 'FF00FF', 'FFFF00']

def get_color(color):
	'''
	get a color based on the given string
	'''
	switcher = {
		'red': 'FF0000',
		'green': '00FF00',
		'blue': '0000FF',
		'cyan': '00FFFF',
		'magenta': 'FF00FF',
		'yellow': 'FFFF00'
	}

	return switcher[color]


