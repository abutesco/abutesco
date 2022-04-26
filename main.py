
import numpy as np
import skimage.io
import skimage.viewer
import matplotlib.pyplot as plt
# import ipympl
import cv2
# from colorthief import ColorThief

camera = skimage.io.imread(fname="cat2.jpg")

while True:
    image = camera.read()
    cv2.imshow('image', image)
        # save the image
    cv2.imwrite('cattest1.jpg', image)
camera.release()
cv2.destroyAllWindows()


