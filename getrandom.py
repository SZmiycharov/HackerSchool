import random
import sys, getopt

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
		
maxvalue = int(maxvalue)

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
