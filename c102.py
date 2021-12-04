import cv2
import time
import random
import dropbox


start_time= time.time()

def take_snapshot():
    number= random.randint(0,100)
    videoCaptureObject= cv2.VideoCapture(0)
    result= True
    while(result):
        ret,frame= videoCaptureObject.read()
        img_name= "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time= time.time()
        result= False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    print("Image Taken")
    return img_name

def upload_files(img_name):
    access_token="9Wp9rsuQaJoAAAAAAAAAAb2JJiQb-pqw6pifTwZyPmNNkbUHfJuuwv3GIBZYQ3hl"

    file= img_name
    file_from= file
    file_to="/pictest/"+(img_name)
    dbx= dropbox.Dropbox(access_token)
        
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode= dropbox.files.WriteMode.overwrite)
        print("file_uploaded")



def main():
    while(True):
        if(time.time()-start_time>=1):
            name= take_snapshot()
            upload_files(name)
            break
main()