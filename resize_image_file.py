from PIL import Image
# My image is a 200x374 jpeg that is 102kb large
foo = Image.open("sailor_moon.png")
# I downsize the image with an ANTIALIAS filter (gives the highest quality)
foo = foo.resize((885, 500), Image.ANTIALIAS)
# foo.save("small_sailor_moon.png", quality=95)
# The saved downsized image size is 24.8kb
foo.save("small_sailor_moon.png", quality=95, optimize=True)
# The saved downsized image size is 22.9kb