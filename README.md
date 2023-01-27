# DSA Zauber CLI tools

Diese Repo beinhaltet praktische CLI-Programme zu berechnung einiger DSA4-Zauber mitsamt interessanter Varianten & Erschwernisse

## Installation

1. Repo klonen
2. Im Ordner `zauberer` eine .json Datei für den eigenen Magier anlegen (siehe Muster `zauberer.json`)
3. Umgebungsvariable `MAGIER` definieren
```console
$ MAGIER=zauberer
```
4. Mit Python ein Skript ausführen:
```console
$ python3 transversalis 1
$ python3 balsam 1
```
5. Ein `alias` auf das jeweilige skript machen:
```console
$ alias transversalis="python3 /home/repos/dsa_zauber/transversalis.py"
$ alias balsam="python3 /home/repos/dsa_zauber/balsam.py"
```
Sollte es zu `fileNotFound error` kommen dann einfach den pfad zur repo in den Skriptenändern.

## Nutzung

### Transversalis

```console
$ transversalis <meilen> <personen>
```
* Meilen: Die Anzahl Meilen die der Zaubernde sich teleportieren möchte
* Personen: Die Anzahl Personen die mitreist (zusätzlich zum Zaubernden)

Meilen müssen stets angegeben werden, Personen greift auf den Standard-Wert von 0 zurück, wenn kein zweites Argument gegeben wurde.

```console
$ transversalis 10 0
✓ | Transversalis-Kosten innerhalb von 10 Meilen mit 0 extra Personen: 20 AsP (Erschwernis Gesamt: 0)

✓ | Mit Reichweite Vergrößern + 3: 15 AsP (Erschwernis Gesamt: 3)
✓ | Mit Reichweite Vergrößern + 6: 12 AsP (Erschwernis Gesamt: 6)
✓ | Mit Reichweite Vergrößern + 9: 11 AsP (Erschwernis Gesamt: 9)
```

Wenn die Anzahl der Meilen über den Maximalwert geht, wird anstelle des Hakens ein 'Verboten' Symbol gezeigt (auch in Abhängigkeit von der jew. Variante 'Reichweite Vergrößern).
Hier ein Beispiel mit dem ZfW 12:

```console
$ transversalis 25
❌ | Transversalis-Kosten innerhalb von 25 Meilen mit 0 extra Personen: 35 AsP (Erschwernis Gesamt: 0)

❌ | Mit Reichweite Vergrößern + 3: 22 AsP (Erschwernis Gesamt: 3)
✓ | Mit Reichweite Vergrößern + 6: 16 AsP (Erschwernis Gesamt: 6)
✓ | Mit Reichweite Vergrößern + 9: 13 AsP (Erschwernis Gesamt: 9)
```

### Balsam

```console
$ balsam <lep> <wunden> -t
```
* lep: Die Anzahl Lebenspunkte die gegeben werden sollen
* Wunden: Die Anzahl an Wunden die geheilt werden sollen
* -t: Flag für 'Rettung von der Schwelle des Todes'. Bei dieser Option müssen negative LeP angegeben werden (die LeP unter 0)

```console
$ balsam 8 1
✓ | Balsam-Kosten für 8 Lebenspunkte mit 1 Wunden: 8 AsP (Erschwernis Gesamt: 2)

Mit Kostenverringerung + 3: 7 AsP (Erschwernis Gesamt: 5)
Mit Kostenverringerung + 6: 6 AsP (Erschwernis Gesamt: 8)
Mit Kostenverringerung + 9: 5 AsP (Erschwernis Gesamt: 11)
Mit Kostenverringerung + 12: 4 AsP (Erschwernis Gesamt: 14)
```

Das Symbol am Anfang gibt an, ob die gegebenen LeP ausreichen um alle Wunden zu heilen:

```console
$ balsam 6 1
❌ | Balsam-Kosten für 6 Lebenspunkte mit 1 Wunden: 6 AsP (Erschwernis Gesamt: 2)

Mit Kostenverringerung + 3: 5 AsP (Erschwernis Gesamt: 5)
Mit Kostenverringerung + 6: 4 AsP (Erschwernis Gesamt: 8)
Mit Kostenverringerung + 9: 4 AsP (Erschwernis Gesamt: 11)
Mit Kostenverringerung + 12: 3 AsP (Erschwernis Gesamt: 14)
```

Mit '-t' wird die Rettung von der Schwelle des Todes berechnet (Wunden sind hierbei egal):

```console
$ balsam -7 -t
Rettung von der Schwelle des Todes bei -7 LeP: 15 AsP, dazu 1 permanente AsP (Erschwernis: 7)
Patient verliert 1 permanente LeP
```




