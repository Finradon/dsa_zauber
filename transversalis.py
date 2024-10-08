import os
import json
import argparse

def moeglich(zfw, meilen, faktor) -> str:
    if zfw * faktor >= meilen:
        return "\N{check mark}"
    else:
        return "\N{cross mark}"

parser = argparse.ArgumentParser()
parser.add_argument('meilen', default = 1, help='Die Meilen die der Zaubernde Reisen möchte', type = int)
parser.add_argument('personen', default = 0, nargs='?', help='Die Anzahl Personen die mitreisen', type = int)

args = parser.parse_args()

magier = os.environ["MAGIER"]
home = os.path.expanduser('~')
with open('{}/repos/dsa_zauber/zauberer/{}.json'.format(home, magier)) as f:
    magier_data = json.load(f)

zfw = magier_data["transversalis"]["zfw"]

kosten = 10 + args.meilen + 7 * args.personen + 2 * args.meilen * args.personen - magier_data["kraftfokus"]
kosten3 = round(10 + (args.meilen/2) + 7 * args.personen + args.meilen * args.personen) - magier_data["kraftfokus"]
kosten6 = round(10 + (args.meilen/4) + 7 * args.personen + (args.meilen/2) * args.personen) - magier_data["kraftfokus"]
kosten9 = round(10 + (args.meilen/8) + 7 * args.personen + (args.meilen/4) * args.personen) - magier_data["kraftfokus"]
kosten12 = round(10 + (args.meilen/16) + 7 * args.personen + (args.meilen/8) * args.personen) - magier_data["kraftfokus"]
kosten15 = round(10 + (args.meilen/32) + 7 * args.personen + (args.meilen/16) * args.personen) - magier_data["kraftfokus"]
kosten18 = round(10 + (args.meilen/64) + 7 * args.personen + (args.meilen/32) * args.personen) - magier_data["kraftfokus"]

erschwernis = 7 * args.personen
print("{} | Transversalis-Kosten innerhalb von {} Meilen mit {} extra Personen: {} AsP (Erschwernis Gesamt: {})\n".format(moeglich(zfw, args.meilen, 1), args.meilen, args.personen, kosten, erschwernis))
print("{} | Mit Reichweite Vergrößern + 3: {} AsP (Erschwernis Gesamt: {})".format(moeglich(zfw, args.meilen, 2), kosten3, erschwernis + 3))
print("{} | Mit Reichweite Vergrößern + 6: {} AsP (Erschwernis Gesamt: {})".format(moeglich(zfw, args.meilen, 4), kosten6, erschwernis + 6))
print("{} | Mit Reichweite Vergrößern + 9: {} AsP (Erschwernis Gesamt: {})".format(moeglich(zfw, args.meilen, 8), kosten9, erschwernis + 9))
print("{} | Mit Reichweite Vergrößern + 12: {} AsP (Erschwernis Gesamt: {})".format(moeglich(zfw, args.meilen, 16), kosten12, erschwernis + 12))
print("{} | Mit Reichweite Vergrößern + 15: {} AsP (Erschwernis Gesamt: {})".format(moeglich(zfw, args.meilen, 32), kosten15, erschwernis + 15))
print("{} | Mit Reichweite Vergrößern + 18: {} AsP (Erschwernis Gesamt: {})".format(moeglich(zfw, args.meilen, 64), kosten18, erschwernis + 18))
