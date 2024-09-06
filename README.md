# Test-foodles

Foodles est un package Python créé dans le cadre d'un test technique pour une entreprise. Il contient une fonction qui permet de déterminer la fréquence des mots dans une phrase donnée.

**Note importante**: Il est demandé dans l'énoncé de trier les mots par ordre alphabétique cependant dans le tableau ASCII les majuscules sont avant les minuscules. C'est pourquoi j'ai pris l'initiative de lowercase les mots avant d'effectuer le tri.

## Installation
Pour installer ce package localement, clonez ce repository et exécutez la commande suivante :

```bash
pip install .
```

Après installation, il est également possible d'utiliser le package en CLI.

```bash
foodles "Hello world world" 1
```

## Fonctionnalités

La fonction principale du package `foodles` est `word_frequency`. Elle prend en entrée une phrase et un nombre, et retourne une liste de taille `n` où chaque élément contient un mot et la fréquence de ce mot dans la phrase. Cette liste est triée par fréquence décroissante et par ordre alphabétique en cas d'égalité.

### Exemple d'utilisation

```python
from foodles import word_frequency

sentence = "bar baz foo foo zblah zblah zblah baz toto bar"
n = 3
result = word_frequency(sentence, n)
print(result)
# Sortie:
# [
#    ("zblah", 3),
#    ("bar", 2),
#    ("baz", 2),
# ]
```


## Tests

Afin d'éxecuter les tests, j'ai décidé d'utiliser tox avec pytest ainsi que son module pytest-cov pour le coverage.

```bash
tox
```

Résultat:
```text
Name                      Stmts   Miss Branch BrPart    Cover   Missing
-----------------------------------------------------------------------
src/foodles/__init__.py       2      0      0      0  100.00%
src/foodles/cli.py            9      0      0      0  100.00%
src/foodles/core.py           8      0      4      0  100.00%
-----------------------------------------------------------------------
TOTAL                        19      0      4      0  100.00%
```

## Licence

Ce projet est sous licence MIT. Vous êtes libre d'utiliser, de modifier et de distribuer ce logiciel sous certaines conditions. Voir le fichier [LICENSE](./LICENSE) pour plus de détails.
