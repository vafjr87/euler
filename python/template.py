import time




def main():
    return 0


if __name__ == "__main__":
    answer = 0
    total_time = 0

    start_time = time.time()
    answer = main()
    run_time = time.time() - start_time

    print("answer  --- {} ---".format(answer))
    print("runtime --- {:.4f} ms ---".format(run_time)
