## colection: Counter,namedtuple,orderdict,deque
from collections import Counter

a="aaaaadddaaaddddrrrwww"
my_count =Counter(a)
print(my_count)
print(my_count.items())

print(my_count.keys())
print(my_count.values())
print(my_count.most_common(2))
print(my_count.most_common(1))
## most common word
print(my_count.most_common(1)[0][0])
## make list
b ="aaaaasssddddfgg"
n= Counter(b)
print(list(n.elements()))
print(tuple(n.elements()))


from collections import namedtuple
point = namedtuple("point","x,y")
pt=point(1,-4)
print(pt.x,pt.y)

print(pt)
from collections import OrderedDict
orderdict = OrderedDict()
orderdict['q'] = "1"
orderdict['b'] = "2"
orderdict['c'] = "3"
orderdict['d'] = "4"
orderdict['e'] = "5"
print(orderdict)

from collections import defaultdict
default = defaultdict(int)

default["a"]="1"
default["c"]="2"

print(default["a"])
## if i give something does not exit it give o for int.if float then 0.0
print(default["r"])
default = defaultdict(float)

default["a"]="1"
default["c"]="2"

print(default["h"])

from collections import deque
m=deque()
m.append(1)
m.append(2)
print(m)
m.appendleft(3)
print(m)
m.pop()
print(m)
m.popleft()
print(m)
m.clear()
print(m)
m.extend([4,5,6,7])
print(m)
m.rotate(1)
print(m)
m.rotate(2)
print(m)
### lamda argument:expression
### lamda like a function
plus=lambda x:x+5
print(plus(5))

mult = lambda x,y:2*3
print(mult(2,3))

## function
def plus_a(d):
    return d+10

print(plus_a(4))

##
list_2d = [(1,2),(4,9),(2,6),(-1,-5)]
list1_2d = sorted(list_2d)
## sorted according to the y index
list2_2d = sorted(list_2d, key=lambda f: f[1])

print(list2_2d)
print(list_2d)
print(list1_2d)

##map function and sequince
a = [1,2,3,4,5,6,7]
b= map(lambda x:x*2 , a)
print(list(b))
####### important
b = [i*2 for i in a]
print(b)
c = [x for x in a if x%2 ==0]
print(c)






