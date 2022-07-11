def my_input():
    n = input("Enter a number: ")
    return n
    
def find_lowest_and_smallest(n, l, s):
        try:
            n  = int(n)
            if l is None or n > l:
                l = n
            elif s is None or n < s:
                s = n
        except:
            print("Invalid input")
        return l, s

def output(l, s):
    print("Maximum is", l)
    print("Maximum is", s)

def main():
    largest = None
    smallest = None
    while True:
        num = my_input()
        if num == "done":
            break
        largest, smallest = find_lowest_and_smallest(num, largest, smallest)
    
    output(largest, smallest)

if __name__ == "__main__":
    main()
