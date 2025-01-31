def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    try:
        score = float(input("Enter score:"))

        if score > 1.0:
            grade = 'Bad score'
        elif score >= 0.9 and score <= 1.0:
            grade = 'A'
        elif score >= 0.8 and score < 0.9:
            grade = 'B'
        elif score >= 0.7 and score < 0.8:
            grade = 'C'
        elif score >= 0.6 and score < 0.7:
            grade = 'D'
        elif score >= 0 and score < 0.6:
            grade = 'F'
        else:
            grade = 'Bad score'
    except:
        grade = 'Bad score'

    print(grade)

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
