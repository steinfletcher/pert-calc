pert-calc
=========

A command line utility for quick 'n dirty PERT estimates

Usage:

     pert --tasks="1,2,4 5,7,11 7,11,22"

which calculates the total duration (including risk) of 3 tasks

     task1: optimistic: 1, nominal: 2, pessimistic: 4
     task2: optimistic: 5, nominal: 7, pessimistic: 11
     task3: optimistic: 7, nominal: 11, pessimistic: 22
