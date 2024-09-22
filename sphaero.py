import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument('asp', default = 3, help='Die Astralpunkte die investiert werden. Muss durch 3 teilbar sein', type = int)
parser.add_argument('www', default = -1, nargs='?', help='Das Resultat aus dem 3W6 Wurf', type = int)

args = parser.parse_args()