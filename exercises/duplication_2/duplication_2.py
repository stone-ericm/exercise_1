def duplication(x):
    i = 1
    output = [x[0],""]
    # print output
    while i < len(x):
        # if output:
        # print x[i]
        if output[0][len(output[0])-1] != x[i]:
            output[0] += x[i]
        else:
            output[1] += x[i]
        i +=1
    print output
            
def main():
    if __name__ == "__main__":
        duplication("aabbccddeded")

main()