import datetime
import math

now = datetime.datetime.now()

goingToCollide = False

for i in range(0, 24):
	n = 720 * i / 11
	n = round(n*100) / 100;
	hour = math.floor(n/60)

	minutes = math.floor(n%60)

	if hour < 25:
		if hour == now.hour and now.minute <= minutes:
			print "Time when arrows point same in current hour: %02d:%02d" % (int(hour), int(minutes))
			goingToCollide = True
			break

if not goingToCollide:
	print "Sorry - arrows won't collide again this hour!"