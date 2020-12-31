'''
Collatz Dictionary
https://youtu.be/PrWXtgHCxNk
I tried to save the number of steps required for numbers previously explored, but this filled up my RAM. So now I'm only saving the number of steps for numbers in a certain range.
'''
import math
import time

# Must be even.
KNOWN_STEPS_LEN = 10 ** 6
# n, steps required, and the ratio
SLEEP_TIME = 3 * 10 ** -3
knownSteps = {2: 1}

def main():
	global knownSteps

	bestFound = (2, 1, 1)
	# Find the steps required for low numbers. When we are decreasing a large number and get it small enough, we can just look up the answer.
	for i in range(3, KNOWN_STEPS_LEN):
		knownSteps[i] = countSteps(i)
	startTime = int(time.time())
	i = KNOWN_STEPS_LEN + 1
	while True:
		steps = countSteps(i)
		if steps > bestFound[1]:
			ratio = math.log2(i) / steps
			if ratio < bestFound[2]:
				bestFound = (i, steps, ratio)
				print(f'{int(time.time()) - startTime}: {bestFound[0]} takes {bestFound[1]} steps and has a ratio of {bestFound[2]:.5}.')
		if i % 1000 == 1:
			time.sleep(SLEEP_TIME)
			if i % 1000000 == 1:
				print(f'{int(time.time()) - startTime}: Checking {i}...')
		i += 2

def countSteps(n):
	steps = 0
	while n not in knownSteps:
		if n % 2 == 0:
			n >>= 1
		else:
			n = 3 * n + 1
		steps += 1
	return knownSteps[n] + steps

if __name__ == '__main__':
	main()
