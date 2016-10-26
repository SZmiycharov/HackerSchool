import datetime
now = datetime.datetime.now()

j = 0

timesWhenArrowsCollide = []

for i in range(0, 25):
	if j == 60:
		j = 0
	if j/10 == 0:
		if i/10 == 0:
			if i == now.hour:
				print "Time when arrows point same in current hour: 0{}:0{}".format(i, j)
		else:
			if i == now.hour:
				print "Time when arrows point same in current hour: {}:0{}".format(i, j)
	else:
		if i/10 == 0:
			if i == now.hour:
				print "Time when arrows point same in current hour: 0{}:{}".format(i, j)
		else:
			if i == now.hour:
				print "Time when arrows point same in current hour: {}:{}".format(i, j)
	j += 5 

