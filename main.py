n = 1  # Initial denominator (base actually)
term = 1 / (n ** 2)  # The single term
result = 0  # Sum up every term
while term >= 0.00000000001:  # Create a loop with condition
    result += term  # Add the term to the result
    n += 1  # Increase n by 1
    term = 1 / (n ** 2)  # Calculate new term

print(result)  # Output the final result after loop stopped
quit()
