from splashkit import *

my_window=open_window("Hello world", 900, 700)
x=window_width(my_window)/2
y=window_height(my_window)/2
while window_close_requested(my_window) == False:
    print('Hey here')
    process_events()
    clear_screen(color_white())
    fill_circle(color_tomato(), x, y, 100)
    refresh_window(my_window)
    if window_height(my_window)-90>=y>=110:
        if key_down(KeyCode.up_key) == True:
            y-=10
    if 90<=y<=window_height(my_window)-110:
        if key_down(KeyCode.down_key) == True:
            y+=10
    if 110<=x<=window_width(my_window)-90:
        if key_down(KeyCode.left_key) == True:
            x-=10
    if 90<=x<=window_width(my_window)-110:
        if key_down(KeyCode.right_key) == True:
            x+=10
        
 
        
    
        
        
