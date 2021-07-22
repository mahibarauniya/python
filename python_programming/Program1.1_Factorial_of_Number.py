def factorial(num):
    if num < 0:
        result_num = 0
    elif num == 0 or num == 1:
        result_num = 1
    else:
        fact = 1
        while (num > 1):
            fact *= num
            num -= 1
        result_num = fact
    return result_num

def main():
    num = 5
    result = factorial(num)
    print ("Number: {} and it's factorial is: {} .........".format(num, result))

if __name__ == "__main__":
    main()