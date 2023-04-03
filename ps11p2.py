def compute_total_and_average(score1, score2, score3):
    total_points = score1 + score2 + score3
    average_score = total_points / 3
    return total_points, average_score
def main():
    last_name = input("Enter the student's last name: ")
    score1 = float(input("Enter the first exam score: "))
    score2 = float(input("Enter the second exam score: "))
    score3 = float(input("Enter the third exam score: "))
    total_points, average_score = compute_total_and_average(score1, score2, score3)
    print(f"Student's last name: {last_name}")
    print(f"Total points: {total_points}")
    print(f"Average exam score: {average_score:.2f}")
if __name__ == "__main__":
    main()
