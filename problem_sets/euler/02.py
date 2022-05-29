

# PDL:
# Set the current to be 2.
# Set the previous to be 1.
# add the previous to the current to get the next number in the sequence.
# subtract the previous from the current to get the new previous number.
# add the number to the sum if it is even.

def slidingFibbonaci(ceiling):
	prev = 1
	current = 1
	sum = 0
	while (current <= ceiling):
		current = prev + current
		prev = current - prev
		if current % 2 == 0:
			sum = sum + current
	return sum

def main():
	solution = slidingFibbonaci(4000000)
	print solution

main()