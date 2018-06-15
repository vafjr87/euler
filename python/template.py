import time


def main():
    pass


if __name__ == "__main__":
    start_time = time.time()
    main()
    total_time = (time.time() - start_time) * 1000
    print("runtime --- {:.4f} ms ---".format(total_time))
