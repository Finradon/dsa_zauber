import argparse
import math
import sys
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument('asp', default = 3, help='Die Astralpunkte die investiert werden. Muss durch 3 teilbar sein', type = int)
parser.add_argument('www', default = -1, nargs='?', help='Das Resultat aus dem 3W6 Wurf', type = int)

args = parser.parse_args()

if args.asp % 3 != 0:
    print("Bitte AsP angeben die durch 3 teilbar sind.")
    sys.exit()

elif args.www < 3 and args.www >= 0 or args.www > 18:
    print("3W6 muss größer als 2 und kleiner als 19 sein.")
    sys.exit()

elif args.www < -1:
    print("Bitte positive Zahl angeben.")
    sys.exit()

elif args.www == -1:
    radius = round(args.asp / 3)
    d_kosten = math.ceil(3 * 3.5) + args.asp #kosten=körperkraft
    min_kosten = 3 + args.asp
    max_kosten = 18 + args.asp

    print("Kosten: {} - {} AsP (Durchschnittlich: {} AsP) | Radius des Zentrums: {} Schritt\n".format(min_kosten, max_kosten, d_kosten, radius))
    while max_kosten > 2:
        radius += 1
        d_kosten -= 2
        min_kosten -= 2
        max_kosten -= 2
        print("Köperkraft zwischen {} und {} Schritt Entfernung: {} - {} (Durchschnittlich: {})".format(radius -0.99, radius, max(0, min_kosten), max_kosten, max(0, d_kosten)))
else:
    # magier = os.environ["MAGIER"]
    magier = "Leonello"
    home = os.path.expanduser('~')
    with open('{}/repos/dsa_zauber/zauberer/{}.json'.format(home, magier)) as f:
        magier_data = json.load(f)
    
    radius = round(args.asp / 3)
    kosten = args.www + args.asp - magier_data["kraftfokus"]
    kk = args.www + args.asp

    print("Kosten: {} AsP | Radius des Zentrums: {} Schritt\n".format(kosten, radius))
    while kk > 0:
        radius += 1

        print("Köperkraft zwischen {} und {} Schritt Entfernung: {}".format(radius -0.99, radius, kk))
        kk -=2