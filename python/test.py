from PIL import Image
import image as sdk_im
import camera_model as camera
import glob

image_list = []
model = camera.CameraModel("/home/tusimple-sudo/robotcar-dataset-sdk/models/", "/home/tusimple-sudo/Downloads/sample/stereo/left/")
for filename in glob.glob('/home/tusimple-sudo/Downloads/sample/stereo/left/*.png'): 
    im_arr = sdk_im.load_image(filename)
    im_arr = model.undistort(im_arr)
    im = Image.fromarray(im_arr)
    filename_arr = filename.split("/")
    filename = filename_arr[len(filename_arr)-1]
    im.save("/home/tusimple-sudo/result/%s" % getName)
