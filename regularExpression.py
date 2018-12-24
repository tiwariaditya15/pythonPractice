import re

fileContaner = open("one.txt", "r")
pattern = re.compile('google')
# using re.search() which returns true or false depending on whether the pattern is available
def isSearch(fileContaner):
    for line in fileContaner:
        if re.search(pattern, line):
            print(line, end = '\n')


#using re.subn() which returns tuple of line read and numbers of replacement done per line
def isSubn():
    for line in fileContaner:
        tup, num = re.subn('regular', 'non-linear', line)
        print('The returned string from subn is "{tupl}" and number of replacement of word done are {num}.'.format(tupl = tup, num = num))

isSearch(fileContaner)