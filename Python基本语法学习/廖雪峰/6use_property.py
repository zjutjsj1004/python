#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            print('score must be an integer!')
        if value < 0 or value > 100:
            print('score must between 0 ~ 100!')
        self._score = value

    @property
    def testXXX(self):
        return self._testNum
    @testXXX.setter
    def setTestXXX(self, value):
        if not isinstance(value, int):
            print("invalid param")
            self._testNum = 0
            return
        elif value > 10:
            print("param is too small")
        else:
            print("param is too small")
        
        self._testNum = value

s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
s.score = 9999

s.setTestXXX = 3
print('s.score =', s.setTestXXX)


#看到：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000