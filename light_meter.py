import numpy as np

from time import sleep
from picamera2 import PiCamera

lsize = (320, 240)
picam2 = Picamera2()
video_config = picam2.create_video_config(main={"size"})