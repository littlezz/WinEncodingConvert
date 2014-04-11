import sys
import os


#compatible with Windows

def main():

    filePath= sys.argv[1] if len(sys.argv)>1 else input('Enter the filePath')
    
    #enter another value to define the newFile name when use shell
    newFileName=sys.argv[2] if len(sys.argv)>2 else None
    print(format('filepath:','<30'),filePath)
    convert(filePath,newFileName,'cp936','utf-8')
    input('Press Enter To Exit')




def convert(filePath,newFileName,oldEncoding,newEncoding):
    """ convert file by assign oldEncoding and newEncoding"""

    try:
        with open(filePath,'r',encoding=oldEncoding) as f:
            newFileName=newFileName if newFileName else 'utf8_'+os.path.basename(filePath)
            with open(newFileName,'w',encoding=newEncoding)as nf:
                nf.write(f.read())
        print('Successful!')
        print(format('New file Name:','<30'),newFileName)
    except FileNotFoundError:
        print("Can not find the file !")
    
if __name__ == '__main__':
    main()