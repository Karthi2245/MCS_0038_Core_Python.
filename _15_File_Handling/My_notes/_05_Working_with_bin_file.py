'''
--> binary Files handle the data in the form of bytes.
--> they can be used to read and write text, images, audio, video files.
--> read binary : 'rb' mode
--> Write binary: 'wb' mode
--> to open use open() method
--> to write use write() method
'''
# program to copy an image file into another file:
img1 = open("C:\\Users\\Iswarya\\Downloads\\bike.jpg", 'rb')
img2 = open("C:\\Users\\Iswarya\\Downloads\\bike2.jpg", 'wb')
bytes = img1.read()
img2.write(bytes)
img1.close()
img2.close()


