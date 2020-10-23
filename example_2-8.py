metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('DelhiNCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('MexicoCity', 'MX', 20.142, (19.433333, -99.133333)),
    ('NewYorkNewark', 'US', 20.104, (40.808611, -74.020386)),
    ('SaoPaulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:.2%}|{:^9}|{:^9}'.format(0.981153, 'lat.', 'long.'))
fmt = '{:15}|{:9.4f}|{:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


"""
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
"""
