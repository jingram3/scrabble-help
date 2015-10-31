scrabble-help
=============

A few functions in Python to help win at Scrabble.

Use bingo [tiles] to check see if you have any 7-letter words.  Use ? for a blank tile.

```
>>>bingo stin?at
conatus
toucans
astound
soutane
outsang
nougats
outmans
amounts
outspan
santour
```

Otherwise, just type a word to see if it's in the scrabble dictionary.

```
>>>hello
True
```

You can also see if 2 words of equal length can be stacked 
so that the vertical columns are also words.

```
>>>stack boy ahi
True
```

Calling stack with just a number will give you a list of pairs of words having that length that can be stacked on top of eachother.
This returns much more than you might think.
