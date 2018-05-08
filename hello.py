from splashkit import *

my_window=open_window("Hello world", 800, 600)
x=400
y=300
while window_close_requested(my_window) == False:
    print('Hey here')
    process_events()
    clear_screen(color_white())
    fill_circle(color_tomato(), x, y, 100)
    refresh_window(my_window)
    if 510>=y>=110:
        if key_down(KeyCode.up_key) == True:
        
           
           y-=10
        
            
    if 90<=y<=490:
        if key_down(KeyCode.down_key) == True:
        
    
            y+=10
        
    
    if 110<=x<=710:
        if key_down(KeyCode.left_key) == True:
        
     
 
            x-=10
            
 
    if 90<=x<=690:
        if key_down(KeyCode.right_key) == True:
        
            
            x+=10
        
 
        
    
        
        
