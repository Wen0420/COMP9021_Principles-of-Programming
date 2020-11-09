# Insert your code here
class Frieze:
    def __init__(self, path):
        self.path = path
        self.period = None
        self.frieze = self.__check_path(path)

    def __check_path(self, path):
        incorrectInput = FriezeError('Incorrect input.')
        notFrieze = FriezeError('Input does not represent a frieze.')
        frieze = []
        with open(path) as friezeFile:
            try:
                rowIndex = 0
                for line in friezeFile:
                    if line.isspace():
                        continue
                    currentRow = [int(number) for number in line.split()]
                    for number in currentRow:
                        if number > 15 or number < 0:
                            raise incorrectInput
                    frieze.append(currentRow)
                    if rowIndex > 0:
                        rowLength = len(frieze[rowIndex])
                        if len(frieze[rowIndex - 1]) != rowLength or rowLength < 4 + 1 or rowLength > 50 + 1:
                            raise incorrectInput
                    rowIndex += 1
                if rowIndex > 16 + 1 or rowIndex < 2 + 1:
                    raise incorrectInput
            except ValueError:
                raise incorrectInput

        friezeLength = len(frieze[0]) - 1
        friezeHeight = len(frieze) - 1

        for number in frieze[0][0:-1]:
            if number not in (4, 12):
                raise notFrieze

        if frieze[0][-1] != 0:
            raise notFrieze
        for row in frieze[1:]:
            if row[-1] not in (0, 1):
                raise notFrieze
            if row[-1] == 1:
                if row[0] % 2 == 0:
                    raise notFrieze

        for number in frieze[-1][0:-1]:
            if number > 7 or number < 4:
                raise notFrieze

        for i in range(friezeHeight):
            for j in range(friezeLength):
                if frieze[i][j] > 7:
                    if frieze[i + 1][j] in (2, 3, 6, 7, 10, 11, 14, 15):
                        raise notFrieze

        friezePeriod = None
        for period in range(1, friezeLength):
            tranisitive = True
            for i in range(friezeHeight + 1):
                if not tranisitive:
                    break
                for j in range(friezeLength):
                    if frieze[i][(j + period) % friezeLength] != frieze[i][j]:
                        tranisitive = False
                        break
            if tranisitive:
                friezePeriod = period
                break

        if friezePeriod is not None and friezePeriod > 1:
            self.period = friezePeriod
            return [[(
                number, number >> 3,
                (number & 4) >> 2,
                (number & 2) >> 1,
                number & 1,
            ) for number in row] for row in frieze]
        else:
            raise notFrieze

    def analyse(self):
        horizontal_reflection = self.__is_horizontal_reflection()
        glided_horizontal_reflection = self.__is_glided_horizontal_reflection()
        vertical_reflection = self.__is_vertical_reflection()
        rotation_reflection = self.__is_rotation_reflection()
        baseString = f'Pattern is a frieze of period {self.period} that is invariant under translation'
        if not vertical_reflection and not horizontal_reflection and not glided_horizontal_reflection and not rotation_reflection:
            print(baseString + ' only.')
        elif vertical_reflection and not horizontal_reflection and not glided_horizontal_reflection and not rotation_reflection:
            print(baseString + '\n        and vertical reflection only.')
        elif not vertical_reflection and horizontal_reflection and not rotation_reflection:
            print(baseString + '\n        and horizontal reflection only.')
        elif not vertical_reflection and not horizontal_reflection and glided_horizontal_reflection and not rotation_reflection:
            print(baseString + '\n        and glided horizontal reflection only.')
        elif not vertical_reflection and not horizontal_reflection and not glided_horizontal_reflection and rotation_reflection:
            print(baseString + '\n        and rotation only.')
        elif vertical_reflection and not horizontal_reflection and glided_horizontal_reflection and rotation_reflection:
            print(
                baseString + ',\n        glided horizontal and vertical reflections, and rotation only.')
        elif vertical_reflection and horizontal_reflection and rotation_reflection:
            print(
                baseString + ',\n        horizontal and vertical reflections, and rotation only.')

    def __is_horizontal_reflection(self):
        friezeLength = len(self.frieze[0])
        friezeHeight = len(self.frieze)

        if friezeHeight % 2 == 0:
            lowerRow = friezeHeight // 2
            upperRow = lowerRow - 1
            for y in range(friezeLength):
                if self.frieze[upperRow][y][1] or self.frieze[lowerRow][y][3]:
                    return False
            reflection = [
                [0 for i in range(friezeLength)]
                for j in range(lowerRow)
            ]
            for x in range(lowerRow, friezeHeight):
                for y in range(friezeLength):
                    if self.frieze[x][y][4] and x != lowerRow:
                        reflection[x - lowerRow - 1][y] += 1
                    if self.frieze[x][y][3]:
                        reflection[x - lowerRow][y] += 8
                    if self.frieze[x][y][2]:
                        reflection[x - lowerRow][y] += 4
                    if self.frieze[x][y][1]:
                        reflection[x - lowerRow][y] += 2
                if x > lowerRow:
                    friezeRowIndex = friezeHeight - x
                    reflectionRowIndex = x - lowerRow - 1
                    for i in range(friezeLength):
                        if reflection[reflectionRowIndex][i] != self.frieze[friezeRowIndex][i][0]:
                            return False
            for i in range(friezeLength):
                if reflection[-1][i] != self.frieze[0][i][0]:
                    return False
            return True
        else:
            centerRow = friezeHeight // 2
            for i in range(friezeLength):
                if self.frieze[centerRow][i][4]:
                    if not self.frieze[centerRow + 1][i][4]:
                        return False
                if self.frieze[centerRow][i][3]:
                    if not self.frieze[centerRow][i][1]:
                        return False
                if self.frieze[centerRow][i][1]:
                    if not self.frieze[centerRow][i][3]:
                        return False
                if self.frieze[centerRow + 1][i][4]:
                    if not self.frieze[centerRow][i][4]:
                        return False

            reflection = [
                [0 for i in range(friezeLength)]
                for j in range(centerRow)
            ]
            beginRow = centerRow + 1
            for x in range(beginRow, friezeHeight):
                for y in range(friezeLength):
                    if self.frieze[x][y][4] and x != beginRow:
                        reflection[x - beginRow - 1][y] += 1
                    if self.frieze[x][y][3]:
                        reflection[x - beginRow][y] += 8
                    if self.frieze[x][y][2]:
                        reflection[x - beginRow][y] += 4
                    if self.frieze[x][y][1]:
                        reflection[x - beginRow][y] += 2
                if x > beginRow:
                    reflectionRowIndex = x - beginRow - 1
                    friezeRowIndex = friezeHeight - x
                    for i in range(friezeLength):
                        if reflection[reflectionRowIndex][i] != self.frieze[friezeRowIndex][i][0]:
                            return False
            for i in range(friezeLength):
                if reflection[-1][i] != self.frieze[0][i][0]:
                    return False
            return True

    def __is_glided_horizontal_reflection(self):
        if self.period % 2 == 1:
            return False
        friezeHeight = len(self.frieze)
        friezeLength = len(self.frieze[0])
        glide_period = self.period // 2
        if friezeHeight % 2 == 0:
            lowerRow = friezeHeight // 2
            last_row_num = lowerRow - 1
            reflection = [
                [0 for i in range(friezeLength)]
                for j in range(lowerRow)
            ]
            for x in range(lowerRow):
                for y in range(friezeLength):
                    if self.frieze[x][y][4]:
                        reflection[last_row_num - x + 1][y] += 1
                    if self.frieze[x][y][3]:
                        reflection[last_row_num - x][y] += 8
                    if self.frieze[x][y][2]:
                        reflection[last_row_num - x][y] += 4
                    if self.frieze[x][y][1]:
                        reflection[last_row_num - x][y] += 2
            friezeLength -= 1
            for y in range(friezeLength + 1):
                if self.frieze[lowerRow][y][4]:
                    reflection[0][y] += 1
                if self.frieze[lowerRow][y][3] and not self.frieze[lowerRow - 1][(y + glide_period) % friezeLength][1]:
                    return False
            for x in range(lowerRow):
                for y in range(friezeLength):
                    if reflection[x][y] != self.frieze[lowerRow + x][(y + glide_period) % friezeLength][0]:
                        return False
            return True
        else:
            centerRow = friezeHeight // 2
            reflection = [
                [0 for i in range(friezeLength)]
                for j in range(centerRow + 1)
            ]
            lower_frieze_first_row = [
                self.frieze[centerRow][y][0]
                for y in range(friezeLength)
            ]
            for y in range(friezeLength):
                if self.frieze[centerRow][y][4]:
                    lower_frieze_first_row[y] -= 1
                if self.frieze[centerRow][y][3]:
                    lower_frieze_first_row[y] -= 2
            for y in range(friezeLength):
                if self.frieze[centerRow][y][3]:
                    reflection[0][y] += 8
                if self.frieze[centerRow][y][2]:
                    reflection[0][y] += 4
                if self.frieze[centerRow][y][4]:
                    reflection[1][y] += 1
            friezeLength -= 1
            for y in range(friezeLength):
                if reflection[0][y] != lower_frieze_first_row[(y + glide_period) % friezeLength]:
                    return False
            for x in range(centerRow):
                for y in range(friezeLength+1):
                    if self.frieze[x][y][4]:
                        reflection[centerRow - x + 1][y] += 1
                    if self.frieze[x][y][3]:
                        reflection[centerRow - x][y] += 8
                    if self.frieze[x][y][2]:
                        reflection[centerRow - x][y] += 4
                    if self.frieze[x][y][1]:
                        reflection[centerRow - x][y] += 2
            for x in range(1, centerRow + 1):
                for y in range(friezeLength):
                    if reflection[x][y] != self.frieze[centerRow + x][(y + glide_period) % friezeLength][0]:
                        return False
            return True

    def __is_vertical_reflection(self):
        friezeHeight = len(self.frieze)
        friezeLength = len(self.frieze[0]) - 1

        for axis in range(self.period + 1):
            reflective = True
            for y in range(self.period + 1):
                if not reflective:
                    break
                for x in range(friezeHeight):
                    if (self.frieze[x][(axis + y) % friezeLength][4]
                            and not self.frieze[x][(axis - y) % friezeLength][4]
                        ) or (self.frieze[x][(axis + y) % friezeLength][3]
                              and not self.frieze[x - 1][(axis - y - 1) % friezeLength][1]
                              ) or (self.frieze[x][(axis + y) % friezeLength][2]
                                    and not self.frieze[x][(axis - y - 1) % friezeLength][2]
                                    ) or (self.frieze[x][(axis + y) % friezeLength][1]
                                          and not self.frieze[x + 1][(axis - y - 1) % friezeLength][3]):
                        reflective = False
                        break
                    elif y > 0:
                        if (self.frieze[x][(axis - y) % friezeLength][4]
                            and not self.frieze[x][(axis + y) % friezeLength][4]
                            ) or (self.frieze[x][(axis - y) % friezeLength][3]
                                  and not self.frieze[x - 1][(axis + y - 1) % friezeLength][1]
                                  ) or (self.frieze[x][(axis - y) % friezeLength][2]
                                        and not self.frieze[x][(axis + y - 1) % friezeLength][2]
                                        ) or (self.frieze[x][(axis - y) % friezeLength][1]
                                              and not self.frieze[x + 1][(axis + y - 1) % friezeLength][3]
                                              ):
                            reflective = False
                            break
            if reflective:
                return True

        for axis in range(self.period + 1):
            reflective = True
            for x in range(friezeHeight):
                if (self.frieze[x][axis][4]
                        and not self.frieze[x][(axis + 1) % friezeLength][4]
                        ) or (self.frieze[x][axis][3] or self.frieze[x][axis][1]):
                    reflective = False
                    break
            for y in range(1, self.period + 1):
                if not reflective:
                    break
                for x in range(friezeHeight):
                    if (self.frieze[x][(axis + y) % friezeLength][4]
                        and not self.frieze[x][(axis - y + 1) % friezeLength][4]
                        ) or (self.frieze[x][(axis + y) % friezeLength][3]
                              and not self.frieze[x - 1][(axis - y) % friezeLength][1]
                              ) or (self.frieze[x][(axis + y) % friezeLength][2]
                                    and not self.frieze[x][(axis - y) % friezeLength][2]
                                    ) or (self.frieze[x][(axis + y) % friezeLength][1]
                                          and not self.frieze[x + 1][(axis - y) % friezeLength][3]
                                          ) or (self.frieze[x][(axis - y) % friezeLength][4]
                                                and not self.frieze[x][(axis + y + 1) % friezeLength][4]
                                                ) or (self.frieze[x][(axis - y) % friezeLength][3]
                                                      and not self.frieze[x - 1][(axis + y) % friezeLength][1]
                                                      ) or (self.frieze[x][(axis - y) % friezeLength][2]
                                                            and not self.frieze[x][(axis + y) % friezeLength][2]
                                                            ) or (self.frieze[x][(axis - y) % friezeLength][1]
                                                                  and not self.frieze[x + 1][(axis + y) % friezeLength][3]):
                        reflective = False
                        break
            if reflective:
                return True
        return False

    def __is_rotation_reflection(self):
        friezeLength = len(self.frieze[0]) - 1
        friezeHeigth = len(self.frieze)
        if friezeHeigth % 2:
            middle = friezeHeigth // 2
            m = friezeHeigth // 2
        else:
            middle = friezeHeigth // 2 - 1
            m = friezeHeigth / 2 - 0.5
        for i in range(self.period + 1):
            is_rotation_reflection = True
            for x in range(friezeHeigth):
                if not is_rotation_reflection:
                    break
                for y in range(friezeLength):
                    if (self.frieze[x][y][4]
                        and not self.frieze[int(2 * m - x + 1)][(2 * i - y) % friezeLength][4]
                        ) or (self.frieze[x][y][3]
                              and not self.frieze[int(2 * m - x + 1)][(2 * i - y - 1) % friezeLength][3]
                              ) or (self.frieze[x][y][2]
                                    and not self.frieze[int(2 * m - x)][(2 * i - y - 1) % friezeLength][2]
                                    ) or (self.frieze[x][y][1]
                                          and not self.frieze[int(2 * m - x - 1)][(2 * i - y - 1) % friezeLength][1]):
                        is_rotation_reflection = False
                        break
            if is_rotation_reflection:
                return True

        for i in range(self.period + 1):
            is_rotation_reflection = True
            i_plus = i + 0.5
            for x in range(friezeHeigth):
                if not is_rotation_reflection:
                    break
                for y in range(friezeLength):
                    if (self.frieze[x][y][4]
                        and not self.frieze[int(2 * m - x + 1)][int(2 * i_plus - y) % friezeLength][4]
                        ) or (self.frieze[x][y][3]
                              and not self.frieze[int(2 * m - x + 1)][int(2 * i_plus - y - 1) % friezeLength][3]
                              ) or (self.frieze[x][y][2]
                                    and not self.frieze[int(2 * m - x)][int(2 * i_plus - y - 1) % friezeLength][2]
                                    ) or (self.frieze[x][y][1]
                                          and not self.frieze[int(2 * m - x - 1)][int(2 * i_plus - y - 1) % friezeLength][1]
                                          ):
                        is_rotation_reflection = False
                        break
            if is_rotation_reflection:
                return True
        return False

    def display(self):
        with open(f'{self.path[:-4]}.tex', 'w') as texFile:
            friezeHeight = len(self.frieze)
            friezeLenght = len(self.frieze[0])
            texFile.write(
                "\\documentclass[10pt]{article}\n\\usepackage{tikz}\n\\usepackage[margin=0cm]{geometry}\n\\pagestyle{empty}\n")
            texFile.write("\n\\begin{document}\n\n")
            texFile.write(
                "\\vspace*{\\fill}\n\\begin{center}\n\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]\n")

            texFile.write("% North to South lines\n")
            x = 0
            y = 0
            while y < friezeLenght:
                while x < friezeHeight:
                    if self.frieze[x][y][4]:
                        texFile.write(f'    \\draw ({y},{x-1}) -- ')
                        while True:
                            x += 1
                            if x == friezeHeight or not self.frieze[x][y][4]:
                                texFile.write(f'({y},{x-1});\n')
                                break
                    else:
                        x += 1
                x = 0
                y += 1

            texFile.write("% North-West to South-East lines\n")
            diagonalSet = set()
            for x in range(friezeHeight):
                for y in range(friezeLenght):
                    if self.frieze[x][y][1] and (x, y) not in diagonalSet:
                        diagonalSet.add((x, y))
                        texFile.write(f'    \\draw ({y},{x}) -- ')
                        xSwap, ySwap = x, y
                        x += 1
                        y += 1
                        while self.frieze[x][y][1]:
                            diagonalSet.add((x, y))
                            x += 1
                            y += 1
                        texFile.write(f'({y},{x});\n')
                        x, y = xSwap, ySwap

            texFile.write("% West to East lines\n")
            x = 0
            y = 0
            while x < friezeHeight:
                while y < friezeLenght:
                    if self.frieze[x][y][2]:
                        texFile.write(f'    \\draw ({y},{x}) -- ')
                        while self.frieze[x][y][2]:
                            y += 1
                        texFile.write(f'({y},{x});\n')
                    else:
                        y += 1
                y = 0
                x += 1

            texFile.write("% South-West to North-East lines\n")
            diagonalSet = set()
            southeast_northeast_coordinate = []
            for x in range(friezeHeight):
                for y in range(friezeLenght):
                    if (x, y) not in diagonalSet and self.frieze[x][y][3]:
                        diagonalSet.add((x, y))
                        endPoint = (x - 1, y + 1)
                        xSwap, ySwap = x, y
                        while True:
                            x += 1
                            y -= 1
                            if x == friezeHeight or y < 0 or not self.frieze[x][y][3]:
                                southeast_northeast_coordinate.append((
                                    (x - 1, y + 1),
                                    (endPoint[0], endPoint[1])
                                ))
                                break
                            else:
                                diagonalSet.add((x, y))
                        x, y = xSwap, ySwap

            southeast_northeast_coordinate.sort(key=lambda x: x[0])
            for val in southeast_northeast_coordinate:
                texFile.write(
                    f'    \\draw ({val[0][1]},{val[0][0]}) -- ({val[1][1]},{val[1][0]});\n')
            texFile.write(
                "\\end{tikzpicture}\n\\end{center}\n\\vspace*{\\fill}\n")
            texFile.write("\n\\end{document}\n")


class FriezeError(Exception):
    def __init__(self, message):
        self.message = message

