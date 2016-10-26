import datetime
now = datetime.datetime.now()

j = 0

timesWhenArrowsCollide = []
goingToCollide = False

for i in range(0, 25):
	if j == 60:
		j = 0
	if j/10 == 0:
		if i/10 == 0:
			if i == now.hour and now.minute <= j:
				print "Time when arrows point same in current hour: 0{}:0{}".format(i, j)
				goingToCollide = True
				break
		else:
			if i == now.hour and now.minute <= j:
				print "Time when arrows point same in current hour: {}:0{}".format(i, j)
				goingToCollide = True
				break
	else:
		if i/10 == 0:
			if i == now.hour and now.minute <= j:
				print "Time when arrows point same in current hour: 0{}:{}".format(i, j)
				goingToCollide = True
				break
		else:
			if i == now.hour and now.minute <= j:
				print "Time when arrows point same in current hour: {}:{}".format(i, j)
				goingToCollide = True
				break
	j += 5 


if not goingToCollide:
	"Sorry - arrows won't collide again this hour!"