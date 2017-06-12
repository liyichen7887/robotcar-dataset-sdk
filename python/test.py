from PIL import Image
import image as sdk_im
im_arr = sdk_im.load_image("/home/tusimple-sudo/Downloads/sample/stereo/left/1418381798076682.png")
im = Image.fromarray(im_arr)
im.save("test.png")
