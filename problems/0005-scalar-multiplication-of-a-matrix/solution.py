def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	return [[a * scalar for a in line] for line in matrix]