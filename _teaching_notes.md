**Deck.py**

I've implemented both `create_cards` and `shuffle` methods because they're both
fairly simple.

For representing cards I've decided to use a dictionary. I think
strings would be too inflexible. What if we want to add more properties, for
example the card's numeric value? On the other hand I don't think a `Card` class
is necessary because I don't see a card needing any methods, it's just data.

If you're wondering about the list comprehension with 2 for loops it's the
same as this:

```
cards = []
for v in values:
    for s in suit:
        cards.append({'value': v, 'suits': s})
```

#### Follow Along
Next let's finish the `draw` method.


#### References
[Python docs - random.shuffle](https://docs.python.org/3/library/random.html#random.shuffle)