def recursive_nth_fibo(number):
    if number == 0:
        return number
    elif number == 1:
        return 1
    else:
        return (recursive_nth_fibo(number - 1) + recursive_nth_fibo(number - 2))



def main():
    print(recursive_nth_fibo(10))


if __name__ == "__main__":
    main()
