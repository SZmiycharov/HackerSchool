import getopt
import sys
import os

try:
	opts, args = getopt.getopt(sys.argv[1:],"hp:",["ipaddress="])		
except getopt.GetoptError:
	print 'jsonCreator.py -ip <ipaddress>'
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print 'jsonCreator.py -ip <ipaddress>'
		sys.exit(0)
    	elif opt in ("-p", "--ipaddress"):
		ip = arg
	else:
		print 'jsonCreator.py -ip <ipaddress>'
		sys.exit(0)

print '\n************************************'
#mypc:192.168.0.1,mylaptop:192.168.0.2
iplist = ip.split(',')
for x in iplist:
	host = x.split(':')[0]
	currentip = x.split(':')[1]
	resultofping = os.popen("ping -c 5 %s"%(currentip)).read()
	lostpackages = resultofping.split('\n')[-3].split(',')[-2].split('%')[0].split(' ')[1]
	print '''{
  "data": [
    {
      "{#NAME}": "%s",
      "{#IPADDRESS}": "%s",
      "{#VALUE}" : "%s"
    }
  ]
}'''%(host,currentip,lostpackages)








