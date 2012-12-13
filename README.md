markov
======

A Markov Chain class and some fun stuff I did with it

Useage
======

import the markov class with:
```python
from markov import markov
```

Samples
=======

word-learning.py is a sample program using the markov class designed to learn how to write based on a set of text that it reads.  To run this program use ```python word-learning.py \<filename>``` where <filename> is the name of the file that contains the learning text.  This program will also dump it's object as hidden files and load them back up on each run to save on computational time, if you change your text files make sure you delete the hidden files too.
