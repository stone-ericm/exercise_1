def fizzbuzz(x):
    i=1
    while i < x:
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if not output:
            output = i
        print output
        i += 1

def main():
    if __name__ == "__main__":
        fizzbuzz(20)
main()