import time

def operation():
    inFile = open('two.txt', 'r')
    outFile = open('Output.txt', 'a')
    
    for line in inFile:
        outFile.write(line)
    outFile.write("\nWritten By : Aditya Tiwari")


def charByte():
    fileContainer = open('one.txt')
    start_time = time.time()
    print(fileContainer.read(10))
    sec = str( (time.time() - start_time ) / 60)
    print('The time taken is {0} '.format(sec))

charByte()

'''

#funtions in file handling

////////////opens a file/////////////////
fileContainer = open('fileName', 'mode')

//////////////reads file word by word////////////////////
fileContainer.read()

//////////////////reads only character those sums up provided byte size
fileContainer.read( byteThatsToBeRead )

//////////////////reads a whole line and returns an iterable object////////////////////
fileContainer.readlines()

//////////////////writes a string to stream in file///////////////////////////////////////
fileContainer.write(string)


'''