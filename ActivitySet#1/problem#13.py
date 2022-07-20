# Network Programming
# https://www.py4e.com/lessons/network



def my_input():
    name = input("Enter file:")
    if len(name) < 1:
        name = "../dataset/mbox-short.txt"
    fh = open(name)
    return fh

def find_hour_count(fh):
    hour_list = list()

    for line in fh:
        if line.startswith("From") and not line.startswith("From:"):
            words = line.split()
            time = words[5]
            hour = time[0:2]
                        
            hour_list.append(hour)


    hour_list.sort()

    hour_count = list()

    i = 0
    while i < len(hour_list):
        j = i
        count = 0
        while j < len(hour_list) and hour_list[i] == hour_list[j]:
            j += 1
        count = j - i
        hour_count.append((hour_list[i], count))
        
        i += count

    return hour_count;

def output(hour_count):
    for i, j in hour_count:
        print(i, j)

def main():
    fh = my_input()
    hour_count = find_hour_count(fh)
    output(hour_count)

if __name__ == "__main__":
    main()
