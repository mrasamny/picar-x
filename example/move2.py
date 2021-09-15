import sys
sys.path.append(r'/home/pi/picar-x/picar')
from utils import reset_mcu
reset_mcu()

from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        px = Picarx()
        px.pan_camera(0)
        #px.forward(-30)
        time.sleep(2)
        #px.forward(0)
        time.sleep(1)


    finally:
        px.forward(0)


