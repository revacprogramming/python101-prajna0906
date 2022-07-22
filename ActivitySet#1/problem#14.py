# Using Web Services
# https://www.py4e.com/lessons/servces



import re
def my_input():
    fh = open("../dataset/reg_ex.txt")
    return fh

def find_sum(fh):
    sum = 0

    for line in fh:
        numbers = re.findall('[0-9]+', line)
        if len(numbers) > 0:
            for number in numbers:
                sum += int(number)

    return sum

def output(sum):
    print(sum)

def main():
    fh = my_input()
    sum = find_sum(fh)
    output(sum)

if __name__ == "__main__":
    main()
