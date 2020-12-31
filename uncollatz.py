'''
Attempts to find integers with very low ratios by reversing the half-or-triple-plus-one procedure.
I have realized that this method is flawed, as the paths that are best often look bad initially (and looking far enough ahead is prohibitively time-consuming).
'''

import itertools

START_RANGE = [2, 5, 7, 9, 11, 13]
END_LIMIT = 10 ** 7
LOOK_AHEAD_DISTANCE = 12
# False represents n * 2; True represents (n - 1) / 3.
POSSIBLE_PATHS = list(itertools.product([False, True], repeat=LOOK_AHEAD_DISTANCE))

def main():
	for i in START_RANGE:
		numberPath = [i]
		while numberPath[-1] < END_LIMIT:
			bestPath = min(POSSIBLE_PATHS, key=lambda path: ratePath(numberPath[-1], path))
			if bestPath[0]:
				numberPath.append(int((numberPath[-1] - 1) / 3))
			else:
				numberPath.append(numberPath[-1] * 2)
		print(f'Found a path of length {len(numberPath)}: {" → ".join(str(a) for a in numberPath)}')

def ratePath(n, path):
	'''Takes a tuple of booleans that describe a path, and assigns a rating to the path. *Lower rates are better.* The rating of a valid path is the number that would result from taking that path. The rating of an invalid path is infinity.'''
	for option in path:
		minus1Divide3 = (n - 1) / 3
		if option:
			if minus1Divide3.is_integer() and minus1Divide3 % 2 == 1 and minus1Divide3 > 1:
				n = int(minus1Divide3)
			else:
				return float('inf')
		else:
			n <<= 1
	return n

if __name__ == '__main__':
	main()
