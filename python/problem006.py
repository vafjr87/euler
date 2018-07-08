import time


runs = 1


def main():
    sum_of_squares = 0
    square_of_sums = 0

    for number in range(1, 101):
        sum_of_squares += number * number
        square_of_sums += number
    else:
        square_of_sums *= square_of_sums
        return square_of_sums - sum_of_squares


if __name__ == "__main__":
    answer = 0
    total_time = 0

    for run in range(0, runs):
        start_time = time.time()
        answer = main()
        run_time = time.time() - start_time
        total_time += run_time

    print("answer  --- {} ---".format(answer))
    print("runtime --- {:.4f} ms ---".format((total_time * runs) / runs))
