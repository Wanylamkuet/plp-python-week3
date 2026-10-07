count = 1
total = 0

# BUG: Missing colon (:) at the end of the while loop header causing a SyntaxError. Fixed by adding a colon.
# BUG: Off-by-one condition (count < 5 stops before adding 5, yielding 10 instead of 15). Fixed by changing condition to count <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: TypeError caused by concatenating a string with an integer (total). Fixed using an f-string (or str(total)).
print(f"Sum of 1 to 5 is: {total}")
