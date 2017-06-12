from PIL import Image
from image import sdk_im
im_arr = sdk_im.load_image("/home/tusimple-sudo/Downloads/sample/stereo/left/")
im = Image.fromarray(im_arr)
im.save("test.png")
