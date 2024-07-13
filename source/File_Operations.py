import os

def openFile(filename, mode):  
  return open(filename, mode)

def writeFile(file, text):  
  file.writelines(text)

def closeFile(file):  
  file.close()

def deleteFile(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)