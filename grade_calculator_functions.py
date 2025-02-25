def get_student_score():
    """
    Prompts the user to enter a student's score and validates the input.

    Returns:
        float: The validated student score.
    """
    while True:
        try:
            score = float(input("Enter the student's score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score):
    """
    Calculates the letter grade based on the student's score.

    Args:
        score (float): The student's score.

    Returns:
        str: The letter grade (A, B, C, D, or F).
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    """
    Main function to get the student's score, calculate the grade, and display the result.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"The student's grade is: {grade}")

if __name__ == "__main__":
    main()
