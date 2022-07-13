def myfunc(n):
  return abs(n + 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

tuple1=("apple","2849","True")
print(tuple1)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

if 5 > 2: print("Five is greater than two!")

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <=0:
      x = self.a
      self.a += 1
      return x
    else:
     raise StopIteration



myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

import datetime
x=datetime.datetime.now()
print(x)