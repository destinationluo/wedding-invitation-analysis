# 创意婚礼请柬统计脚本

婚礼请柬的统计脚本，每次执行可将请柬数据库中的人数以及祝福统计出发，发送给执行的邮箱，已达到统计和通知的目的

婚礼请柬的前端仓库地址：https://github.com/destinationluo/wedding-invitation-client.git

婚礼请柬的后端仓库地址：https://github.com/destinationluo/wedding-invitation-server.git

## 技术栈

- Python3
- pymysql
- smtplib

## 开发配置

1. launch.py中配置数据库信息和邮箱信息
2. config.ini中配置要发送通知的邮箱信息
3. 运行launch.py即可执行

## Windows环境部署

方式一、 使用pyinstaller进行打包
1. 安装pyinstaller`pip3 install pyinstaller`
2. 打包`pyinstaller launch.py`
3. 复制config.ini文件到dist/launch目录下
4. 运行dist/launch.exe即可执行

方式二、直接执行python脚本（需要python环境及依赖包环境）
1. 直接执行launch.py

## Linux环境部署

方式一、 使用pyinstaller进行打包
1. 安装pyinstaller`pip3 install pyinstaller`
2. 打包`pyinstaller launch.py`
3. 复制config.ini文件到dist/launch目录下
4. 执行`sh dist/launch`

方式二、直接执行python脚本（需要python环境及依赖包环境）
1. 修改start.sh脚本中的python路径及脚本路径
2. 执行`sh start.sh`

### Linux环境下部署的建议及坑
1. 若采用方式二进行部署，可通过以下命令把所有依赖包输出到文件:
`pip3 freeze -r modules.txt`
然后在Linux服务器采用以下命令来安装所有相关的依赖包
`pip3 install -r modules.txt`
2. 建议将执行脚本加入服务器的定时任务crontab中定时执行，可以从此不再管它
3. 阿里云的服务器有个大坑：禁用发邮件的25端口，这时需要我们改一下mailServer.py文件：
```python
# 修改25端口为465端口
# NETEASY_163 = ['smtp.163.com', 25]
NETEASY_163 = ['smtp.163.com', 465]

# 修改SMTP方法SMTP_SSL方法，采用SSL连接
# self.server = smtplib.SMTP(from_stmp_server[0], from_stmp_server[1])
self.server = smtplib.SMTP_SSL(from_stmp_server[0], from_stmp_server[1])
```