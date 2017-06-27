import unittest
from fizz_buzz.fizz_buzz import *

class TestFizzBuzz(unittest.TestCase):

    def test_fizz(self):
        fizz_buzz = FizzBuzz(3)
        fizz_buzz.set_separate("")
        self.assertEqual("12Fizz", fizz_buzz.say())

    def test_buzz(self):
        fizz_buzz = FizzBuzz(5)
        fizz_buzz.set_separate("")
        self.assertEqual("12Fizz4Buzz", fizz_buzz.say())

    def test_fizz_buzz(self):
        fizz_buzz = FizzBuzz(15)
        fizz_buzz.set_separate("")
        self.assertEqual("12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz", fizz_buzz.say())

if __name__ == '__main__':
    unittest.main()