j = 0

for i in range(12, 25):
	if j == 60:
		j = 0
	if j/10 == 0:
		print "Time when arrows point same: {}:0{}".format(i, j)
	else:
		print "Time when arrows point same: {}:{}".format(i, j)
	j += 5 
