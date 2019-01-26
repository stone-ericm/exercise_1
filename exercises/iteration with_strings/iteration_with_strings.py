def reverse_my_string(x):
    i = len(x)-1
    output = ""
    while i >= 0:
        output += x[i]
        i -= 1
    print output


def main():
    if __name__ == "__main__":
        reverse_my_string("Jeff")
main()