import random
import sys, getopt

def some_func():
	maxvalue = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hm:",["max="])		
	except getopt.GetoptError:
	    	print 'webserver1.py -m <maxvalue>'
	    	sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'webserver1.py -m <maxvalue>'
			sys.exit()
		elif opt in ("-m", "--max"):
			maxvalue = arg
		

	try:
		maxvalue = int(maxvalue)
	except ValueError:
		string = '''<!DOCTYPE html>
	<html>
	<body>
	<p>MAX was not a number!</p>
	</body>
	</html>'''
		print string
	else:
		a = random.randrange(0,maxvalue)
		b = random.randrange(0,maxvalue)
		string = '''<!DOCTYPE html>
	<html>
	<body>

	<h2 style="color:green;">%s</h2>
	<h2 style="color:red;">%s</h2>

	</body>
	</html>'''%(a,b)
		print string

if __name__ == "__main__":
	some_func()
