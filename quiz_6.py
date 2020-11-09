# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Randomly generates a grid with 0s and 1s, whose dimension is controlled
# by user input, as well as the density of 1s in the grid, and finds out,
# for given step_number >= 1 and step_size >= 2, the number of stairs of
# step_number many steps, with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest
# step sizes, and for a given step size, from stairs with the smallest number
# of steps to stairs with the largest number of stairs.


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0))
                              for j in range(len(grid))
                             )
             )

try:
    arg_for_seed, density, dim = (int(x) for x in 
                        input('Enter three positive integers: ').split()
                                 )
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE






#先生成这些点
#再check 这些点
#再check这些steps
#再check 每一个size
#把check的结果放到result 里，
#最后把最终结果生成出来

# generate or create 所有的点
# 定义一个方法叫做generate_points(row_index:y, column_index:x)
def create_points(row_index, column_index, size):
    points = set()
    # 生成的点
    cs = column_index + size
    for current_column_index in range(column_index, cs):
        points.add((row_index, current_column_index))  # 这里面存的是一个tuple
    rs = row_index + size
    for current_row_index in range(row_index, rs):
        points.add((current_row_index, cs - 1))
    for current_column_index in range(cs - 1, cs - 1 + size):
        points.add((rs - 1, current_column_index))
    return points

# check 这些点, check 里面这些点都是1
def observe_points_are_all_1(points):
    for point in points:
        row_index, column_index = point
        # check y,x 因为上面没有加出界的判断
        lg = len(grid)
        lg_0 = len(grid[0])
        if row_index >= 0 and row_index < lg \
            and column_index >= 0 and column_index < lg_0 \
                and grid[row_index][column_index] != 0:
            # 在界内判断它不等于0， 也就是等于1
            pass
        else:
            return False  # 上面的条件不满足就return 一个False
    else:
        return True  # 所有的条件都满足：每个点都是1


# 0123456

# 111
#  1
#  111  (第一个点是（2,2）)        #已知一个step和一个size求第一个点： y + step * (size -1)
#    1                                                          x + step * (size -1)
#    111    (第一个点是（4,4）)
#      1
#      111      (第一个点是（6,6）)
# 假设已知第一阶梯step = 1, size = 3，现在需要check 下一个step, 针对step 里某个特定的点来check

def observe_steps(row_index, column_index, size):
    #一开始step等于0
    steps = 0
    #还要记录所有的pass
    wanted_points = set()#如果是true 了，就把它记录下来visited.union(points),证明里面的点都是我们想要的点
    while (True):
        q = steps * (size - 1)
        new_r = row_index + q
        new_c = column_index + q
        new_point = create_points(new_r, new_c, size)
        points = new_point
        #不停的check 它的step
        if observe_points_are_all_1(points):
            wanted_points.update(points)
            steps += 1
        else:
            break
# 对于固定的size, 我们check 它的step,如果step是1 check2，以此类推
    return steps, wanted_points

#有check step，现在要check size 了
#把下面的for 封装一下
def check_stairs_found(stairs,wanted_points):
    si = stairs.items()
    for point, v in si:
        vv = v.values()
        for others_wanted_points in vv:
             # 如果空集就是已经访问过了，如果有内容就continue
            if wanted_points - others_wanted_points:
                continue
            else:
                # 空集
                return False
    #如果没有找到
    return True

#110 只要等于0就不是它的长度
#111
def check_maxi_mini_size(row_index, column_index, stairs):
    #先求最大的size
    lg_0 = len(grid[0])
    size = lg_0 - column_index
    #最小的size是2，先check 长的
    while size >= 2:
        ObserveSteps = observe_steps(row_index, column_index, size)
        steps, wanted_points = ObserveSteps
        #没有找到可以包含的子stair
        #如果visited 里面有内容（表示从y到x这个点有个梯子，梯子的大小是要取的size, steps）：(如果step 为0， wanted_points 为空)
        CheckStairsFound = check_stairs_found(stairs, wanted_points)
        if wanted_points and CheckStairsFound:
            main_tuple = (row_index, column_index)
            stairs[main_tuple][(steps, size)] = wanted_points #表示在这个点上有step,size,因为一个点上可能有多个step,size,需要check一下
            #size check 完了，现在check 比它小的size
        size -= 1

#已经check,step,size，现在要去check 每一个点,因为点可能有重复的
def check_each_RowColumnTuple():
    stairs = defaultdict(dict)
    lg = len(grid)
    for row_index in range(lg):
        lg_0 = len(grid[0])
        for column_index in range(lg_0):
            grid_rc = grid[row_index][column_index]
            if grid_rc != 0:
                check_maxi_mini_size(row_index, column_index, stairs)

    real_stair = defaultdict(dict)
    for v in stairs.values():
        for k in v.keys():
            steps, size = k
            rs_size = real_stair[size]
            if steps in rs_size:
                real_stair[size][steps] += 1
            else:
                real_stair[size][steps] = 1
    return real_stair

print_stairs = check_each_RowColumnTuple()
if print_stairs:
    #把里面的size 和size排序：
    for print_size in sorted(print_stairs.keys()):
        print(f"\nFor steps of size {print_size}, we have:")
        #step也要排序
        for print_step in sorted(print_stairs[print_size].keys()):
            a = print_stairs[print_size][print_step]
            b = print_step
            if a != 1 and b == 1:
                print(f"     {a} stairs with {b} step")
            elif a != 1 and b != 1:
                print(f"     {a} stairs with {b} steps")
            elif a == 1 and b == 1:
                print(f"     {a} stair with {b} step")
            else:
                print(f"     {a} stair with {b} steps")

