

def getMultiplesBelowLimit(multiplier, ceiling):
	results = set()
	result = 1
	count = 0
	while result < ceiling - multiplier: 
		count = count + 1
		result = multiplier * count
		results.add(result)
	return results

def main():
	threes = getMultiplesBelowLimit(3, 1000)
	fives = getMultiplesBelowLimit(5, 1000)

	multiples = threes | fives
	print(multiples)


	sum = 0
	for multiple in multiples:
		sum = sum + multiple

	print(sum)

main()
