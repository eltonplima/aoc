#!/usr/bin/env python3

import sys


class ChronalCalibration():
    def __init__(self, frequencies):
        self.frequencies = frequencies
        self.current_frequency = 0

    def run(self):
        for frequency in self.frequencies:
            self.current_frequency += frequency


def cleanup(frequency):
    return frequency.strip()


def cast(frequency):
    return int(frequency)


if __name__ == '__main__':
    frequecies = []
    for frequency in sys.stdin:
        frequency = cleanup(frequency)
        frequency = cast(frequency)
        frequecies.append(frequency)
    chronal_calibration = ChronalCalibration(frequecies)
    chronal_calibration.run()
    print(chronal_calibration.current_frequency)
