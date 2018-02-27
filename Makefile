CC = python

start:  eightpuzzle.py
  $(CC) eightpuzzle.py -o start

clean:
  \rm start *.o
