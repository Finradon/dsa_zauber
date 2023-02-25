import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument('asp', default = 3, help='Die Astralpunkte die investiert werden. Muss durch 3 teilbar sein', type = int)

args = parser.parse_args()

if args.asp % 3 != 0:
    print("Bitte AsP angeben die durch 3 teilbar sind.")
    sys.exit()
    
d_kosten = math.ceil(3 * 3.5) + args.asp #kosten=körperkraft
min_kosten = 3 + args.asp
max_kosten = 18 + args.asp
radius = round(args.asp / 3)

print("Kosten: {} - {} AsP (Durchschnittlich: {} AsP) | Radius des Zentrums: {} Schritt\n".format(min_kosten, max_kosten, d_kosten, radius))
while max_kosten > 2:
    radius += 1
    d_kosten -= 2
    min_kosten -= 2
    max_kosten -= 2
    print("Köperkraft bis {} Schritt Entfernung: {} - {} (Durchschnittlich: {})".format(radius, max(0, min_kosten), max_kosten, max(0, d_kosten)))

