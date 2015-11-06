Wechat-Python-Template
========

将此文件夹放到树莓派中，更改`index.py`中的`your_token`为你的`token`

在文件夹目录内，输入命令执行：`sudo python index.py 80`

80为绑定到80端口上，微信公众平台目前仅支持80端口

Ps:如果无法执行，可能需要更改文件权限：`chmod +x index.py`

需要安装`webpy`和`python-lxml`

``` bash

git clonegit://github.com/webpy/webpy.git

ln -s `pwd`/webpy/web

cd /root/webpy

sudo python setup.py install

sudo apt-get install python-lxml

```

程序执行后，在微信公众平台的接口配置界面分别输入`你的ip`或者`域名`及`token`：

`http://你的ip或域名/weixin`

然后输入刚才配置程序时更改的自己的`token`

点击提交，提示配置成功。

在微信上对此公众平台测试号发送消息，微信可以返回你发送的消息。

至此，微信平台与树莓派的对接结束
