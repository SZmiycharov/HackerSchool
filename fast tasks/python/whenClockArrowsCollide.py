import datetime
import math

now = datetime.datetime.now()

j = 0

goingToCollide = False

for i in range(0, 24):
	n = 720 * i / 11
	n = round(n*100) / 100;
	hour = math.floor(n/60)

	minutes = math.floor(n%60)


	if hour < 25:
		if len(str(int(minutes))) == 1:
			if len(str(int(hour))) == 1:
				print "Time when arrows point same in current hour: 0{}:0{}".format(int(hour), int(minutes))
				if hour == now.hour and now.minute <= minutes:
					print "Time when arrows point same in current hour: 0{}:0{}".format(int(hour), int(minutes))
					goingToCollide = True
					break
			else:
				print "Time when arrows point same in current hour: {}:0{}".format(int(hour), int(minutes))
				if hour == now.hour and now.minute <= minutes:
					print "Time when arrows point same in current hour: {}:0{}".format(int(hour), int(minutes))
					goingToCollide = True
					break
		else:
			if len(str(int(hour))) == 1:
				print "Time when arrows point same in current hour: 0{}:{}".format(int(hour), int(minutes))
				if hour == now.hour and now.minute <= minutes:
					print "Time when arrows point same in current hour: 0{}:{}".format(int(hour), int(minutes))
					goingToCollide = True
					break
			else:
				print "Time when arrows point same in current hour: {}:{}".format(int(hour), int(minutes))
				if hour == now.hour and now.minute <= minutes:
					print "Time when arrows point same in current hour: {}:{}".format(int(hour), int(minutes))
					goingToCollide = True
					break

if not goingToCollide:
	print "Sorry - arrows won't collide again this hour!"