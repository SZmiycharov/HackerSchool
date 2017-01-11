import math

def numberIsSpecial(number):
  return ('0' in str(number)) and ('4' in str(number)) and ('9' in str(number)) and ('1' not in str(number)) and ('2' not in str(number)) and ('3' not in str(number)) and ('5' not in str(number)) and ('6' not in str(number)) and ('7' not in str(number)) and ('8' not in str(number))


while True:
  try:
     line = raw_input("Enter member < positive number>0 >: ")
     member = int(line.split(' ')[0])
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(member < 1):
         print("Incorrect values!")
         continue
     else:
        break

squaredNumbers = [x*x for x in range(1000000) if numberIsSpecial(x*x)]
iteration = 1

for i in squaredNumbers:
  if iteration == member:
    print int(math.sqrt(i))
  iteration += 1

