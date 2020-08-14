
## collections.nametuple

用 colections.nametuple 构建一个简单类来表示一张纸牌，利用 nametuple，可以很  
轻松的得到一个纸牌对象：

```python
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
beer_card = Card('7', 'diamonds')
print(beer_card)
```

输出：

```bash
Card(rank='7', suit='diamonds')
```

nametuple 用以构建只有少数属性但是没有方法的对象，比如数据库条目

## 列表生成中嵌套for循环

如，

```python
from collections import namedtuple
Card = namedtuple('Card', ['rank', 'suit'])
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds club hearts'.split()
[Card(rank, suit) for suit in suits for rank in ranks]
```

等同于：

```python
from collections import namedtuple
Card = namedtuple('Card', ['rank', 'suit'])
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds club hearts'.split()
test = []
for suit in suits:
    for rank in ranks:
        test.append(Card(rank, suit))
test
```

## \_\_repr__

repr 通过 `__repr__` 特殊方法来得到一个对象的字符串表示形式

```python
from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        对象的字符串表示形式
        :return:
        """
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
    v = Vector(3, 4)
    print(abs(v))
    print((v * 3))
    print(abs(v * 3))
```

输出：

```bash
Vector(4, 5)
5.0
Vector(9, 12)
15.0
```

### \_\_repr__ 和 \_\_str__ 的区别

后者在 `str()` 函数被使用，或是在用 `print` 函数打印一个对象的时候才被调用的，
并且它返回的字符串对终端用户更友好。
如果你只想实现这两个特殊方法的一个，`__repr__` 是更好的选择，因为如果一个对象
没有 `__str__` 函数，而 Python 又需要调用它的时候，解释器会用 `__repr__`
作为替代

## 中缀运算符的基本原则

**不改变操作对象，而是产出一个新的值**

## magic function 隐式调用规则

如，`bool(x)` 的背后是调用 `x.__bool__()` 的结果；如果不存在 `__bool__` 方法，
那么 `bool(x)` 会尝试调用 `x.__len__()` 。若返回 0，则 `bool` 会返回 False;
否则返回 True。