#!/usr/bin/env python

from blessed import Terminal

def main():
    # set up terminal object, and initialise
    term = Terminal()
    term.home()
 
    # loop
    while True:
        print(term.clear()+ term.move(5,5) + f'hello world')

if __name__ == "__main__":
    main()
