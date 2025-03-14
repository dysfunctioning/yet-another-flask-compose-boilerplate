#!/usr/bin/env python
import argparse
import os
import pytest
import sys


def main():
    os.environ['ENV'] = 'testing'
    parser = argparse.ArgumentParser()
    args, pytest_args = parser.parse_known_args()
    try:
        print(f'--> Running pytest with args: {pytest_args}')
        code = pytest.main(pytest_args)
    except Exception as e:
        print(f'--> Exception on pytest main: {str(e)}')
        code = 1

    return code


if __name__ == '__main__':
    sys.exit(main())
