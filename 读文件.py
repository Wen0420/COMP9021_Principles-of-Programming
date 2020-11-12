file = open('some_instructions.txt', mode='r')

#只读不加
file = open('some_instructions.txt')
file.close()

with open('some_instructions.txt') as open_file:
    #怎么读里面的每一行数据

    #一次性读出所有的行
    #lines = open_file.readlines()
    #一行一行的读
    for line in open_file:
        if line.startswith("Draw a line of "):
            values = line.split()
            number1 = values[4]
            symbol = values[5]
            number2 = values[7]
            print(int(number2) * ' ' + int(number1) * symbol)
#if 之后是边读边打印

    #也可以最后输出
    line = []
    for line in open_file:
        if line.startswith("Draw a line of "):
            values = line.split()
            number1 = values[4]
            symbol = values[5]
            number2 = values[7]
            lines.append(int(number2) * ' ' + int(number1) * symbol)

    #把每一行都打印出来
    lines = []
    for line in open_file:
        if line.startswith("Draw a line of "):
            values = line.split()
            number1 = values[4]
            symbol = values[5]
            number2 = values[7]
            lines.append(int(number2) * ' ' + int(number1) * symbol)


    #换行\n
    lines = []
    for line in open_file:
        if line.startswith("Draw a line of "):
            values = line.split()
            lines.append(int(values[4]) * ' ' + int(values[7]) * values[5])

    print("\n".join(lines))



