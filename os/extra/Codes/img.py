from PIL import Image,ImageEnhance,ImageFilter
import os,shutil
# lista = os.listdir()
# i = 1
# for item in lista:
#     if item.endswith('.jpg'):
#         shutil.move(item,f'{os.getcwd()}/{i}.jpg')
#         i += 1
img1 = Image.open('2.jpg')
# img1.save('4.png')
# max = (2222,2222)
# img1.thumbnail(max)
# img1.save('5.png')


# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1.4).save('5.jpg')
img1.filter(ImageFilter.GaussianBlur(radius = 1.4)).save('5.jpg')