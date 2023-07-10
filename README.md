# 《使用 Flask + Flask RESTful 快速搭建 API 服务》 代码仓库

> 这是一个基于 [Flask](https://flask.net.cn/) 搭建的服务，遵守 RESTful API 规范
> [使用 Flask + Flask RESTful 快速搭建 API 服务](https://juejin.cn/post/7252976055093592120) 文章中的项目代码存放于此
## 运行项目

```bash
# 克隆仓库 todo 填写gitlab地址
git clone <gitlabPath>
# 进入仓库 todo 填写克隆下来的文件夹名字
cd <filePath>

# 使用虚拟环境
python3 -m venv venv
# 在 windows 下：
py -3 -m venv venv

# 激活虚拟环境
. venv/bin/activate
# 在 windows 下：
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 添加环境变量
# 环境变量中会存放一些敏感信息 如密钥、数据库密码等
# 每个开发者应该在自己本地新建 .env 文件 并添加环境变量
FLASK_ENV=development # 当前环境
FLASK_DEBUG=True # 开启 debug mode
FLASK_APP=run.py # flask项目入口文件
SECRET_KEY=b... # flask扩展密钥
JWT_SECRET_KEY=b... # jwt密钥
MYSQL_USER_NAME=... # MySQL数据库名称
MYSQL_USER_PASSWORD=... # MySQL数据库密码
MYSQL_HOSTNAME=...# MySQL数据库地址
MYSQL_PORT=...# MySQL数据库端口
MYSQL_DATABASE_NAME=...# MySQL数据库名称

# 第一次运行 或 数据库模型映射('/app/api/models/*')有更改后 需要同步数据库
flask db migrate
flask db upgrade

# 运行 
# 在IDE中可以手动运行 run.py 文件 或 使用命令行：
flask run
```

## 发布

```bash
# 打包镜像
docker build -t <image_name> .
# 运行容器
docker run -p 5000:5000 --name <container_name> --restart=always <image_name>
```

## 开发时注意

```bash
# 在安装新依赖或卸载依赖后 需要手动导出依赖描述文件 requirements.txt
pip freeze -l > requirements.txt

# 第一次运行 或 数据库模型映射('/app/api/models/*')路径下的文件有更改或新增后 需要使用迁移插件同步数据库
flask db migrate
flask db upgrade
# 要注意 使用迁移插件必须在 /app/__init__.py 中显式的导入该模型文件
# 所有数据库模型 需要显式的在这里导入 不然同步无效！！！
# from .api.models.user import UserModel
# from .api.models.revoked_token import RevokedTokenModel

# /app/config.py 中关于数据库的一些敏感配置 建议在项目根目录下新建 .env 文件进行统一管理
MYSQL_USER_NAME=... # MySQL数据库名称
MYSQL_USER_PASSWORD=... # MySQL数据库密码
MYSQL_HOSTNAME=...# MySQL数据库地址
MYSQL_PORT=...# MySQL数据库端口
MYSQL_DATABASE_NAME=...# MySQL数据库名称
```
