# PLP Python Week 3 Assignment: Conditions and Loops

## Files Overview
* `grade_reporter.py`: Calculates letter grades, total pass/fail counts, and the average score from a list of learner scores using `for` loops and conditional statements.
* `bug_hunt.py`: A debugged script that calculates the sum of numbers from 1 to 5 using a `while` loop with explanatory comments for each bug fixed.

## Debugging Reflection
The off-by-one logic error (`count < 5` instead of `count <= 5`) was the hardest bug to find because Python executed the code without throwing any error messages or crashing. I knew something was wrong because the output printed `10` instead of the expected correct sum of `15`. To spot it, I traced the `while` loop execution step-by-step and realized the loop stopped before `count` could equal 5.