import time


runs = 1


def main():
    number = 2
    index = 1

    while index < 10001:
        number += 1

        for divisor in range(2, number):
            if number % divisor == 0:
                break
        else:
            index += 1
        
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
