'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 - 32 - 13 - 10 - 1 - 1
85 - 89 - 145 - 42 - 20 - 4 - 16 - 37 - 58 - 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''
import math
from time import sleep 

# calculate next nr in the chain
def calc_next(nr):
  str_from_nr=str(nr)
  next_nr=0
  for i in range(len(str_from_nr)):
    figure=int(str_from_nr[i])
    next_nr=next_nr+(figure*figure)
  return next_nr

def main():
  count=0
  next_nr=0
  for i in range(1,10000000):
    next_nr=calc_next(i)
    #print i,
    while (next_nr != 1) and (next_nr != 89) :
      #print next_nr,
      next_nr=calc_next(next_nr)
      #sleep(1)
    #print next_nr
    if next_nr == 89 : count+=1
  print count


if __name__ == "__main__":
  main()