#!/usr/bin/python3

"""
This is the 100-my_int.py
"""

class MyInt(int):
    
    def __init__(self, value):
        
        self.num = value
        

        
    def __eq__(self, other):
        
        return self.num != other
    

    
    def __ne__(self, other):
        
        return self.num == other
