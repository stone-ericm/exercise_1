def iterate(x):
    for each in x:
        if not isinstance(each, list):
            print each
        else:
            iterate(each)
        

def main():
    if __name__ == "__main__":
        iterate([1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]])

            
main()