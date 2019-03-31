### 更新备忘

#### 20190331

更新shixiseng_font_replace.py，实现爬虫实时更换网站字符替换字典。

### 一些笔记

- 使用requests的get方法获得的content是一个bytes对象，在进行bs4解析后才成为string，或者也可直接使用str()转换，使用bs4会将无法解析的文件字符去除，而str()方法则不会；

- Python I/O 中'wb'/'w'模式是创建→写入或删除→写入的逻辑，无需担心续写问题；

- xml文件中元素可能包含元素、属性和文本三种内容；






