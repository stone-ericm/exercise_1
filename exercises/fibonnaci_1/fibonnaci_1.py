def fibonacci(x):
    a = 0
    b = 1
    i = 0
    while i < x:
        y = a + b
        a , b = b, y
        if y % 2 == 0:
            print y
            i += 1

def main():
    if __name__ == "__main__":
        fibonacci(10)

main()