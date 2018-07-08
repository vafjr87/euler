import time


runs = 1000

def is_palindrome(palindrome):
    if len(str(palindrome)) % 2 != 0:
        return False

    last = len(str(palindrome))-1

    for run in range(last):
        if str(palindrome)[run] != str(palindrome)[last]:
             return False
        last -= 1

    return True

def main():
    palindrome = 0
    term_first = 999

    while term_first >= 100:
        term_second = 999

        while term_second >= term_first:
            product = term_first * term_second
            if is_palindrome(product):
                if product > palindrome:
                    palindrome = product
            
            term_second -= 1

        term_first -= 1

    return palindrome


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
