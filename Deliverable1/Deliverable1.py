import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

#Main function
def main():
    #Using command line to get photo
    if len(sys.argv) != 3:
        print("Usage: python filter1.py input_name output_name")
        sys.exit(1)

    #Read image using OpenCv in colored mode (1 Represents colored mode) 
    
    read = cv2.imread(sys.argv[1], 1)
    
    #Check if file exists
    try:
        if read == None:
            print("File doesn't exist")
            sys.exit(2)
    except:
        print("File exist->")

    #Loop to prevent unkown input
    while 1:
        #Get input from user to choose the filter
        get = input("R=red, B=blue, G=green, G1=grayscale, n=Negative, hf=horozintal flip, vf=Vertical flip:")

        #Cases 
        if get.lower() == 'r':
            read = reddify(read)
            break
        elif get.lower() == 'b':
            read = blueify(read)
            break
        elif get.lower() == 'g':
            read = greenify(read)
            break
        elif get.lower() == "g1":
            read = grayscale(read)
            break
        elif get.lower() == "n":
            read = negative(read)
            break
        elif get.lower() == "hf":
            read = horozintalflip(read)
            break
        elif get.lower() == "vf":
            read = verticalflip(read)
            break
        else:#Loop if unknown input
            print("No such a filter")
    
    #Show image
    #cv2.imshow("filter", read)
    plt.imshow(read)
    plt.show()

    #Wait for keyboard input to stop showing image
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

    #Save image
    cv2.imwrite(sys.argv[2],read)



#All functions depends on numpy 3d-arrays
#Function reddify takes image array, changes each pixel's blue and green to 0 using numpy
def reddify(img):
    img[:,:,0] = 0
    img[:,:,1] = 0
    
    return img 

#Function reddify takes image array, changes each pixel's blue and red to 0 using numpy
def greenify(img):
    img[:,:,0] = 0
    img[:,:,2] = 0

    return img 

#Function reddify takes image array, changes each pixel's red and green to 0 using numpy
def blueify(img):
    img[:,:,1] = 0
    img[:,:,2] = 0

    return img 

#Function grayscale takes image array, changes each pixel rgb using weighted method
def grayscale(img):
    img[:,:,0] = img[:,:,0] * 0.1140 + img[:,:,1] * 0.5870 + img[:,:,2] * 0.2989
    img[:,:,1] = img[:,:,0] * 0.1140 + img[:,:,1] * 0.5870 + img[:,:,2] * 0.2989
    img[:,:,2] = img[:,:,0] * 0.1140 + img[:,:,1] * 0.5870 + img[:,:,2] * 0.2989

    return img 

#Function negative takes image array, changes each pixel rgb to 255 - value
def negative(img):
    img[:,:,0] = 255 - img[:,:,0]
    img[:,:,1] = 255 - img[:,:,1]
    img[:,:,2] = 255 - img[:,:,2]

    return img 

#Function vertical flop is used to reflect image over x-axis by swaping rows
def verticalflip(img):
    #helper is used to swap rows
    helper = img
    x = 0
    y = img.shape[0] - 1 
    while x < y:
        helper[0,:,:] = img[x,:,:]
        img[x,:,:] = img[y,:,:]
        img[y,:,:] = helper[0,:,:]
        x += 1          
        y -= 1

    return img

#Function vertical flop is used to reflect image over y-axis by swaping columns
def horozintalflip(img):
    #helper is used to swap columns
    helper = img
    x = 0
    y = img.shape[1] - 1 
    while x < y:
        helper[:, 0, :] = img[:,x,:]
        img[:,x,:] = img[:,y,:]
        img[:,y,:] = helper[:,0,:]
        x += 1          
        y -= 1

    return img

#Run main
main()