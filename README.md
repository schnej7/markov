markov
======

A Markov Chain class and some fun stuff I did with it

Useage
======

Import the markov class with:
```python
from markov import markov
```

The first thing you will need to do is create a markov object:
```python
Markov = markov()
```

To train the markov chain simply use:
```python
Markov.record( previous, current )
```
previous is the nth item in the sequence.
current is the n+1th item in the sequence.

Once the object is trained on all of your data, you simply use:
```python
Markov.predict( current )
```

current is the nth item in the sequence and this function will return the n+1th item in the sequence or ```none``` if there is no data to base the decision off of.

Samples
=======

word-learning.py is a sample program using the markov class designed to learn how to write based on a set of text that it reads.  To run this program use ```python word-learning.py <filename>``` where \<filename> is the name of the file that contains the learning text.  This program will also dump it's object as hidden files and load them back up on each run to save on computational time, if you change your text files make sure you delete the hidden files too.
