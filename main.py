#by: Jorge Kenned Ferreira dos Santos (but call only kenned :) )
#posted on: 12/01/2022
#-----------------
#-----------
#-----
#-

#imports-------------------------------------
import random
import time
import pygame
import thorpy

#function to draw the list
def drawListOnSurface(ds,numbers_list):
    #clear surface
    #try comment this and run :)
    ds.fill((13,17,23))

    #loop to get all elements
    for i in range(len(numbers_list)):
        #draw on surface
        #to gradient effect you need only increase 
        #one of variables (or two) R,G,B
        pygame.draw.rect(ds, (i/num_of_lines*255,150,200), (i, 0, 1, numbers_list[i]))


#function that iterate on list
def iterateBubbleSort(numbers_list):
    #control variable
    is_sorted = True

    #loop from 0 to size of list
    for i in range(len(numbers_list)):
        #avoid infinity loop because python allows negative index
        if i<len(numbers_list)-1:

            #the main logic of bubble sort
            #if number in n position is
            #greater than next we swap they
            if numbers_list[i] > numbers_list[i+1]:
                #setting control variable
                is_sorted=False
                #swapping
                numbers_list[i+1], numbers_list[i] = numbers_list[i], numbers_list[i+1]
        
    #returning the control variable and the list iterate
    return is_sorted,numbers_list

#starting pygame-------------------------------------
pygame.init()
timer = time.time()
#size of screen
#num_of_lines is used on visualization so if you
#modify this too will change on visualization
num_of_lines = 480
#making the screen
ds = pygame.display.set_mode((num_of_lines, num_of_lines))
#changing title of screen
pygame.display.set_caption("Bubble Sort Visualization")

#constanst---------------------------------------------
OFFSET=10

#variables---------------------------------------------
numbers_list = list(range(num_of_lines))
#randon list
random.shuffle(numbers_list)
#control variable to check if list is already sorted
list_is_sort = False
#control variable to save num of iteration
n_iterations = 0
is_running = True

#thorpy elements---------------------------------------
speed_slider = thorpy.SliderX(100, (5, 220), "Visualization speed:", type_=int)
iteration_text = thorpy.OneLineText("Number of iterations on list: "+str(n_iterations))
note_text = thorpy.OneLineText("Note: this not represent the efficiency of bubble sort")
note_text1 = thorpy.OneLineText("is only to fix concepts and example for who needs")

#making box to all gui elements
box = thorpy.Box(elements=[speed_slider,
                        iteration_text,
                        note_text,
                        note_text1,])

#making menu for box
menu = thorpy.Menu(box)

#seting surface
for element in menu.get_population():
    element.surface = ds

#setting position of box
box.set_topleft((OFFSET,num_of_lines-box.get_size()[1]-OFFSET))

#main loop
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quit 
            is_running=False
        
        #adding events observer to thorpy menu
        menu.react(event)

    #verifying if the list is already sort
    if not list_is_sort:
        #case not add one to iteration control variable
        n_iterations+=1
        #iterate again
        list_is_sort,numbers_list = iterateBubbleSort(numbers_list)
        #draw
        drawListOnSurface(ds,numbers_list)

    #setting iteration text of gui
    iteration_text.set_text("Number of iterations on list: "+str(n_iterations))
    #draw and updating thorpy
    box.blit()
    box.update()

    #setting fps of visualization
    pygame.time.Clock().tick(speed_slider.get_value())
    #updating pygame screen
    pygame.display.update()
