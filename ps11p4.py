def compute_averages(scores, handicap):
    avg_score = sum(scores) / len(scores)
    avg_score_with_handicap = avg_score + handicap
    return avg_score, avg_score_with_handicap
def main():
    last_name = input("Enter the bowler's last name: ")
    scores = [int(input(f"Enter score for game {i + 1}: ")) for i in range(3)]
    handicap = int(input("Enter the bowler's handicap: "))
    avg_score, avg_score_with_handicap = compute_averages(scores, handicap)
    print(f"\nBowler: {last_name}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Average Score with Handicap: {avg_score_with_handicap:.2f}")
if __name__ == "__main__":
    main()