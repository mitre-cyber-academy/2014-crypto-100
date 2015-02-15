import random
import string

alpha = "abcdefghijklmnopqrstuvwxyz1234567890"

fileOut = open("file3.txt", "w")

for i in range(1, 40001):

	'''if i == 36040:
		fileOut.write("c22b5f9178342609428d6f51b2c5af4c0bde6a42")
		i = i + 40   USED TO PLACE KEY INTO RANDOM FILE'''

	if i % 39 == 0:
		fileOut.write(random.choice('ghijklmnopqrstuvwxyz<>!?,.;:-+_'))
	else:
		fileOut.write(random.choice(alpha))