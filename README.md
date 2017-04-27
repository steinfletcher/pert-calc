pert-calc
=========

A command line utility for quick 'n dirty PERT estimates. Depends on python 2

Usage:

     pert --tasks="1,2,4 5,7,11 7,11,22"

which calculates the total duration (including risk) of 3 tasks

     task1: optimistic: 1, nominal: 2, pessimistic: 4
     task2: optimistic: 5, nominal: 7, pessimistic: 11
     task3: optimistic: 7, nominal: 11, pessimistic: 22

and produces the following output

     [1: (O:1.0), (N:2.0),  (P:4.0)]  | duration: 2.17,  risk: 0.5
     [2: (O:5.0), (N:7.0),  (P:11.0)] | duration: 7.33,  risk: 1.0
     [3: (O:7.0), (N:11.0), (P:22.0)] | duration: 12.17, risk: 2.5
     Final estimate: 24.41
