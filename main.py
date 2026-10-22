def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def get_pass_status(marks, passing_marks=40):
    """Check whether a student has passed."""
    return marks >= passing_marks


def main():
    marks = [78, 65, 32, 89, 45]

    average = calculate_average(marks)

    print("Student Marks Report")
    print("--------------------")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")

    for index, score in enumerate(marks, start=1):
        status = "Pass" if get_pass_status(score) else "Fail"
        print(f"Student {index}: {score} - {status}")


if __name__ == "__main__":
    main()