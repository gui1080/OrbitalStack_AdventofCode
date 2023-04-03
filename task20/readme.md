## Moving Logic

Moving a number in the list is basically removing It and adding It again in a given index.

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

### Problem

In the original task, as you are moving:

Moving = -2
Index = 2

Circular Linked List 
 -> 1
 -> 2
 -> -2
 -> 0
 -> -3
 -> 3
 -> 4
End of CLL.

The correct result is:

Circular Linked List 
 -> 1
 -> 2
 -> 0
 -> -3
 -> 3
 -> 4
 -> -2
End of CLL.

And not:

Circular Linked List 
 -> -2
 -> 1
 -> 2
 -> 0
 -> -3
 -> 3
 -> 4
End of CLL.

This felt a little inconsistent to me. 