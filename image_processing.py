import pygame as pg

# grayPixel: pixel -> pixel
# compute and return a gray pixel with the same intensity
# as the given pixel
def grayPixel(pixel):
    red_intensity = pixel[0]
    green_intensity = pixel[1]
    blue_intensity = pixel[2]
    ave_intensity = (red_intensity + green_intensity+ blue_intensity)//3
    return (ave_intensity, ave_intensity, ave_intensity)

# channel: pixel -> channel -> pixel
# return a gray pixel with intensity from given channel of given pixel
def channel(pixel,chan):
    return (pixel[chan],pixel[chan],pixel[chan])


# inverse: pixel -> pixel
# return the color negative of the given pixel
def inverse(pixel):
    return (255-pixel[0], 255-pixel[1], 255-pixel[2])


# intensify: pixel -> nat255 -> pixel
# brighten each channel of pixel by quantity
def intensify(pixel,quantity):
    return (pixel[0]+quantity, pixel[1]+quantity, pixel[2]+quantity)


def invert(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]

    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = inverse(pixels3d[x,y])

def bw(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]

    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = grayPixel(pixels3d[x,y])

def ifadd(x,y):
    if x + y > 255:
        return(255)
    else:
        return(x+y)

def ifsub(x,y):
    if x - y < 0:
        return(0)
    else:
        return(x-y)


def brightenPixel(pixel):
    red_intensity = pixel[0]
    green_intensity = pixel[1]
    blue_intensity = pixel[2]
    return (ifadd(red_intensity,10) , ifadd(green_intensity,10), ifadd(blue_intensity,10))

def darkenPixel(pixel):
    red_intensity = pixel[0]
    green_intensity = pixel[1]
    blue_intensity = pixel[2]
    return (ifsub(red_intensity,10) , ifsub(green_intensity,10), ifsub(blue_intensity,10))

def brighten(image_surf):
        # get pixel dimensions of image
        rows = image_surf.get_size()[0]
        cols = image_surf.get_size()[1]

        # get reference to and lock pixel array
        pixels3d = pg.surfarray.pixels3d(image_surf)

        # update pixels in place (side effect!)
        for x in range(rows):
            for y in range(cols):
                pixels3d[x,y] = brightenPixel(pixels3d[x,y])

def darken(image_surf):
        # get pixel dimensions of image
        rows = image_surf.get_size()[0]
        cols = image_surf.get_size()[1]

        # get reference to and lock pixel array
        pixels3d = pg.surfarray.pixels3d(image_surf)

        # update pixels in place (side effect!)
        for x in range(rows):
            for y in range(cols):
                pixels3d[x,y] = darkenPixel(pixels3d[x,y])
