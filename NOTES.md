
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

collections.nametuple 是一个工厂函数，可以用来构建一个带字段名的元祖和一个有  
名字的类——这个带名字的类对调试程序有很大帮助。

> 用 nametuple 构建的类的实例所消耗的内存跟元祖是一样的，因为字段名都被存在  
> 对应的类里面。这个实例跟普通的对象实例比起来也要小一些，因为 Python 不会用
> `__dict__` 来存放这些实例的属性

```python
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)
```

## 列表生成中嵌套for循环

> 也叫作列表推导，list comprehension --> listcomps
>
> 对应的还有生成器表达式，generator expression --> genexps

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

## timeit 测试代码的速度

用 `timeit.repeat` 方法，通过 `setup` 参数设置代码段用到的方法和常量

```python
import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))


clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
```

## 笛卡尔积

两个或以上的列表中的元素对构成元祖，这些元祖构成的列表就是笛卡尔积。

> 笛卡尔积是一个列表，列表里的元素是由输入的可迭代类型的元素对构成的元祖，因此
> 笛卡尔积列表的长度等于输入变量的长度的乘积

```bash
        [red, blue]
[A,  [A red, A blue,
 K,   K red, K blue,
 Q]   Q red, Q blue]
```

如上所示，含有两种颜色和 3 种牌面的列表的笛卡尔积，结果是一个包含 6 个元素的列表。

## 列表推导与生成器表达式

列表推导的作用只有一个：生成列表。

生成器表达式：
- 可以生成其他类型的序列
- 可以逐个地产出元素、
- 能节省内存

```python
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
```

## 元祖和记录

元祖拥有作为记录数据信息的功能，如

```python
lax_coordinates = (33.9425, -118.408056)
# 元祖拆包
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
```

## \_ 与 国际化软件

`_` 也是 gettext.gettext 函数的常用别名。里面有个 `_()` 函数，所以在使用
gettext 做国际化处理时，应避免使用 `_` 做占位符

> gettext 模块的文档: https://docs.python.org/3/library/gettext.html

## 平行赋值

如，

```python
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(head, b, c, d)
```

## 字符串 format 占位符

- 名称索引: `{price}`
    - ```python
      txt1 = "My name is {fname}, I'am {age}".format(fname = "John", age = 36)
      ```
- 数字索引: `{0}`
    - ```python
      txt2 = "My name is {0}, I'am {1}".format("John",36)
      ```
- 空占位符: `{}`
    - ```python
      txt3 = "My name is {}, I'am {}".format("John",36)
      ```

### Formatting Types
添加以下的格式化字符串来格式结果

| 格式化字符串 | 说明                        |
| ------------ | --------------------------- |
| `:<`         | 左对齐                      |
| `:>`         | 右对齐                      |
| `:^`         | 中间对齐                    |
| `:b`         | 将数字转成二进制格式        |
| `:c`         | 将数值转成对应的Unicode字符 |
| `:e`         | 科学计数格式，小写的e表示   |
| `:E`         | 科学计数格式，大写的E表示   |
| `:f`         | 固定的小数格式              |
| `:%`         | 将数值转成百分比格式        |
