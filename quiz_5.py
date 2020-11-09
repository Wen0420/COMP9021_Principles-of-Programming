# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Uses National Data on the relative frequency of given names in the
# population of U.S. births, stored in a directory "names", in files
# named "yobxxxx.txt with xxxx (the year of birth)
# ranging from 1880 to 2018.
# The "names" directory is a subdirectory if the working directory.
# Prompts the user for a male first name, and finds out the years
# when this name was most popular in terms of ranking amongst male names.
# Displays the ranking, and the years in decreasing order of frequency,
# computed, for a given year, as the count of the name for the year
# divided by the sum of the counts of all male names for the year.


import csv
from pathlib import Path

cwd = Path.cwd()
possible_path_1 = cwd.parent.parent / 'names'
possible_path_2 = Path(cwd.root) / 'course' / 'data' / 'names'
if possible_path_1.exists():
    # FOR ME
    path = possible_path_1
elif possible_path_2.exists():
    # FOR ED
    path = possible_path_2
else:
    # FOR YOU, names IS A SUBDIRECTORY OF THE WORKING DIRECTORY
    path = Path('names')

# INSERT YOUR CODE HERE

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Uses National Data on the relative frequency of given names in the
# population of U.S. births, stored in a directory "names", in files
# named "yobxxxx.txt with xxxx (the year of birth)
# ranging from 1880 to 2018.
# The "names" directory is a subdirectory if the working directory.
# Prompts the user for a male first name, and finds out the years
# when this name was most popular in terms of ranking amongst male names.
# Displays the ranking, and the years in decreasing order of frequency,
# computed, for a given year, as the count of the name for the year
# divided by the sum of the counts of all male names for the year.


import csv
from pathlib import Path

cwd = Path.cwd()
possible_path_1 = cwd.parent.parent / 'names'
possible_path_2 = Path(cwd.root) / 'course' / 'data' / 'names'
if possible_path_1.exists():
    # FOR ME
    path = possible_path_1
elif possible_path_2.exists():
    # FOR ED
    path = possible_path_2
else:
    # FOR YOU, names IS A SUBDIRECTORY OF THE WORKING DIRECTORY
    path = Path('names')

# INSERT YOUR CODE HERE



input_first_name = input("Enter a male first name: ")

from collections import defaultdict
freq_years = defaultdict(list)

#读文件1880-2018年
for file_year in range(1880, 2018 + 1):
    data_name = path/f"yob{file_year}.txt"
#判断文件是否存在
    if path.exists():
        #读文件
        with open(data_name) as open_file:
            male_name = []
            frequency = []
#按行来读
            lines = []
            for line in open_file:
                lines.append(line)

                a = line.split(",")
                name = a[0]
                gender = a[1]
                freq = a[2]

                if gender == 'M':
                    male_name.append(name)
                    frequency.append(int(freq))
            #判断名字是否存在，如果在就去找它的排名
            if input_first_name in male_name:
                #index 在第几个就是ranking
                #出现的频次对应的年分
               #这个时候freq对应着ranking,file_year, index
                #这里面可能是放index,如果是index，找排名最小，如果是freq,找最大的一个。
                freq_years[male_name.index(input_first_name)].append((frequency[male_name.index(input_first_name)] / sum(frequency), file_year))
#判断是否有freq_years
if freq_years:
#假设是index,就找最小的
    minimum_key = min(freq_years.keys())
    print(f"By decreasing order of frequency, {input_first_name} was most popular in the following years:")
#现在找到他要把years取出来
    #years = sorted(freq_years[minimum_key])
    years = []#可以直接把下面两行删掉，把这行变为years = [str(item[1]) for item in sorted(freq_years[minimum_key], reverse=True)]
    f = freq_years[minimum_key]
    for item in sorted(f, reverse=True):
        years.append(str(item[1]))
    #现在去print,每5 个一打印
    for index in range(0, len(years), 5):
        print("","","","","".join([" ".join(years[index:index + 5])]))
    #现在需要给一个排名#Its rank was 9771 then.
    print(f"Its rank was {minimum_key + 1} then.")

else:
    print(f"{input_first_name} is not a male first name in my records.")
