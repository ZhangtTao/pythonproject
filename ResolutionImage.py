import cv2
import numpy as np
class ResolutionImage:
    def __init__(self,Image):
        self.img=Image
    def getpixel(self,co,channel):
        assert isinstance(co,tuple),"co must be tuple"
        self.img.item(co,channel)
    def setpixel(self,co,channel,value):
        assert isinstance(co, tuple), "co must be tuple"
        self.img.item()
    def getresolution(self):
        return self.img.shape[0],self.img.shape[1]
    def getareapixel(self,sv,ev):
        return self.img[sv[0]:sv[1],ev[0]:ev[1]]
    def BGRsplit(self):
        return cv2.split(self.img)
if __name__=='__main__':
    img = cv2.imread(r'C:\Users\Administrator\Desktop\t01d53dd07ee8929638.jpg')
    resolveimg=ResolutionImage(img)
    print(resolveimg.BGRsplit())