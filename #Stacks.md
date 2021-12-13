# Stacks
To understand the data structure of stacks let’s say you have a bunch of books that you need to stack on a table. Now Stacks in python work in a very similar manner to stacking books. A stack in python is ordered by which items are added and removed. Now when you place book on your stack it would be called a push in python. That book would go on top (back) of the stack and if we were to remove a book from the stack or pop as it’s called in python it would be the first to go. Just like removing books from a stack you would start with the top (or last item in your stack) and work your way down (to the first item). 



## Reading a Stack

Let’s take a look at an actual stack and break it down piece by piece.


```python
stack = [1, 2, 3, 4, 5]
```
Here in this Stack, we already 5 items. In Python Stacks are represented by using lists. One is the first the item on the list and five is the last. Now with a list this short we can just look at the list and tell the length. However larger lists can be much harder to track. Thankfully there is a command built in python that can return the size of a stack. The len() command will tell you the size of your input stack.

```python
stack = [1, 2, 3, 4, 5]

size = len(stack)

print(size)
```
Go ahead and copy the code and run it using your preferred code editor. The code should return 5 when run as our list is five items long. Now try it with this stack just replace the previous one. This time you should get Seven even though the stack has no numbers in it. As we mentioned in the introduction every code we write takes time to run and we measure that time In Big O notation. Finding the size of a stack is a very efficient bit of code and is only O(1)

```python
stack = [a, b, c, d, e, f, g]
```


## Adding to a Stack

Now lets say we need to add to the original stack 
```python
stack = [1, 2, 3, 4, 5]
```
as mentioned we call adding to the stack pushing and whatever value we push it will always end up on the end of the stack. So lets say we want to add the number 6 to the stack we would use code that would look like this (go ahead and copy/run this one to)

```python
stack = [1, 2, 3, 4, 5]

stack.append(6)

print(stack)
```
Now we should have 
```python
[1, 2, 3, 4, 5, 6]
```

Just like finding the size of a list the Big O notation of pushing to a stack is O(1) because no matter how many items you add they will always be placed at the end of the stack.




## Removing from a Stack

Removing from a stack is almost the same as adding to a stack though we can do a thing or two more. Now to remove something form a stack we use pop. (Go ahead and try this code)

```python
stack = [1, 2, 3, 4, 5]

stack.pop()

print(stack)
```
Now the stack should look something like 
```python
[1, 2, 3, 4]
```

however, we can be more specific with what we remove from stacks in python. When we call pop() we can call what item we want deleted from our list by placing the position of item inside the () give this code a spin.

```python
stack = [1, 2, 3, 4, 5]

stack.pop(3)

print(stack)
```
notice which number got removed from the list. The reason that 4 got removed instead of three is because lists in python start at zero. You can also set a variable to the item that you just popped by using code that looks like this.

```python


removed_item = stack.pop()
```



Just like the other two we discussed removing from a list is O(1) as it only needs to go to one place and delete and the location is already known. 



## Example

Now we are going to take a problem and walk through it together and apply what we have learned about stacks/lists. 
Let’s say we have been given a task of editing this List. 

```Python
list = ["Rhino", "Lion", "Monkey", "Tiger", "Horse", "turtle"]
```
we have been tasked to 
1. Remove Lion and Tiger from the list
2. Add Sheep, Lama, and Giraffe to the stack
3. Find the length of the list. 

our first step would be to remove Lion and Tiger form the list. For that we need to use a pop() command. remember that stacks and lists start counting at 0


```Python
list = ["Rhino", "Lion", "Monkey", "Tiger", "Horse", "turtle"]

list.pop(1)
list.pop(3)
```
next we would call the append command to add the new items.

```Python
list = ["Rhino", "Lion", "Monkey", "Tiger", "Horse", "turtle"]

list.pop(1)
list.pop(3)
list.append("Sheep")
list.append("Lama")
list.append("Giraffe")
```

finally, we will use len() to get the new length of the list.

```Python
list = ["Rhino", "Lion", "Monkey", "Tiger", "Horse", "turtle"]

list.pop(1)
list.pop(3)
list.append("Sheep")
list.append("Lama")
list.append("Giraffe")

print(len(list))
```



## Try it Yourself
Now a more complicated problem to try yourself. Your goal here is to use a while loop and reverse this stack. One last hint you can use `if len(my_stack) == 0` to return true or false.

```python
[1, 2, 3, 4, 5]
```

when your finished take a look [here for a sample soultion.](https://github.com/Davids55/Data-Structures/blob/main/stack_soultion.py)


[back to home](https://github.com/Davids55/Data-Structures)


