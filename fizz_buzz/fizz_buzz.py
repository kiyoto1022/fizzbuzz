#!/usr/bin/env python
# -*- coding: utf-8 -*-

class FizzBuzz:

    _DEFAULT_SEPARATE = "\n"

    def __init__(self, stop):
        self.__stop = stop
        self.__separate = self._DEFAULT_SEPARATE

    def __is_fizz(self, num):
        if num % 3 == 0:
            return True
        return False

    def __is_buzz(self, num):
        if num % 5 == 0:
            return True
        return False

    def __is_fizz_buzz(self, num):
        if self.__is_fizz(num) and self.__is_buzz(num):
            return True
        return False

    def __judge(self, num):
        if self.__is_fizz_buzz(num):
            return "FizzBuzz"
        if self.__is_fizz(num):
            return "Fizz"
        if self.__is_buzz(num):
            return "Buzz"
        return str(num)

    def set_separate(self, separate):
        self.__separate = separate

    def say(self):
        say = ""
        for i in range(int(self.__stop)):
            answer = self.__judge(i + 1)
            say += answer + self.__separate
        return say