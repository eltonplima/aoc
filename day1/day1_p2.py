#!/usr/bin/env python3

import sys
from itertools import cycle


class FrequencyDuplicate(Exception):
    pass


class ChronalCalibration():
    def __init__(self, frequencies):
        self.frequencies = frequencies
        self.resulting_frequency = 0
        self.resulting_frequencies = {self.resulting_frequency, }

    def _update_frequency_reached_twice(self):
        if self.resulting_frequency in self.resulting_frequencies:
            raise FrequencyDuplicate(self.resulting_frequency)

    def run(self):
        for frequency in cycle(self.frequencies):
            self.resulting_frequency += frequency
            self._update_frequency_reached_twice()
            self.resulting_frequencies.add(self.resulting_frequency)


def cleanup(frequency):
    return frequency.strip()


def cast(frequency):
    return int(frequency)


if __name__ == '__main__':
    frequencies = list()
    try:
        for current_frequency in sys.stdin:
            current_frequency = cleanup(current_frequency)
            current_frequency = cast(current_frequency)
            frequencies.append(current_frequency)
        chronal_calibration = ChronalCalibration(frequencies)
        chronal_calibration.run()
    except FrequencyDuplicate as exc:
        print(f'Frequency reached twice: {str(exc)}')
