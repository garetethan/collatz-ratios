// Python seems to be too slow, so let's try it in C.

#include <math.h>
#include <stdio.h>
#include <time.h>

#define KNOWN_STEPS_LEN 100000000
const unsigned long SLEEP_NS = 400000;
const struct timespec SLEEP_STRUCT = {0, SLEEP_NS};
const unsigned long START = 1100000001;
unsigned int bestSteps = 0;
// The worst possible ratio (shared by all powers of 2).
float bestRatio = 1.0;

void hotpol (unsigned long* n);
void compareToBest (unsigned long* n, unsigned int* steps);

int main () {
	time_t startTime = time(NULL);
	static unsigned int knownSteps[KNOWN_STEPS_LEN + 1];
	// Fill knownSteps.
	knownSteps[1] = 0;
	for (unsigned long i = 2; i < KNOWN_STEPS_LEN; i++) {
		unsigned long j = i;
		for (knownSteps[i] = 0; j >= i; knownSteps[i]++) {
			hotpol(&j);
		}
		knownSteps[i] += knownSteps[j];
		compareToBest(&i, &knownSteps[i]);
	}

	// Find low ratios.
	// Intentional infinite loop.
	for (unsigned long k = START; 1; k += 2) {
		unsigned int steps = 0;
		unsigned long m = k;
		for (; m >= KNOWN_STEPS_LEN; steps++) {
			hotpol(&m);
		}
		steps += knownSteps[m];
		compareToBest(&k, &steps);
		if (k % 1000 == 1) {
			nanosleep(&SLEEP_STRUCT, NULL);
			// Print progress every 10 million.
			if (k % 10000000 == 1) {
				printf("%u: Checked %u...\n", time(NULL) - startTime, k);
			}
		}
	}
}

void hotpol (unsigned long* n) {
	/* Half or triple plus one for longs. */
	if (*n % 2 == 0) {
		*n >>= 1;
	}
	else {
		*n = *n * 3 + 1;
	}
}

void compareToBest (unsigned long* n, unsigned int* steps) {
	if (*steps > bestSteps) {
		float ratio = log2f((float) *n) / *steps;
		if (ratio < bestRatio) {
			printf("%lu takes %u steps and has a ratio of %.5f\n", *n, *steps, ratio);
			bestSteps = *steps;
			bestRatio = ratio;
		}
	}
}
