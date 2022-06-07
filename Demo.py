#! /home/dai/anaconda2/envs/py27/bin/python
import  Tkinter as tk
from FileDialog import *
from PIL import Image
from PIL import ImageTk
import io
import tkFileDialog
import os
import shutil                   #import some modules about file operations

def image_select_move():                                                                            #slect a picture and move it to the test folder at the same time rename it
    image_filepath_tuple = tkFileDialog.askopenfilename()           #the data type of return is a tuple,so we need convert it to string
    image_filepath = ''.join(image_filepath_tuple)                              #convert tuple to string so that shuil.copy can work
    new_path = './dataset/GAIC/images/test/000.jpg'                  #all images needed to be cropped needs to be put in the test folder
    shutil.copy(image_filepath,new_path)                                                                                                #copy the image you have selected to the test folder

def clear_all_pictures():                                                                                #clear all pictures in the test folder before run a new image cropping program
    shutil.rmtree("./dataset/GAIC/images/test")                             #remove the test folder
    os.mkdir("./dataset/GAIC/images/test")                                      #rebuild a new test folder to save the image you have selected

def clear_result_pictures():                                                                               
    if os.path.exists("./dataset/test_result"):
        shutil.rmtree("./dataset/test_result")                       
        os.mkdir("./dataset/test_result") 
    else:
        os.mkdir("./dataset/test_result") 

def run_demo_eval():
    os.system("python ./demo_eval.py")                   #run the demo_eval.py to process the image you have selected, it needs 40 to 50  seconds to finish it.

def resize( w_box, h_box, pil_image):                       #to make the picture fit the window size
  w, h = pil_image.size
  f1 = 1.0*w_box/w 
  f2 = 1.0*h_box/h    
  factor = min([f1, f2])   
  width = int(w*factor)    
  height = int(h*factor)    
  return pil_image.resize((width, height), Image.ANTIALIAS) 

def show_image():                                       #show the image you have selected on the lable
    global photo
    img = Image.open('./dataset/GAIC/images/test/000.jpg')
    photo_resized = resize(700,500,img)
    photo = ImageTk.PhotoImage(photo_resized)
    img_label = tk.Label(root_window,relief='sunken',image=photo,width='700',height='500')
    img_label.place(x=50,y=100)

def show_image0():
    global photo0
    img0 = Image.open('./dataset/test_result/000_0.jpg')
    photo0_resized = resize(700,500,img0)
    photo0 = ImageTk.PhotoImage(photo0_resized)
    img0_label = tk.Label(root_window,relief='sunken',image=photo0,width='700',height='500')
    img0_label.place(x=850,y=100)

def show_image1():
    global photo1
    img1 = Image.open('./dataset/test_result/000_1.jpg')
    photo1_resized = resize(700,500,img1)
    photo1 = ImageTk.PhotoImage(photo1_resized)
    img1_label = tk.Label(root_window,relief='sunken',image=photo1,width='700',height='500')
    img1_label.place(x=850,y=100)

def show_image2():
    global photo2
    img2 = Image.open('./dataset/test_result/000_2.jpg')
    photo2_resized = resize(700,500,img2)
    photo2 = ImageTk.PhotoImage(photo2_resized)
    img2_label = tk.Label(root_window,relief='sunken',image=photo2,width='700',height='500')
    img2_label.place(x=850,y=100)

def show_image3():
    global photo3
    img3 = Image.open('./dataset/test_result/000_3.jpg')
    photo3_resized = resize(700,500,img3)
    photo3 = ImageTk.PhotoImage(photo3_resized)
    img3_label = tk.Label(root_window,relief='sunken',image=photo3,width='700',height='500')
    img3_label.place(x=850,y=100)                                                                                                                                   #show image0-image3 that have been cropped

def show_image_0():
    img = Image.open('./dataset/GAIC/images/test/000.jpg')
    img.show()

def show_image_1():
    img = Image.open('./dataset/test_result/000_0.jpg')
    img.show()

def show_image_2():
    img = Image.open('./dataset/test_result/000_1.jpg')
    img.show()

