import datetime
import math

now = datetime.datetime.now()

goingToCollide = False

for i in range(0, 23):
	n = 720 * i / 11

	hour = math.floor(n/60)
	minutes = math.floor(n%60)

	print "Time when arrows collide: %02d:%02d" % (int(hour), int(minutes))
	if hour == now.hour and now.minute <= minutes:
		goingToCollide = True
		hourToCollide = hour
		minutesToCollide = minutes
		break

print "\n"
if not goingToCollide:
	print "Sorry - arrows won't collide (again) this hour!"
else:
	print "Time when arrows point same in current hour: %02d:%02d" % (int(hourToCollide), int(minutesToCollide))