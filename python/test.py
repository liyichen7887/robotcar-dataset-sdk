from PIL import Image
import image as sdk_im
import camera_model as camera
import glob

def getName(num):
    strTmp = []
    strRes = ''

    while(num / 10):
        strTmp.append(num % 10)
        num = num / 10
    strTmp.append(num)
    n = len(strTmp)
    for i in range(0,5-n):
        strRes = strRes + '0'
    for i in range(n-1,-1,-1):
        strRes = strRes + str(strTmp[i])
    return strRes

image_list = []
idx = 1

model = camera.CameraModel("/home/tusimple-sudo/robotcar-dataset-sdk/models/", "/home/tusimple-sudo/Downloads/sample/stereo/left/")
for filename in glob.glob('/home/tusimple-sudo/Downloads/sample/stereo/left/*.png'): 
    im_arr = sdk_im.load_image(filename)
    im_arr = model.undistort(im_arr)
    im = Image.fromarray(im_arr)
    #filename_arr = filename.split("/")
    #filename = filename_arr[len(filename_arr)-1]
    im.save("/home/tusimple-sudo/result/"+getName(idx)+'.png')
    idx = idx + 1
