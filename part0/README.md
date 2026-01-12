# PART 1: Starting out with ncurses

### 1.1: A brief introduction of everything

This project is based on the terminal game tutorial of fundamelon
, fundamelon/terminal-game-tutorial in c++, translated to Python using the blessed library.

### 1.2: Testing for `blessed`

These tutorials requires the Python library `blessed` for a simple interface to text-based screen coding, so let's check you have that:

Open a terminal:

![image](images/img0000.png)

and at the prompt type:

```
python -c 'from blessed import Terminal;print("hello world")'
```

If this is ok, it will print "hello world" in the terminal.

![image](images/img0001.png)


If this fails, it will report something like:

`ModuleNotFoundError: No module named 'blessed'`

and you should then install the library. 

### 1.3: Install `blessed`

If you need to, install the `blessed` library. You should not proceed if you have not got this working.

Most commonly, this involves you downloading and installing using `pip`, by typing at the prompt:

```
pip install blessed
```

If this responds with `Requirement already satisfiedi: blessed`, then you already have it installed, but no harm done.

In any case, make sure yiu confirm, running the test you did before:

```
python -c 'from blessed import Terminal;print("hello world")'
```

If thats all good, then you can start learning how to write simple games in Python with `blessed`.
