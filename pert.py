#!/usr/bin/env python

# copyright (c) 2014 Stein Fletcher <steinfletcher@gmail.com>
#
# Purpose: A simple utility to estimate tasks using PERT
# Usage:
#    pert --tasks="1,2,4 5,7,11 7,11,22"
#
# which calculates the total duration (including risk) of 3 tasks
#     task1: optimistic: 1, nominal: 2, pessimistic: 4
#     task2: optimistic: 5, nominal: 7, pessimistic: 11
#     task3: optimistic: 7, nominal: 11, pessimistic: 22

from math import pow, sqrt
import argparse


class Task(object):
    def __init__(self, opt, nom, pes):
        self.opt = opt
        self.nom = nom
        self.pes = pes


class Estimation:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_duration(self):
        return Calculator.total_duration(self.tasks)

    def get_uncertainty(self):
        return Calculator.total_uncertainty(self.tasks)

    def get_estimate(self):
        return Calculator.estimate(self.tasks)

    def print_report(self):
        for index, task in enumerate(self.tasks):
            print "[{0}: (O:{1}), (N:{2}), (P:{3})] | duration: {4}, risk: {5}".format(
                  index + 1
                , task.opt
                , task.nom
                , task.pes
                , round(Calculator.expected_duration(task), 2)
                , round(Calculator.uncertainty(task), 2)
            )
        print "Final estimate: {}".format(round(self.get_estimate(), 2))


class Calculator(object):

    @staticmethod
    def estimate(tasks):
        return (Calculator.total_duration(tasks) +
                Calculator.total_uncertainty(tasks))

    @staticmethod
    def total_duration(tasks):
        return sum([Calculator.expected_duration(task) for task in tasks])

    @staticmethod
    def total_uncertainty(tasks):
        return sqrt(sum([pow(Calculator.uncertainty(task), 2) for task in tasks]))

    @staticmethod
    def expected_duration(task):
        return (task.opt + 4*task.nom + task.pes) / 6

    @staticmethod
    def uncertainty(task):
        return (task.pes - task.opt) / 6


def main():

    def validate_params(params):
        task_list = params['tasks'].split()
        if len(task_list) < 1:
            print "No tasks specified"
            parser.print_help()
            exit(255)
        for element in task_list:
            element_params = element.split(',')
            if len(element_params) != 3:
                print "Invalid number of task attributes"
                parser.print_help()
                exit(255)
        return task_list

    parser = argparse.ArgumentParser(description='A command line PERT calculator for quick \'n dirty estimates')
    parser.add_argument(
        '--tasks',
        help='a comma separated task list in the form "1,2,12 4,5,9 2,3,6", where whitespace separates tasks',
        required=True)
    args = vars(parser.parse_args())
    tasks = validate_params(args)
    estimation = Estimation()
    for task in tasks:
        attrs = [float(val) for val in task.split(',')]
        t = Task(opt=attrs[0], nom=attrs[1], pes=attrs[2])
        estimation.add_task(t)

    estimation.print_report()


if __name__ == '__main__':
    main()
