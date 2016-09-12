#! /usr/bin/env python
from random import choice


class Generator(object):
    MAX_SIZE = 4
    COLORS = range(1, 9)

    @staticmethod
    def create():
        return [choice(Generator.COLORS) for _ in range(Generator.MAX_SIZE)]
