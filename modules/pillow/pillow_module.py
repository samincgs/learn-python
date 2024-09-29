import os
from PIL import Image, ImageFilter

size_300 = (300, 300)
size_700 = (700, 700)

# use pillow to manipulate images with python
# display them, modifying colors, change sizes
naruto = Image.open('naruto_hw.jpg')

# show image
naruto.show()

# save file as different extension
naruto.save('naruto_hw.png') # changed jpg to png

# work with multiple images in the same folder
# convert all jpgs in the folder into pngs
for f in os.listdir('.'): # use . for current directory
    if f.endswith('.jpg'):
        image = Image.open(f)
        fn, fext = os.path.splitext(f)
        
        image.thumbnail(size=size_700)
        image.save(f'700x700/{fn}_700{fext}')
        
        image.thumbnail(size=size_300)
        image.save(f'300x300/{fn}_300{fext}')
        
# rotate an image
naruto.rotate(90).show()

# turn an image black and white
naruto.convert(mode='L').show()

# blur an image (use Image Filter)
naruto.filter(ImageFilter.GaussianBlur()).show()