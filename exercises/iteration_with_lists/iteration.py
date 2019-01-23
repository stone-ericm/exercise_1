import sys

def my_loop(x):
    i = 1
    while i < x:
        print i
        i += 1


def my_reverse_loop(x):
    i = x-1
    while i > 0:
        print i
        i -= 1

def main():
    if __name__ == "__main__":
        try:
            sys.argv[2];
        except IndexError:
            print("Please include the function to be run followed by the number to use.")
            exit()
        function = str(sys.argv[1])
        number = int(sys.argv[2])
        if function == "loop":
            my_loop(number)
        elif function == "rloop":
            my_reverse_loop(number)

            
main()
# print (my_loop(10))

