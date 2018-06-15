import time


runs = 10000


def main():
    multiples_sum = 0
    for x in range(3, 1000):
        if x % 3 == 0 or x % 5 == 0:
            multiples_sum += x

    return multiples_sum


if __name__ == "__main__":
    answer = 0
    total_time = 0

    for run in range(0, runs):
        start_time = time.time()
        answer = main()
        run_time = time.time() - start_time
        total_time += run_time

    print("answer  --- {} ---".format(answer))
    print("runtime --- {:.4f} ms ---".format((total_time * 1000) / runs))
