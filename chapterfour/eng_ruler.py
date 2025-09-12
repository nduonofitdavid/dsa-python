def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

    
draw_ruler(4, 4)

# study the khan academy precalculus series videos which covers mathematical induction to understand justification
# by induction.

"""
What this code does, is to use the recursive approach to draw an english ruler
you start out by giving it the  major length and the number of inches you want do draw.

The first thing is does is to draw the marker for zero, which will be the start of the ruler,
then it uses a for loop to loop and for the number of inches, draw their interval and then draw a line

now the magic lies in drawing the intervals. remember from the picture of the english ruler, that the intervals followed the format of

L - 1
L
L - 1

so we start with the center length, the center length will always be the value of the major length minus 1 as it indicates half of an inch
so we call the draw_interval function and pass in major_length -1, after passing in major length - 1, 
inside the draw_interval function, we check if the value of the value passed in is greater than zero, if it is, we then follow the format in which the english ruler follows

we draw an interval for l - 1 by calling draw_interval on the center tick length - 1
then we draw the length of the central tick
then we repeat step 1, since recursion stops the execution of the current function till the previous has been called, hence when we pass in say 4 as the major tick length, this
subtracts 1 from it, and we then have 3, so we call draw_interval on 3 - 1, which in turn calls on 2 - 1, which in turn calls on 1 - 1, when the contition for the recursive call has been breached, execution is returned to the previous function call,
and after all that we have the intervals

then in the body of the for loop of the draw_ruler call, we draw the line signifying the major_inch length.
"""