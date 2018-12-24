import re

fileContainer = open("one.txt", "r")
pattern = re.compile('google')
# using re.search() which returns true or false depending on whether the pattern is available
def isSearch(fileContainer):
    for line in fileContainer:
        if re.search(pattern, line):
            print(line, end = '\n')


#using re.subn() which returns tuple of line read and numbers of replacement done per line
def isSubn():
    for line in fileContainer:
        tup, num = re.subn('regular', 'non-linear', line)
        print('The returned string from subn is "{tupl}" and number of replacement of word done are {num}.'.format(tupl = tup, num = num))

isSearch(fileContainer)