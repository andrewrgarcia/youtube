# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 22:17:53 2019

@author: garci
"""

'''random seed ---> starting pt. for a random number sequence
computers do not generate TRUE rn 
pseudo rn (PRNGs) algorithms --> deterministic ---> python: Mersenne Twister (read)

python: always seeds after it runs something [system time?]

why seeding? 

example -- encryption --> making passwords [a series of] 
    lets get specific!
        make 50 passwords
            *10 character long "random" 
                
            alphanumeric
            
            '''
import numpy.random as ran
from sty import fg, bg, ef, rs

fg.crimson = ('rgb', (220, 20, 60))
fg.deepskyblue1 = ('rgb', (0,191,255))

def keygen(N=100):

    box = N*[''] 
    charno = 10
    
    letter = 'qwertyuiopasdfghjklzxcvbnm'
    LETTER = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    nos = '1234567890'
    special = '!@#$%^&r*()_+~'


    string = letter + LETTER + 5*nos + 3*special
    
    for i in range(N):
        k=0
        while k < charno:
            box[i] = box[i] + string[ran.randint(0,140)]
            k+=1
#        print (fg.crimson + box[i] +fg.rs)
    return box
#
#keygen()
print(keygen())


            
            
            