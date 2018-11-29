基于 [markolofsen/py_translator](https://github.com/markolofsen/py_translator)

#### 安装

`$ pip install git+https://github.com/GuQiangJS/py_translator.git`

#### 变更记录

* 2018/11/29 使用中发现 Google 修改了部分源码，造成在解析 `https://translate.google.com` 时遭遇以下错误：

    ```
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:\Program Files\Python37\lib\site-packages\py_translator\client.py", line 172, in translate
        data = self._translate(text, dest, src)
      File "C:\Program Files\Python37\lib\site-packages\py_translator\client.py", line 75, in _translate
        token = self.token_acquirer.do(text)
      File "C:\Program Files\Python37\lib\site-packages\py_translator\gtoken.py", line 184, in do
        self._update()
      File "C:\Program Files\Python37\lib\site-packages\py_translator\gtoken.py", line 56, in _update
        self.tkk = self.RE_TKK.findall(r.text)[0]
    ```

    主要是解析不到源码中标记Token的部分。新的格式：`tkk:'428743.1969233314'`