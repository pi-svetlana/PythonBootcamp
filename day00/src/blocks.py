import sys

if len(sys.argv) == 2 and sys.argv[1].isnumeric():
    num = int(sys.argv[1])
    my_list = []
    for i in range(num):
        my_list.append(input())
    for x in my_list:
        if len(x) == 32 and x.startswith('00000') and x[5] != '0':
            print(x)
else:
    print("Ошибка: необходимо ввести один числовой аргумент")


# cat tests/ten_lines.txt | python3 blocks.py 10
# cat tests/ten_lines.txt | python3 blocks.py 5
