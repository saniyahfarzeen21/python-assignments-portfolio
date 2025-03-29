def arctan(x):
    # Step 1: Check if x is within the interval (0, 1]
    if x < 0 or x > 1:
        return "Error!"

    # Step 2: Initialize variables for approximation, error bound, and loop counter
    approx = 0
    error = float('inf')
    n = 0

    # Step 3: Loop until the error bound is less than or equal to 0.0001
    while error > 0.0001:
        # Calculate the current term in the series
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
        approx += term

        # Update the error bound based on the next term (+3 come from using next term, n+1)
        error = (x ** (2 * n + 3)) / (2 * n + 3)

        # Increment the counter for the next term
        n += 1

    # Step 4: Return the approximation, n, and the final error bound
    return approx, n, error

# Test the funtion with the given inputs
test = [-1, 0, 0.25, 0.5, 0.75,1]
for x in test:
    result = arctan(x)
    print(f"arctan(x) = {result}")