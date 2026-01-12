#!/usr/bin/env python

from blessed import Terminal

# set up terminal object, and initialise
term = Terminal()

term.home()
 
# loop
while True:
    print(term.clear()+ term.move(5,5))
    print('hello world',end='')

