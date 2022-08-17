from ast import arg
from asyncio import FastChildWatcher
from threading import Thread
from tkinter.tix import Tree
import cv2

class WebcamVideoStream:
    def __init__(self, src: int):
        self.stream = cv2.VideoCapture(src)

        (self.grabbed, self.frame) = self.stream.read()

        self.stopped = False


    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                self.stream.release()
                return
        
            (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True
        

    def read(self):
        return self.frame