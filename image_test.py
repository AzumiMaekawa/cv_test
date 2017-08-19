from PIL import Image
from pylab import *


im = Image.open('lena.png')
imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# 赤い星マークで描画する
plot(x, y, 'r*')

plot(x[:2], y[:2])

title('Plottting: "lena.png"')
show()
