import sys
import os
import json
import argparse

def moeglich(zfw, lep, wunden):
    if zfw * 2 >= lep:
        if wunden * 7 <= lep:
            return "\N{check mark}"
        
    return "\N{cross mark}"

parser = argparse.ArgumentParser()
parser.add_argument('lep', default = 1, help='Die Lebenspunkte die gegeben werden sollen', type = int)
parser.add_argument('wunden', default = 0, nargs='?', help='Die Anzahl Wunden die geheilt werden sollen', type = int)
parser.add_argument('-t', action='store_true', help='Flag für \'Rettung von der Schwelle des Todes\'')

args = parser.parse_args()

magier = os.environ["MAGIER"]
home = os.path.expanduser('~')

with open('{}/repos/dsa_zauber/zauberer/{}.json'.format(home, magier)) as f:
    magier_data = json.load(f)
    
zfw = magier_data["balsam"]["zfw"]

if args.t:
    if args.lep >= 0:
        print('Bei \'Rettung von der Schwelle des Todes\' bitte negative LeP angeben')
        sys.exit()
    
    if -1 >= args.lep >= -10:
        perm_asp = 1
        perm_lep = 1
    elif -11 >= args.lep >= -20:
        perm_asp = 2
        perm_lep = 2
    
    kosten = args.lep * (-2) + 1

    erschwernis = -args.lep

    print("Rettung von der Schwelle des Todes bei {} LeP: {} AsP, dazu {} permanente AsP (Erschwernis: {})\nPatient verliert {} permanente LeP".format(args.lep, kosten, perm_asp, erschwernis, perm_lep))
else:
    if args.lep < 1:
        print('Bitte positive LeP angeben')
        sys.exit()

    kosten = args.lep
    kosten3 = round(args.lep * 0.9)
    kosten6 = round(args.lep * 0.8)
    kosten9 = round(args.lep * 0.7)
    kosten12 = round(args.lep * 0.6)

    erschwernis = args.wunden * 2

    print("{} | Balsam-Kosten für {} Lebenspunkte mit {} Wunden: {} AsP (Erschwernis Gesamt: {})\n".format(moeglich(zfw, args.lep, args.wunden), args.lep, args.wunden, kosten, erschwernis))
    print("Mit Kostenverringerung + 3: {} AsP (Erschwernis Gesamt: {})".format(kosten3, erschwernis + 3))
    print("Mit Kostenverringerung + 6: {} AsP (Erschwernis Gesamt: {})".format(kosten6, erschwernis + 6))
    print("Mit Kostenverringerung + 9: {} AsP (Erschwernis Gesamt: {})".format(kosten9, erschwernis + 9))
    print("Mit Kostenverringerung + 12: {} AsP (Erschwernis Gesamt: {})".format(kosten12, erschwernis + 12))
