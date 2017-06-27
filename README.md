# fizzbuzz

Enjoy FizzBuzz.

## Installation

    $ python setup.py install

## Usage
```python
import sys
from fizz_buzz.FizzBuzz import *

def main():
    fizzbuzz = FizzBuzz(100)
    sys.stdout.write(fizzbuzz.say())

if __name__ == '__main__':
    main()
```