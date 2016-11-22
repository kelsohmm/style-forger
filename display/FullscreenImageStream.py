from Animation import Animation
from helpers import resizeRawImage


class FullscreenImageStream:
    def __init__(self, canvas, imageProvider, windowSize):
        self.canvas = canvas
        self.imageProvider = imageProvider
        self.windowSize = windowSize
        self.windowCenter = calculateWindowCenter(*windowSize)
        self.currentPhoto = None

    def draw(self, timePassed):
        self.currentPhoto = resizeRawImage(self.imageProvider.getRawImage(), self.windowSize)
        self.canvas.create_image(self.windowCenter, image=self.currentPhoto)

def calculateWindowCenter(windowWidth, windowHeight):
    return windowWidth/2, windowHeight/2