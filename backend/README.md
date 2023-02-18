
### 1

```
下载swagger相关的静态资源文件
链接: https://pan.baidu.com/s/1MwbBIyv6SFJm8J2guYr9iA 提取码: surq
```

### 2

```
将static文件夹解压在main.py目录下

```

### 3

```
修改docs.py文件
我的ubuntu虚拟机中该文件目录如下
/home/username/.local/lib/python3.10/site-packages/fastapi/openapi/docs.py

修改get_swagger_ui_html函数中三行内容为如下
swagger_js_url: str="/static/swagger-ui/swagger-ui-bundle.js",
swagger_css_url: str="/static/swagger-ui/swagger-ui.css",
swagger_favicon_url: str="/static/swagger-ui/favicon.png",

修改get_redoc_html函数中两行内容为如下
redoc_js_url: str = "/static/redoc/bundles/redoc.standalone.js",
redoc_favicon_url: str = "/static/redoc/favicon.png",

```


### 4

```

在main.py中添加如下内容

from fastapi.staticfiles import StaticFiles

这一句需要添加在app = FastAPI()语句之后
app.mount('/static', StaticFiles(directory='static'))



```
