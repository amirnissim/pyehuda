# Pyehuda

Codename generator written in Python. It is named after [Eliezer Ben-Yehuda](http://en.wikipedia.org/wiki/Eliezer_Ben-Yehuda).

## Usage
```python
from vocabulary import adjectives, fruit
from pyehuda import Pyehuda

yehuda = Pyehuda(adjectives, fruit)
yehuda.generate()

>>> 'Angular Asparagus'
```