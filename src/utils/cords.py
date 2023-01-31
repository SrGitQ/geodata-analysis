import math
import re

def dms2dd(s):   
    try:
        degrees, minutes, seconds, direction = re.split('[Â°\'"]+', s)
    except:
        return 0
    else:
        dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction in ('S','W'):
        dd*= -1
    return dd
