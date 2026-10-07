scores = [72, 45, 90, 61, 38]

# Initialize tracking variables
passed_count = 0
failed_count = 0
total_score = 0

# Loop through each score in the list
for score in scores:
    total_score += score  # Add to running total
    
    # Determine the grade and count pass/fail
    if score >= 80:
        grade = "A"
        passed_count += 1
    elif score >= 70:
        grade = "B"
        passed_count += 1
    elif score >= 50:
        grade = "C"
        passed_count += 1
    else:
        grade = "F"
        failed_count += 1
        
    print(f"Score: {score} - Grade: {grade}")

# Calculate average
average = total_score / len(scores)

# Print summary statistics
print("-" * 20)
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average score: {round(average, 1)}")
