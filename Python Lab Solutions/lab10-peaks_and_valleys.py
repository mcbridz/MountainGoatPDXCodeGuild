#filename: lab10-peaks_and_valleys.py
#author: Zachary McBride

# Define the following functions:
#     peaks(data) -   Returns the indices of peaks. A peak has a lower number on both 
#                     the left and the right.
#     valleys(data) - Returns the indices of 'valleys'. A valley is a number with a 
#                     higher number on both the left and the right.
#     peaks_and_valleys(data) - uses the above two functions to compile a single list  
#                of the peaks and valleys in order of appearance in the original data.

# Using the data list above, draw the image of X's above.

# Hint 1: If you wanted to draw this horizontally, you could do so very easily like this.

# Imagine pouring water into onto these hills. 
# The water would wash off the left and right sides, but would accumulate in the valleys. 
# Below the water is represented by O's. Given data, calculate the amount of water that 
# would be collected, and if you can, draw the following diagram.

# reduces redundant coding and prevent inadvertent range generation
# input is a list of height(integers)
# output is a range object that buffers the ends of the list
def truncated_range(data):
    return range(1, len(data) - 1)

# function to return the number of peaks (highest integer height)
# of a list of integers. Output is a list of indices of the input
# list
def peaks(data):
    peaks = []
    for i in truncated_range(data):
        if data[i] > data[i + 1] and data[i] > data[i - 1]:  # data[i-1] < data[i] > data[i+1]
            peaks.append(i)
    #print(peaks)
    return peaks

# function to return the number of vallies (lowest integer height)
# of a list of integers. Output is a list of indices of the input
# list
def valleys(data):
    valleys = []
    for i in truncated_range(data):
        if data[i] < data[i + 1] and data[i] < data[i - 1]:
            valleys.append(i)
    #print(valleys)
    return valleys

# function to return a combined list of peaks and valleys
def peaks_and_valleys(data):
    return peaks(data) + valleys(data)

# function to develop spaces to be added to a print statement
# between mountain sides
def space_buffer(index_a, index_b):
    # if index_a == 0 and index_b == 1:
    #     return '  '
    # else:
    number_of_empties = index_b - index_a
    number_of_empties -= 1
    return '  '*number_of_empties

# function to find a list of indices from the list-integer-height
# of mountains.  If value at index accessed is larger than the 'n'-
# height of the mountains
def list_of_indices_of_n(n, data):
    output = []
    for i in range(len(data)):
        if data[i] >= n:
            output.append(i)
    #print(output)
    return output

# function to develop water-filled blocks in print statement
# assuming that index_a and index_b are mountain-sides
def water_buffer(index_a, index_b, water_units):
    number_of_empties = index_b - index_a
    number_of_empties -= 1
    water_units[0] += number_of_empties
    return ' 0'*number_of_empties

def draw_mountains(data):
    #find max height
    i = max(data)

    # main loop to cycle from max-height to lowest-height,
    # lowest height will always be 1
    while i > 0:
        #finding the spaces which will be mared with 'X'
        draw_x_at = list_of_indices_of_n(i, data)

        #required to easily determine whether an 'X'
        #has been marked yet. If not, no water to fill
        marked_first_X = False

        #loop using <draw_x_at> list of indices to be marked
        #'X'
        while len(draw_x_at) > 1: #handle look-ahead calls

            #no 'X' marked yet, AND data[0] is not part of
            #the list to be marked
            if not marked_first_X and draw_x_at[0] != 0:
                
                # print: <leading spaces>
                print(space_buffer(0, draw_x_at[0]), end='  ')

                # pull out the index to be used from list
                index_a = draw_x_at.pop(0)

                #print 'X' then following spaces to the next index
                print('X' + space_buffer(index_a, draw_x_at[0]), end=' ')
                marked_first_X = True
            
            #data[0] is not in the list of indices to be marked
            elif draw_x_at[0] != 0:
                index_a = draw_x_at.pop(0)
                print('X' + space_buffer(index_a, draw_x_at[0]), end=' ')

            #no 'X' marked yet, and it is the first index
            else:
                index_a = draw_x_at.pop(0)
                print('X' + space_buffer(index_a, draw_x_at[0]), end=' ')
                marked_first_X = True

        #last 'X' index, accounted spacing in above logic
        if not marked_first_X:
            print(space_buffer(0, draw_x_at[0]) + '  X')
        else:
            print('X')
        i -= 1    

def draw_filled_mountains(data):
    #find max height
    i = max(data)

    #track water units, must use list to make it mutable
    water_units = [0]

    # main loop to cycle from max-height to lowest-height,
    # lowest height will always be 1
    while i > 0:
        #finding the spaces which will be mared with 'X'
        draw_x_at = list_of_indices_of_n(i, data)

        #required to easily determine whether an 'X'
        #has been marked yet. If not, no water to fill
        marked_first_X = False

        #loop using <draw_x_at> list of indices to be marked
        #'X'
        while len(draw_x_at) > 1: #handle look-ahead calls

            #no 'X' marked yet, AND data[0] is not part of
            #the list to be marked
            if not marked_first_X and draw_x_at[0] != 0:
                
                # print: <leading spaces>
                print(space_buffer(0, draw_x_at[0]), end='  ')

                # pull out the index to be used from list
                index_a = draw_x_at.pop(0)

                #print 'X' then water filled to the next index
                print('X' + water_buffer(index_a, draw_x_at[0], water_units), end=' ')
                marked_first_X = True

            #data[0] is not in the list of indices to be marked
            #includes filling water between mountains
            elif draw_x_at[0] != 0 and marked_first_X:
                index_a = draw_x_at.pop(0)
                print('X' + water_buffer(index_a, draw_x_at[0], water_units), end=' ')

            #no 'X' marked yet, and it is the first index
            #includes filling water between mountains
            else:
                index_a = draw_x_at.pop(0)
                print('X' + water_buffer(index_a, draw_x_at[0], water_units), end=' ')
                marked_first_X = True
        
        #last 'X' index, accounted spacing in above logic
        if not marked_first_X:
            print(space_buffer(0, draw_x_at[0]) + '  X')
        else:
            print('X')
        i -= 1   
    print(f"{water_units[0]} units of water filled the mountains after a downpour.") 

import random
def generate_mountains(max = 9, min = 1):
    output = []
    for _ in range(20):
        output.append(random.randint(min, max))
    return output




      #                                           X  O  O  O  O  O  X
      #                                        X  X  X  O  O  O  X  X
      #                   X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
      #                X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
      #             X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
      #          X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
      #       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
      #    X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
      # X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
      # 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20
      #                   P        V              P        V
# peaks(data) # [6, 14]
# valleys(data) # [9, 17]
# print(peaks_and_valleys(data)) # [6, 9, 14, 17]
# draw_mountains(data)
# draw_filled_mountains(data)
new_mountains = generate_mountains()
draw_mountains(new_mountains)
draw_filled_mountains(new_mountains)