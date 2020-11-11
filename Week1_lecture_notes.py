tape = [0, 0, 1, 1, 1, 0, 0, 0]

def display_tape():#def a function function's name. 此时run 会出现EOF 意思是End Of File
    pass#add pass, now function definition is acceptable

#How can we draw horizontal line
print('this is text')
print('this is \'text\'')#backslash后面加要打印的符号
print('-' * (2 * len(tape) + 1))#有17个
#we want to draw this at the beginning and at the end
#we don want to repeat the text, so we need to define a function
def draw_horizontal_line():
    print('-' * (2 * len(tape) + 1))#now the function has been defined

def draw_tape():
    draw_horizontal_line()#   the top boundary of the tape fragment.
    print('|' + '|'.join(str(e) for e in tape) + '|', sep='')#   also drawing vertical line segments as cell boundaries.
    # sep''separater = empty string (for the string without space)
    draw_horizontal_line()#   the bottom boundary of the tape fragment.

print(draw_tape())

print([str(e) for e in tape])#for element in tape, I give e as a string version

#glues  粘合
print('|'.join(['0', '0', '1', '1', '1', '0', '0', '0']))#join all string in this list together by using '',join is only use for string

#concatenate 连接
print('Hi ' + 'there')

print('|' + '|'.join(['0', '0', '1', '1', '1', '0', '0', '0']) + '|')

E = (str(e) for e in tape)

print(next(E))
print(next(E))
print(next(E))

#读文件
with open('division_by_2.txt') as TM_program:#use TM_program to process contents of 'division_by_2', this command should contain at least 1 file.
    print(TM_program.readlines())#用readline()读出每一行，适用于内容小的文件

with open('division_by_2.txt') as TM_program:
    print(TM_program.readline())#读出第一行 or we can use # next(TM_program) 下面一行也是一样
        print(TM_program.readline())#读出第二行
#上面两个with 打印出来每一行都是'内容\n'的样子

#现在要把 '。。。\n' 去掉read the lines one by one
with open('division_by_2.txt') as TM_program:
    for line in TM_program:
        print(line)#就可以将每一行都答应出来而不会有'。。。\n'

#end=''意思是不要换行
print('a', end='')
print('b', end='')
print('c')
#结果是abc

#.startwith() #test whether the particular string start with '...'
print('A string'.startswith('A'))
#结果是：True

#now with the loop i want to check if my line is start with #, if so, it will be print out
with open('division_by_2.txt') as TM_program:
    for line in TM_program:
        if line.startswith('#') and not line.isspace()):# use if not line.startswith('#'): to exclude this line开始有#,and 为空的line都不打印出来
            print(line, end='')#就可以将每一行都答应出来而不会有'。。。\n'

#判断字符是否为空白符
print(' '.isspace())
#结果是：True

with open('division_by_2.txt') as TM_program:
    for line in TM_program:
        if line.startswith('#') or line.isspace()):
            continue#means go back to the loop and work next line, if this statement is true. if not,then don't proceed further
        print(line, end='')

#how to extract strings: use split()
E = 'aXaaAaaaX'.split('a')
print(E)
#结果是：['', 'X', '', 'A', '', '', 'X']

E = 'aXaaAaaaX'.split('aa')
print(E)
#结果是：['aX', 'A', 'aX']

with open('division_by_2.txt') as TM_program:
    for line in TM_program:
        if line.startswith('#') or line.isspace()):
            continue
        print(line.split())
#结果，【'del1', '1', 'del2',...】每个元素用逗号隔开，且里面都是'', isolate the content

#dictionary
D = {'one':1, 'two':2, 'three':3}
print(D['one'])
#结果：1

A = {'a':1}
A['b'] = 2
print(A)
#结果：{'a': 1, 'b': 2}

L = [10, 11, 12]
L[1] = 100
print(L)#结果：[10, 100, 12]
L.append(40)
print(L)#结果：[10, 100, 12, 40]
L.remove(10)
print(L)#结果：[100, 12, 40]

()#this is a tuple
[]# is list

# we cannot append tuple
T = 1, 2, 3
T.append(4)
#this will give an error result

with open('division_by_2.txt') as TM_program:
    for line in TM_program:
        if line.startswith('#') or line.isspace()):
            continue
        instruction = line.split()
        TM_program[instruction[0], instruction[1]] = \
            instruction[2], instruction[3], instruction[4]
    print(TM_program)


(x, y, z) = [10, 11, 12]
print(x)
print(y)
print(z)
#结果
10
11
12

L = 'del1 1 del2 0 R'.split()
print(L)#结果：['del1', '1', 'del2', '0', 'R']
[state, symbol, new_state, new_symbol, direction] = L
print(state)#结果：del1

TM_program = {}
with open('division_by_2.txt') as TM_program_file:
    for line in TM_program_file:
        if line.startswith('#') or line.isspace():
            continue
        state, symbol, new_state, new_symbol, direction = line.split()
        TM_program[state, symbol] = new_state, new_symbol, direction
print(TM_program)

#结果
{('del1', '1'): ('del2', '0', 'R'),
('del2', '1'): ('mov1R', '0', 'R'),
('mov1R', '1'): ('mov1R', '1', 'R'),
('mov1R', '0'): ('mov2R', '0', 'R'),
('mov2R', '1'): ('mov2R', '1', 'R'),
('mov2R', '0'): ('mov1L', '1', 'L'),
('mov1L', '1'): ('mov1L', '1', 'L'),
('mov1L', '0'): ('mov2L', '0', 'L'),
('mov2L', '1'): ('mov2L', '1', 'L'),
('mov2L', '0'): ('del1', '0', 'R'),
('del1', '0'): ('end', '0', 'R'),
('del2', '0'): ('end', '0', 'R')}

int(32)#get integer 32
str(32)#get string 32

TM_program = {}
with open('division_by_2.txt') as TM_program_file:
    for line in TM_program_file:
        if line.startswith('#') or line.isspace():
            continue
        state, symbol, new_state, new_symbol, direction = line.split()
        TM_program[state, int(symbol)] = \
            new_state, int(new_symbol), direction
print(TM_program)

结果
{('del1', 1): ('del2', 0, 'R'),
('del2', 1): ('mov1R', 0, 'R'),
('mov1R', 1): ('mov1R', 1, 'R'),
('mov1R', 0): ('mov2R', 0, 'R'),
('mov2R', 1): ('mov2R', 1, 'R'),
('mov2R', 0): ('mov1L', 1, 'L'),
('mov1L', 1): ('mov1L', 1, 'L'),
('mov1L', 0): ('mov2L', 0, 'L'),
('mov2L', 1): ('mov2L', 1, 'L'),
('mov2L', 0): ('del1', 0, 'R'),
('del1', 0): ('end', 0, 'R'),
('del2', 0): ('end', 0, 'R')}

current_state = del_1
current_position = tape.index(1)#查看1现在哪个位置出现
print(current_position)
#结果是：2
def display_current_configuration():
    draw_tape()
    print(' ' * current_position, current_state)
print(display_current_configuration)
#结果：
-------------
|0|0|1|1|1|0|
-------------
     del_1

# I can ask, do I have key like (current_state, current_bit) in program.keys?
print((current_state, current_bit) in program.keys())
#结果True
print(program[current_state, current_bit])
#结果（'del2', 0, 'R'）, it will shows its corresponding value

