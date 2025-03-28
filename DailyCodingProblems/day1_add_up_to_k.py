#Pablo Moreno Moreu

"""Daily Coding Problem: Problem #1 [Easy]
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

def addTo(k, intList):
    rest = set()
    for i in intList:
        if i in rest:
            return True
        else:
            rest.add(k-i)
    return False
if __name__ == "__main__":
    print(addTo(17, [10,15,3,1, 2]))
    print(addTo(2, [2,1,4,39]))
    print(addTo(56, [23, 48, 9, 57, -1]))