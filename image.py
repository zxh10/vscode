# -*- coding: utf-8 -*-

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# 输入图片的完整路径，打开该图片
location = input("Please input the location of the image:")
target = input(
    "Please input the new name of target, you can enter to get the default name:"
)
image = Image.open(location)

# 获得当前图片的大小，根据此参数设置字体大小
xSize, ySize = image.size
font = ImageFont.truetype("arial.ttf", int(ySize / 8))

# 在图片上添加数字3
draw = ImageDraw.Draw(image)
draw.text((0.9 * xSize, 0.1 * ySize), "3", (255, 0, 0), font)

# 根据输入的命名来设置新图片名字，默认设置为“原名_new”，格式与原图相同
form = location.split('.')[1]
if target == "":
    new_location = location.split('.')[0]
    image.save(new_location + '_new.' + form)
else:
    image.save(target + '.' + form)
