# 记录fastapi install


在自定义目录下下载https://gitee.com/startplatinum/full-stack-fastapi-postgresql.git

对自定义项目进行配置。

- pip install cookiecutter
- cookiecutter https://github.com/tiangolo/full-stack-fastapi-postgresql

安装docker-compose

- pip3 install docker-compose

在自定义目录下执行

- docker-compose up -d


安装过程中发现缺少poetry，需要安装，如果不能翻墙则需要先下载国内资源

`https://gitee.com/mirrors/poetry.git`
将下载的目录进行打包`tar -zcvf peotry.tar.gz poetry`并复制到自定义目录的mytest/backend/app目录下.

然后修改`backend/backend.dockerfile`和`backend/celeryworker.dockerfile `

```
# Install Poetry
#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
#    cd /usr/local/bin && \
#    ln -s /opt/poetry/bin/poetry && \
#    poetry config virtualenvs.create false
COPY ./app/poetry.tar.gz /app/
RUN tar -zxvf poetry.tar.gz && export POETRY_HOME=/opt/poetry && cd /app/poetry && python install-poetry.py && cd /usr/local/bin && ln -s /opt/poetry/bin/poetry && poetry config virtualenvs.create false

```


## 重启服务

- docker-compose up -d



