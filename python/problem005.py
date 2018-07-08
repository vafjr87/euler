import time


runs = 1


def main():
    number = 1
    highest_divisor = 20

    while True:
        print(number)
        for divisor in reversed(range(1, highest_divisor+1)):
            if number % divisor != 0:
                number += 1
                break
        else:
            return number


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
