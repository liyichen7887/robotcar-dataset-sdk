from PIL import Image
import image as sdk_im
import camera_model as camera

im_arr = sdk_im.load_image("/home/tusimple-sudo/Downloads/sample/stereo/left/1418381798076682.png")
mode = CameraModel("../models/stereo_narrow_left.txt", "/home/tusimple-sudo/Downloads/sample/stereo/left/")
im_arr = model.undistort(im_arr)
im = Image.fromarray(im_arr)
im.save("test.png")
