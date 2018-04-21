# File: Class_Buffer_in_Python.py
# Description: Creating class Buffer in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Class Buffer in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Class_Buffer_in_Python (date of access: XX.XX.XXXX)


# Implementing the task
# Creating class Buffer
# Adding to the buffer numbers
# Saving in the buffer only < 5 numbers
# Printing the sum of sequence of 5 numbers

# Creating the class Buffer:
class Buffer:
    # Constructor of the class
    def __init__(self):
        # Creating list to store the current sequence but not longer then 5 elements
        self.lst = []
          
    # Adding the sequence of numbers:
    def add(self, *args):
        # Going through all elements of the tuple *args
        for i in range(len(args)):
            # Adding elements to the list till it has 5
            if len(self.lst) < 5:
                self.lst += [args[i]]
            # Printing sum of the 5 elements and clearing the list
            if len(self.lst) == 5:
                print(sum(self.lst))
                self.lst = []
        
    # Returning the currently saved elements of the sequence
    def get_current_part(self):
        return self.lst

# Showing the results
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()  # show [1, 2, 3]
buf.add(4, 5, 6)  # print 15 
buf.get_current_part()  # Show [6]
buf.add(7, 8, 9, 10)  # print(40)
buf.get_current_part()  # Show []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print 5 and again print 5
buf.get_current_part()  # Show [1]
