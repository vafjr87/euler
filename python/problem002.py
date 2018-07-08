import time


runs = 1000


def main():
    term_first = 1
    term_second = 2

    for run in range(10):
        fibonacci = term_first + term_second
        print(fibonacci)

        term_first = term_second
        term_second = fibonacci



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