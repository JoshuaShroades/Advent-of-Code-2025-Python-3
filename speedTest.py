import time
import Day01.part1 as A01
import Day01.part2 as A02
import Day02.part1 as B01
import Day02.part2 as B02

def speedTest(func):
	times = []
	for _ in range(100):
		startTime = time.time()

		value = func.main()

		times.append(time.time() - startTime)

	print("\n" + func.__name__ + ": " + str(value))
	print("Average time (ms): " + str(round(sum(times) / len(times) * 1000, 2)))

# speedTest(A01)
speedTest(A02)
# speedTest(B01)
# speedTest(B02)