def show_image_3():
    img = Image.open('./dataset/test_result/000_2.jpg')
    img.show()

def show_image_4():
    img = Image.open('./dataset/test_result/000_3.jpg')
    img.show()

root_window =tk.Tk()                                        #make a blank window
root_window.title('Image Cropping Based On Deep Learninig')              #name the blank window with 'Image Cropping Based on Deep Learning'
root_window.geometry('1600x900')            #set the window size

text1=tk.Label(root_window,text="(Wait the 'Crop' button turns green, about 40 seconds!)\nClick Image0~Image3 to view images cropped well.\nClick O_Image0~O_Image3 to view theirs original images. ",relief='sunken',font=('Times','10','bold'),bg='white',width='100',height='5')
text1.place(x=850,y=800)                                #create a label

text2=tk.Label(root_window,text="Click 'Select an image' to select an image from your computer.\nClick 'View the original image' to view its original image.\nClick the green 'Crop' button to crop the image!",relief='sunken',font=('Times','10','bold'),bg='white',width='100',height='5')
text2.place(x=50,y=800)                                #create a label

text3=tk.Label(root_window,text="Welcome to the Image Cropping System based on Deep Learning!",relief='sunken',font=('Times','20','bold'),width='70',height='2',bg='alice blue')
text3.place(x=320,y=20)

text4=tk.Label(root_window,text="GUI designed by Dai",font=('Times','10','bold'),bg='ivory')
text4.place(x=1460,y=880)

clear_all_pictures()                                  #clear the test folder
clear_result_pictures()                            #clear the test_result folder

button1=tk.Button(root_window,text="Select an image",bg='lightblue',width='61',height='3',relief='raised',font=('Arial','13',"bold"),command=lambda:[image_select_move(),show_image()])
button1.place(x=50,y=630)

button1_0 = tk.Button(root_window,text="View the original image",bg='lightyellow',width='61',height='3',relief='raised',font=('Arial','13',"bold"),command=show_image_0)
button1_0.place(x=50,y=700)

button2=tk.Button(root_window,text="Crop",bg='SpringGreen',width='4',height='8',relief='raised',font=('Arial','20',"bold"),command=run_demo_eval)
button2.place(x=758,y=250)

button3=tk.Button(root_window,text="Image0",bg='NavajoWhite',width='10',height='3',relief='raised',font=('Times','15',"bold"),command=show_image0)
button3.place(x=850,y=630)

button3_0=tk.Button(root_window,text="O_Image0",bg='PaleGoldenrod',width='10',height='3',relief='raised',font=('Times','15',"bold"),command=show_image_1)
button3_0.place(x=850,y=700)

button4=tk.Button(root_window,text="Image1",bg='NavajoWhite',width='10',height='3',relief='raised',font=('Times','15',"bold"),command=show_image1)
button4.place(x=1040,y=630)

button4_0=tk.Button(root_window,text="O_Image1",bg='PaleGoldenrod',width='10',height='3',relief='raised',font=('Times','15',"bold"),command=show_image_2)
button4_0.place(x=1040,y=700)

button5=tk.Button(root_window,text="Image2",bg='NavajoWhite',width='10',height='3',relief='raised',font=('Times','15',"bold"),command=show_image2)
button5.place(x=1230,y=630)

button5_0=tk.Button(root_window,text="O_Image2",bg='PaleGoldenrod',width='10',height='3',relief='raised',font=('Times','15',"bold"),command=show_image_3)
button5_0.place(x=1230,y=700)

button6=tk.Button(root_window,text="Image3",bg='NavajoWhite',width='10',height='3',relief='raised',font=('Times','15',"bold"),command=show_image3)               #create some buttons
button6.place(x=1420,y=630)

button6_0=tk.Button(root_window,text="O_Image3",bg='PaleGoldenrod',width='10',height='3',relief='raised',font=('Times','15',"bold"),command=show_image_4)
button6_0.place(x=1420,y=700)

root_window.mainloop()          #make the window into a endless loop so that it can display on the screen