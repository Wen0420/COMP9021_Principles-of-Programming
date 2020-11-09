# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left
#   corner,  so the largest region consisting of connected cells all
#   filled with 1s or all filled with 0s, depending on the value stored
#   in the top left corner;
# - the size of the largest area with a checkers pattern.


from random import seed, randint
import sys


dim = 10

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))

try:
    arg_for_seed, density = (int(x) for x in 
                    input('Enter two positive integers: ').split()
                            )
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[int(randint(0, density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE




def check_Qi_one(Zi):
    if Zi in current_status:
        pass
    else:
        # check这个是不是上、下、左、右一样
        y, x = Zi
        current_status.add(Zi)
        UpDownLeftRight = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for dulr_y, dulr_x in UpDownLeftRight:
            # 向不同方向走就会有出界的问题，#再判断当前的值是不是和它一样
            if 0 <= y + dulr_y < dim and 0 <= x + dulr_x < dim and grid[y + dulr_y][x + dulr_x] == grid[0][0]:
                # 如果等于就继续check这个点
                check_Qi_one((y + dulr_y, x + dulr_x))
                # 再判断当前的值是不是和它一样

# 接下来checkThe size of the largest homogenous region from the top left corner is 3.
current_status = set()  # 这里调用的是一个方法，用的是全局变量
check_Qi_one((0, 0))
print(f"The size of the largest homogenous region from the top left corner is {len(current_status)}.")

#第二问 只要不同它就走如果当前是1就check周围是0，反之亦然
#第二问 只要不同它就走如果当前是1就check周围是0，反之亦然
def not_same_point(y,x):
    UpDownLeftRight = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    # 不check same 把值return一个list
    results = []
    for udlrY, udlrX in UpDownLeftRight:
        # 向不同方向走就会有出界的问题，#再判断当前的值是不是和它一样
        if 0 <= y + udlrY < dim and 0 <= x + udlrX < dim and grid[y + udlrY][x + udlrX] != grid[y][x]:
            results.append((y + udlrY, x + udlrX))
    return results

def for_not_same(Zi):
    y,x = Zi
    if Zi not in current_status:
        current_status.add((y, x))
        #如果results 有内容
        for y, x in not_same_point(y, x):
            for_not_same((y, x))
current_status = set()  # 这里调用的是一个方法，用的是全局变量
Vpoint = set()
checker_structure = []
#取最大, 只check没有访问过的点，记录从当前点出发，所有记录的点
for y in range(dim):
    if y not in Vpoint:
        current_status.clear()
    for x in range(dim):
        #点没有被访问过
        if x not in Vpoint:
            current_status.clear()
            #visited 是每一次的, 取最大
            for_not_same((y,x))
            checker_structure.append(len(current_status))
            Vpoint.update(current_status)
print(f"The size of the largest area with a checkers structure is {max(checker_structure)}.")
