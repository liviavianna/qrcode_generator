from pyqrcode import *
from png import *

url = pyqrcode.create('https://www.instagram.com/lilizok4/')
url.svg('ig-url.svg', scale=5)
url.png('ig-url.png', scale=5, module_color=(127, 17, 224), background=(255, 255, 255, 255))
