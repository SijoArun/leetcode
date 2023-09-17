
# Read input from "inputPS10.txt"
with open("inputPS10.txt", "r") as f:
    lines = f.readlines()

# Extract denominations and purchase amount
denominations_line = None  # Initialize to None
purchase = None  # Initialize to None

for line in lines:
    if line.startswith("Denominations:"):
        denominations_line = line
    elif line.startswith("Purchase:"):
        purchase = int(line.strip().split()[1])

# Check if both lines were found
if denominations_line is not None and purchase is not None:
    denominations = list(map(int, denominations_line.strip().split()[1:]))

    # Initialize the dp table
    dp = [0] * (purchase + 1)
    dp[0] = 1

    # Calculate the number of combinations
    for denomination in denominations:
        for i in range(denomination, purchase + 1):
            dp[i] += dp[i - denomination]

    # Get the number of combinations for the purchase amount
    combinations = dp[purchase]

    # Write the result to "outputPS10.txt"
    with open("outputPS10.txt", "w") as f:
        f.write("Possible Combinations: {}\n".format(combinations))
else:
    print("Error: Denominations and/or Purchase line not found in input file.")




