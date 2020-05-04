from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import pygame


def change():
    pass


main_form = Tk()
main_form.title('')

photo = ImageTk.PhotoImage(Image.open('Bg.jpg'))
w = photo.width()    #626
h = photo.height()   #469
bag_photo = Label(main_form, image=photo, bd=0)
bag_photo.pack()

main_form.geometry('%dx%d+0+0' % (w, h))  # Размер окна
main_form.resizable(False, False)  # Окно нельзя растягивать

button_1 = tk.Button(main_form, text='НАЧАТЬ ИГРУ')
button_2 = tk.Button(main_form, text='ЗАГРУЗИТЬ ИГРУ')
button_3 = tk.Button(main_form, text='ВЫХОД ИЗ ИГРЫ', command=main_form.quit)

button_1.place(x=(w / 2) - 48, y=(h / 2) + 50)
button_2.place(x=(w / 2) - 49, y=(h / 2) + 78)
button_3.place(x=(w / 2) - 48, y=(h / 2) + 112)

walkRight = [pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_00.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_01.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_02.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_03.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_04.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_05.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_06.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_07.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_08.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_09.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_010.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_011.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_012.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_013.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_014.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_015.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_016.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_017.png')]
walkLeft = [pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_00.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_01.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_02.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_03.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_04.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_05.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_06.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_07.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_08.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_09.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_010.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_011.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_012.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_013.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_014.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_015.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_016.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_017.png')]
idle = pygame.image.load('sprites\Golem_Braun\idle\Idle_0.png')

main_form.mainloop()
