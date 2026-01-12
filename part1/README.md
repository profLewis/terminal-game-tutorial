# PART 1: Starting out with ncurses

### 1.1: A brief introduction of everything

This project is based on the terminal game tutorial of fundamelon
, fundamelon/terminal-game-tutorial in c++, translated to Python using the blessed library.

It requires the Python library `blessed`, so let's check you have that:

Open a terminal, iand at the prompt type:

```
python -c 'from blessed import Terminal;print("hello world")'
```

If this fails, it will say something like:

`ModuleNotFoundError: No module named 'blessed'`

and you should then install the library. Most commonly, this involves you downloading and installing using `pip`, by typing at the prompt:

```
pip install blessed
```

i
### 1.2: Getting comfortable in our format
This project will follow a standard structure which you should already be familiar with.
Let's start by creating a file, main01.py:

```python
from blessed import Terminal
```

Note the inclusion of the library ``blessed.  
This is required to use the features we will rely on later.

Try to `make` the project now. 
If you encounter an error related to the library, this probably means it's not installed.
You'll need to run `sudo apt-get install libncurses5-dev` (or the latest compatible version) to get it on your machine.  

*note to ucr students on hammer: this may not compile with cs100 settings active*


### 1.3: Getting started with ncurses

Adding the following code to our main function:
```c++
    initscr();
    cbreak();
    noecho();
    clear();
    refresh();

    while(1);
```
and compiling + running `bin/main` results in a blank screen.  Here we see several important effects:
- keyboard buttons pressed are not output to the screen
- ending the program with ctrl-c returns the terminal to its previous state

This is important because a simple call such as printf("\033c") or system("clear") would modify the terminal and its history - but here, ncurses takes control and reserves it for us.
See [here](http://hughm.cs.ukzn.ac.za/~murrellh/os/notes/ncurses.html#init)
and [here](http://tldp.org/HOWTO/NCURSES-Programming-HOWTO/helloworld.html)
for detailed explanations of these functions.

We are now ready for our obligatory "Hello World"!

### 1.4: Hello terminal

Before our infinite loop, we add this code to the main:
```c++
move(5, 5);

std::string text = "Hello world!";
for(int i = 0; i < text.size(); i++) {
    addch(text[i]);
    addch(' ');
}

refresh();
```

The `move(5, 5)` command moves the cursor to the specified ```(y, x)``` position.
Remember, curses is built entirely on this character-oriented coordinate system.

Next, a simple for loop will invoke `addch()`twice - once to print the text char, and once to print a space.  
`addch()` will print a character at the current cursor position, and advance it by 1 space.

*Don't forget to `include <string>`!*

Finally, it is important to call `refresh()` whenever any changes made should show up on the screen.
Any changes using curses will not show up until you call this function.


#### Final product

![final product](.img/part1_4.gif)

We are now ready to start building our game!  
[Part 2](../part2) of the tutorial series deals with the basic structure of our project.



This folder contains all project files for part 1.
