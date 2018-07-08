import time


runs = 1000


def main(number):
    divisor = 2

    while number != 1:
        if number % divisor == 0:
            number /= divisor
        else:
            divisor += 1

    return divisor
    

if __name__ == "__main__":
    answer = 0
    total_time = 0

    for run in range(0, runs):
        start_time = time.time()
        answer = main(600851475143)
        run_time = time.time() - start_time
        total_time += run_time

    print("answer  --- {} ---".format(answer))
    print("runtime --- {:.4f} ms ---".format((total_time * 1000) / runs))
