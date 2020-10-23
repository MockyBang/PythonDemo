from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
# `_fields` 是一个包含这个类所有字段名称的元祖
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# `_make()` 通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟 `City(*delhi_data)` 是一样的
delhi = City._make(delhi_data)
# `_asdict()` 把具名元祖以 `collections.OrderedDict` 的形式返回，
# 可以利用它来把元祖里的信息友好地呈现出来
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)
