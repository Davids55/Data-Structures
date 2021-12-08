# SETS
## Introduction
Unlike Stacks, Lists or Queues Sets don’t really worry about the location/order when adding or removing an item it holds. Sets have a unique difference to these other data structures. A Set will not allow duplicates which is useful when we want unique answers form large lists. We might  use Sets when  fast performance for adding, removing, and finding are our top priorities. 

## How to read a stack
In python Stacks are made using the curly brackets {} now python also uses {} for dictionaries. You read though a set the same way you do with Stacks starting at zero rather than one. One of the best tools we have for checking sets is the "in" command. The in command will return true if the desire value is in your set let’s look at an example. (Go ahead and run the code to see what happens) 

```python
set = {5, 8, 9, 7, 3, 1}

if 5 in set:
    print("We found it in the set)
else:
    print("not there")
```
Because 5 was in the set we got the positive return now try 

```python
set = {8, 9, 7, 3, 1}

if 5 in set:
    print("We found it in the set)
else:
    print("not there")
```

## Adding to or removing from a set
Adding to or removing from a set is very similar to Stacks but has more going on in the background. When we use non-integers in a set they are Hashed in the background by python turning them into numbers so python can check for duplicates. For example, the word dog might be hashed as the number 1433604155. The hash will change each time you run your code but will be consistent for that execution of the code. If you want to check the hash number use `hash()`

There are two important other differences to note. One is the commands we run to add or remove items from a set. For stacks we used `.append` to add and `.pop` to remove. For sets we use `.add` and `.remove`. The second difference is because sets don’t care about location or order we must tell python what value to remove unlike the pop command. 

Try running this code

```python
set = {8, 9, 7, 3, 1}

set.remove(7)
set.add(10)
set.add(8)

print(set)
```
Notice that even though we tried to add another 8 to the set when the updated set printed we only got one 8. As mentioned at the start of the section sets don’t allow duplicates. So, we can try to add as many as we wanted but the set will remove all duplicates. 

## Intersections and unions
Two unique operations that sets have access to are Intersections and unions. When we call an `intersection()` we are comparing two sets with each other. The intersection well then return any items the sets have in common. Try this code:

```python


set = {8, 9, 7, 3, 1}

set2 = {8, 5, 10, 7}

set3 = set.intersection(set2)
print(set3)
```
When run the code should return `{8, 7}` as those two numbers are found in both sets. 

A Union joins together two different sets into one new set try this code.

```python
set = {8, 9, 7, 3, 1}

set2 = {8, 5, 10, 7}

set3 = set.union(set2)
print(set3)
```
This time we should get `{1, 3, 5, 7, 8, 9, 10}` 


One final note about adding, removing, and checking for values in a set. They are O(1) assuming there are no hash conflicts 

## Example

Let’s walk though an example problem using sets together. 
We have been given a set `{3, 5, 20, 9, 7, 2}` and must complete the following adjustments.

1. remove the highest number form the set
2. add 18, 6, and 12
3. join the first set with a seconded set `{5, 13, 22, 8}`

Our first task asks us to remove the highest number from the set.

```python
set_1 = {3, 5, 20, 9, 7, 2}

set_1.remove(20)
```
Next we add the three new numbers

```python
set_1 = {3, 5, 20, 9, 7, 2}

set_1.remove(20)
set_1.add(18)
set_1.add(6)
set_1.add(12)

```
Finally we join the two sets

```python
set_1 = {3, 5, 20, 9, 7, 2}

set_1.remove(20)
set_1.add(18)
set_1.add(6)
set_1.add(12)

set_2 = {5, 13, 22, 8}

set_3 = set_1.union(set_2)

print(set_3)

```
Your final result should be `{2, 3, 5, 6, 7, 8, 9, 12, 13, 18, 22}`



 

## Problem to Solve

If you want some for practice Try this this Problem.

Check if two sets have any elements in common. If yes, display the common elements and join the two lists otherwise tell the user that no common elements were found.

```python
Set_1 = {10, 15, 20, 40, 55}
set_2 = {30, 50, 15, 25}
```
