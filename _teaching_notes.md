**Blackjack.py**

First let's describe what we want to happen in the `take_bets` method:

1. Show the player how much they have in their bankroll.
2. Ask the player how much they want to bet.
3. Reduce the player's bankroll by the bet amount.
4. Save the bet amount so you can pay out later.

None of these things look like they should be handled by another object. They're
also simple enough to code directly without creating any new methods.

#### Follow Along

Next let's try to implement `deal_hands`.

#### References

[String formatting](https://mkaz.tech/code/python-string-format-cookbook/)

[Python 3 - *input* function](https://docs.python.org/3/library/functions.html#input)

[What's the difference between raw_input() and input() in python3.x?](https://stackoverflow.com/questions/4915361/whats-the-difference-between-raw-input-and-input-in-python3-x)
