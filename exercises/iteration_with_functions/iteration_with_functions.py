given_list = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

def three_ms(x):
    if len(x)%2 == 0:
        median = x[(len(x)/2)-1]
    else:
        median = x[(len(x)/2)]
    print "Median = ", median
    mean = sum(x)/len(x)
    print "Mean = ", mean
    mode = max(set(x), key=x.count)
    print "Mode = ", mode



def main():
    if __name__ == "__main__":
        three_ms(given_list)
main()