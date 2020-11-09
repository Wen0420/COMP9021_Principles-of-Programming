# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n
#   is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together
#   with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing
# the standard form decomposition of the permutation into cycles
# (see wikepedia page on permutations for details).
# - A given cycle starts with the largest value in the cycle.
# - Cycles are given from smallest first value to largest first value.
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix
# and in-place uses.


class PermutationError(Exception):
    pass


# class Permutation:
#     def __init__(self, *args, length=None):
#         pass
#         # Replace pass above with your code

#     def __len__(self):
#         pass
#         # Replace pass above with your code

#     def __repr__(self):
#         pass
#         # Replace pass above with your code

#     def __str__(self):
#         pass
#         # Replace pass above with your code

#     def __mul__(self, permutation):
#         pass
#         # Replace pass above with your code

#     def __imul__(self, permutation):
#         pass
#         # Replace pass above with your code

#     def inverse(self):
#         pass
#         # Replace pass above with your code

#     # Insert helper functions, if needed
class Permutation:
    # - A given cycle starts with the largest value in the cycle.
    # - Cycles are given from smallest first value to largest first value.
    # check cycle#写一个方法，在值的基础上check cycle
    # arts with the largest value
    # 例如：（1, 2, 3, 4)，索引值是 0 1 2 3， cycle 就是索引值等于它自己这里= 1 2 3 4
    # 例如： （2, 3, 4, 5, 1) 索引值是1 2 3 4 5 对应的值， 1-2 2-3 3-4 4-5 5-1，索引值去取对应的value，把value当作是新的索引值再去取value直到找到头尾相等
    # largest 是5， 5-1， 1-2，2-3， 3-4， 4-5结束
    # 特殊情况（1, 3, 4, 5, 1)check有不相等的， （1, 3, 4, 5, 6)check length, 加在初始条件里
    def FindCycle(self, largest):
        # 给定一个最大值check住一个cycle
        cycles = []
        # largest value = 5
        # indexvalue = 1
        next_largest = self.args[largest - 1]
        # 如果自己等于自己就结束
        FoundCycles = [largest]
        if next_largest != largest:
            # 继续去取下一个值
            # next 值是2 （5-1 1-2）
            # 只要next value 不等于 largest value:
            # 1 不等于5就继续走
            while self.args[next_largest - 1] != largest:
                FoundCycles.append(next_largest)
                next_largest = self.args[next_largest - 1]
            else:
                FoundCycles.append(next_largest)
        return FoundCycles

    # init 是在初始化class
    def __init__(self, *args, length=None):
        pass
        if args:
            for item in args:
                # 元组里面的每一个值都是int
                if not isinstance(item, int):
                    raise PermutationError("Cannot generate permutation from these arguments")
                elif item <= 0:
                    raise PermutationError("Cannot generate permutation from these arguments")
                elif length is not None and item > length:
                    # 里面的元素不能超过这个length
                    raise PermutationError("Cannot generate permutation from these arguments")
                # 此时第一个case 可以过，因为第一个case是一个字符串，而我已经判断只要它不是int就跳出， 第二个case也可以过
                # Permutation(2, 1, 0)--》小于等于0就报错：
        # 判断Permutation(3, 2, 1, length=4)
        # 如果参数和长度不为空，还有长度一定要等于参数的长度，不等于就报错
        if length is not None:
            if length <= 0:
                raise PermutationError("Cannot generate permutation from these arguments")
            if args:
                if len(args) != length:
                    raise PermutationError("Cannot generate permutation from these arguments")

        # args and length 都有值
        if args and length is not None:
            if len(set(args)) != length:
                raise PermutationError("Cannot generate permutation from these arguments")
                # 上面已经检查过了，现在要把它存下来
            self.args = args  # 左边；类里面的变量（或者类的属性例如args,length）方 。 右边：方法内的局部变量
            self.length = length
            # 如果args不为空
        elif args:
            self.args = args
            self.length = len(args)
            # 如果长度不为空,默认生成一组数：
        elif length is not None:
            self.length = length
            self.args = tuple(x + 1 for x in range(length))
            # 都为空
        else:
            self.length = 0
            self.args = tuple()

        self.FooundAllCycles = set()
        # 找到了cycle了，如何删掉原来的
        # 复制一份列表,找max check cycle如果不为空就把找到的删掉继续去找,继续找用while
        FooundAllCycles = set([x for x in self.args])
        while FooundAllCycles:
            # 获取cycles
            if self.FindCycle(max(FooundAllCycles)):
                c = self.FindCycle(max(FooundAllCycles))
                FooundAllCycles = FooundAllCycles - set(c)
                self.FooundAllCycles.add(tuple(c))  # 把找到的添加
            else:
                break

        self.nb_of_cycles = len(self.FooundAllCycles)

        # 接下来length 直接返回上面的length 就可以了

    def __len__(self):
        pass
        # Replace pass above with your code
        return self.length

    def __repr__(self):
        pass
        # Replace pass above with your code
        # (1)(2)(3)(4), 用逗号分割， join args里面的内容, 注意int类型没有办法用join
        # result = f"Permutation({', '.join(self.args)})"
        # 注意int类型没有办法用join,把它转换成字符串
        return f"Permutation({', '.join((str(x) for x in self.args))})"

    def __str__(self):
        pass
        # replace pass above with your code
        final = ""
        if self.FooundAllCycles:
            for items in sorted(self.FooundAllCycles):
                final = final + "(" + " ".join(str(x) for x in items) + ")"
        else:
            final = "()"
        return final

    def __mul__(self, permutation):
        pass
        # Replace pass above with your code
        # 先判断他们不一样
        if self.length != permutation.length:
            raise PermutationError("Cannot compose permutations of different lengths")
        else:
            return Permutation(*[permutation.args[P1_i - 1] for P1_i in self.args])

    def __imul__(self, permutation):
        pass
        # Replace pass above with your code
        if self.length != permutation.length:
            raise PermutationError("Cannot compose permutations of different lengths")
        else:
            return Permutation(*[permutation.args[P1_i - 1] for P1_i in self.args])

    def inverse(self):
        pass
        # Replace pass above with your code
        # inverse是指索引值和数字
        # 1   2   3   4   5
        # （2， 3， 4， 5， 1）
        # 索引和value 一一对应
        ##用枚举的方式,遍历每一个数，但遍历有一个基准，基准设为一从1开始
        final = {value: index for index, value in enumerate(self.args, start=1)}

        return Permutation(*[final[key] for key in sorted(final.keys())])

    # Insert helper functions, if needed

