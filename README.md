# fizzbuzz

Enjoy FizzBuzz.

## Installing

    $ python setup.py install

## Running the tests

    $ python setup.py test

## Usage
```python
import sys
from fizz_buzz.fizz_buzz import *

def main():
    fizz_buzz = FizzBuzz(100)
    sys.stdout.write(fizz_buzz.say())

if __name__ == '__main__':
    main()
```