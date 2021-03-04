# def main():
#     name = input("input your full name: ")
#     file_write = open("write.txt", 'a') #w: write only; r: read only; a: append
#     file_write.write(name)
#
# main()

# def main():
#     file_test = open("write.txt", 'r') #w: write only; r: read only; a: append
#     line = file_test.readline()
#     while line != '':
#         print(line, end='')
#         line = file_test.readline()
#     file_test.close()
#
# main()

def main():
    try:
        file_write = open("write.txt", 'r')
        line = file_write.readline()
        count = 0
        total = 0
        while line != '':
            total += int(line)
            count += 1
            line = file_write.readline()
        file_write.close()
        average = total / count
        print(average)

    except Exception as er:
        print(er)
main()