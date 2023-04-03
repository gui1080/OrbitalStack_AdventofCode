## Moving Logic

Moving a number in the list is basically removing It and adding It again at a certain index.

### Moving Positive Numbers

"3 moves between 0 and 4"
1, 2, 3, -2, -3, 0, 4
3 is CLL[2]
3 needs to be CLL[5]
remove CLL[2]
1, 2, -2, -3, 0, 4
insert 3, CLL[5]

result:
1, 2, -2, -3, 0, 3, 4

"10 moves between 2 and 3"
1, 2, 3, -2, -3, 10, 4
10 is CLL[5]
10 needs to be CLL[2]
list is size 7
10 + 5 mod 7 = 1
remove CLL[5]
1, 2, 3, -2, -3, x, 4
insert 10, CLL[2]

result:
1, 2, -2, 5, -3, 0, 3, 4

### Moving Negative Numbers

"-2 moves to 1, 2"
1, 2, 3, -2, -3, 10, 4
-2 is CLL[4]
-2 needs to be CLL[2]
4 + (- 2) = 2

result:
1, -2, 2, 3, -3, -10, 4

"-10 moves to 3, -2"
1, 2, 3, -2, -3, -10, 4
-10 is CLL[5]
-10 needs to be CLL[2]
5 - (- 10) % 7 = 1

if data.node < index, don't add 1
else, add 1 and insert

1, -2, 2, 3, -3, 10, 4

### Problem 1

In the original task, as you are moving:

Moving = -2
Index = 2

```
Circular Linked List 
 -> 1
 -> 2
 -> -2
 -> 0
 -> -3
 -> 3
 -> 4
End of CLL.
```

The correct result is:

```
Circular Linked List 
 -> 1
 -> 2
 -> 0
 -> -3
 -> 3
 -> 4
 -> -2
End of CLL.
```

And not:

```
Circular Linked List 
 -> -2
 -> 1
 -> 2
 -> 0
 -> -3
 -> 3
 -> 4
End of CLL.
```

This felt a little inconsistent to me, but ok.

### Problem 2

"The numbers should be moved in the order they originally appear in the encrypted file. Numbers moving around during the mixing process do not change the order in which the numbers are moved."

In other words, one should start with a list that goes like:

```
x -> y -> z
```

And as It moves, you still have to do "x" operation, "y" operation and "z" operation at last.

But, If you have:

```
x -> y -> z -> x -> w
```

And you still have to do "x" operation, then "y" operation, then "z" operation and then "x" operation again. But what occurrence of "x" should be taken into account? Logically, the second occurrence. But that adds another layer of complexity to the problem that really was not specified as the example given only shows a list with no repeated elements.

Sometimes, the original second occurrence of "x" won't be the second occurrence at the mixing moment.