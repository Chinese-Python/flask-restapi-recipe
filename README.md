###API 的使用

**1、初始化数据库

在run.py的同级目目录中运行：

python run.py -i

**2、使用Gunicorn运行服务器(以端口号5001为例)

在screen中操作，如screen -S flaskAPI,在screen中运行:

gunicorn -w4 -b0.0.0.0:5001 restapi:app

**3、为固定IP生成一个API Key（以120.67.218.31为例）

如果ip为0.0.0.0，则任何ip的用户均有权限 ，退出screen在session中运行：

python manage.py -g 120.67.218.31 "My Flask Key0906" 
python manage.py -g 0.0.0.0 "test key 0907"


###API特点说明

**1、可实现多条件、多字段查询
**2、为特定IP生成唯一的API key
**3、多模块可拓展性，随时添加新的数据模块
**4、网页地址及端口

###API key的管理

**1、生成一个API key，0.0.0.0 表示所有用户可以获取 
./run.py -g IP -c "this IP is for the engineer on floor 3"
**2、删除一个API key 
./run -d APIKEYID
**3、显示所有的API key 
./run -a
