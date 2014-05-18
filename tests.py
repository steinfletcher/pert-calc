#!/usr/bin/env python

import unittest
from pert import *


class TestPertCalculator(unittest.TestCase):
    def setUp(self):
        self.task1 = Task(opt=1.0, nom=3.0, pes=12.0)
        self.task2 = Task(opt=1.0, nom=1.5, pes=14.0)
        self.task3 = Task(opt=3.0, nom=6.25, pes=11.0)
        self.tasks = [self.task1, self.task2, self.task3]

    def test_duration(self):
        self.assertEqual(
            round(Calculator.expected_duration(self.task1), 2),
            4.17
        )

        self.assertEqual(
            round(Calculator.expected_duration(self.task2), 2),
            3.5
        )

        self.assertEqual(
            round(Calculator.expected_duration(
                self.task3), 2),
            6.5
        )

    def test_uncertainty(self):
        self.assertEqual(
            round(Calculator.uncertainty(self.task1), 2),
            1.83
        )

        self.assertEqual(
            round(Calculator.uncertainty(self.task2), 2),
            2.17
        )

        self.assertEqual(
            round(Calculator.uncertainty(self.task3), 2),
            1.33
        )

    def test_total_duration(self):
        self.assertEqual(
            round(Calculator.total_duration(self.tasks), 2),
            14.17
        )

    def test_total_uncertainty(self):
        self.assertEqual(
            round(Calculator.total_uncertainty(self.tasks), 2),
            3.14
        )


if __name__ == '__main__':
    unittest.main()
