def biFiles():
    fileContainer = open('Nobita.jpg', 'rb')
    newFile = open('new_nobita.jpg', 'wb')
    bufferSize = 50000
    buffer = fileContainer.read(bufferSize)
    while len(buffer) :
        newFile.write(buffer)
        buffer = fileContainer.read(bufferSize)


biFiles()