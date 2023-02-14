import sys

# def String2Dic():
# def eliminate():

def main():
    # convert string to dictionary
    f = open("data/input.txt", "r")
    words = []
    for l in f:
        words = l.split(" ")
    print(words)
    f.close()

if __name__ == '__main__':
    main()
