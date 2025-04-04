# Name: Lillian McGowan
# Program: Chapter 5 – Loops
# Description: This program takes three test scores as input, checks that they’re between 0 and 100,
# drops the lowest score, calculates the average of the top two scores,
# and gives a letter grade like A, B, C, D, or F based on the average.

A_GRADE = 90
B_GRADE = 80
C_GRADE = 70
D_GRADE = 60
NUM_TESTS = 3

print("Test Grade Calculator")

# Ask the user to enter 3 test scores and make sure each one is valid
testScores = []
for i in range(NUM_TESTS):
    while True:
        try:
            score = int(input(f"Enter test score {i+1}: "))
            if 0 <= score <= 100:
                testScores.append(score)
                break
            else:
                print("Oops! Score must be between 0 and 100.")
        except ValueError:
            print("That wasn’t a number. Please enter a whole number like 85.")

# Find and drop the lowest score
lowScore = min(testScores)
testScores.remove(lowScore)

# Average the other two scores
avgScore = sum(testScores) / 2

# Give a letter grade based on the average
if avgScore >= A_GRADE:
    letterGrade = 'A'
elif avgScore >= B_GRADE:
    letterGrade = 'B'
elif avgScore >= C_GRADE:
    letterGrade = 'C'
elif avgScore >= D_GRADE:
    letterGrade = 'D'
else:
    letterGrade = 'F'

# Show the final results
print(f"Lowest test score dropped: {lowScore}")
print(f"Average test score: {avgScore:.2f}")
print(f"Letter grade: {letterGrade}")
