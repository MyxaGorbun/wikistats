import os
import sys
import math

import array

import statistics as st

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            a = f.readline()
            a = a.strip()
            a = list(map(int, a.split(' ')))
            self._n, self._nlinks = a[0], a[1]
            i = 0
            self._titles = []
            self._sizes = array.array('L', [0]*self._n)
            self._links = array.array('L', [0]*self._nlinks)
            self._redirect = array.array('B', [0]*self._n)
            self._offset = array.array('L', [0]*(self._n))
            self._idunnootherways = array.array('L', [0]*(self._n))
            self._linksto = array.array('L', [0]*(self._n))

            for n in range(self._n):
                a = f.readline().strip()
                self._titles.append(a)
                a = f.readline()
                a = list(a.split(' '))
                self._sizes[n] = int(a[0])
                self._redirect[n] = int(a[1])
                self._offset[n] = self._offset[n-1] + int(a[2])
                self._idunnootherways[n] = int(a[2])
                a = int(a[2])
                i+=a
                while a != 0:
                    self._links[i-a] = int(f.readline())
                    a -= 1
            for i in range(self._n):
                self._linksto[i] = self._links.count(i)
        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id+1] - self._offset[_id]

    def get_links_from(self, _id):
        for i in range(self._offset[_id+1]-self._offset[_id]):
            return self._links[self._offset[_id]+i]

    def get_id(self, title):
        for i in range(len(self._titles)):
            if title == self._titles[i]:
                return i
                break
        return None
