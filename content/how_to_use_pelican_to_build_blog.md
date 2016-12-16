Title: 使用pelican搭建博客
Date: 2016-12-07 22:55
Modified: 2016-12-07 22:55
Category: python
Tags: pelican,python,blog

[TOC]

# 使用pelican搭建博客 #

## 简介 ##
pelican是一个用python写的静态博客生成器，可以方便的把Markdown文本转换为静态Html文本。
### 相关路径 ###
- 官方文档：[http://docs.getpelican.com/](http://docs.getpelican.com/)
- 源码：[https://github.com/getpelican/pelican](https://github.com/getpelican/pelican)
- 插件：[https://github.com/getpelican/pelican-plugins](https://github.com/getpelican/pelican-plugins)
- 主题：[https://github.com/getpelican/pelican-themes](https://github.com/getpelican/pelican-themes)


## 安装 ##
### 安装python ###
到官方网站[https://www.python.org/](https://www.python.org/)下载安装。
### 创建virtualenv环境 ###
这一步可选，virtualenv可方便管理多个隔离的python环境，这里创建一个供pelican使用的专用python环境。
```
//安装virtualenv
pip install virtualenv

//创建名称为pelican的virtualenv环境
virtualenv pelican

//进入pelican隔离环境目录，找到如下脚本并执行以激活环境
activate
```
### 安装pelican ###
下载最新pelican源码，进入源码目录。  
在pelican的virtualenv环境中安装
```
python setup.py install
```
### 安装markdown ###
```
pip install markdown
```

## pelican的使用 ##
### 生成pelican工程 ###
创建一个目录myblog，进入该目录，执行以下命令生成pelican博客工程
```
pelican-quickstart
```
命令执行后，会要求输入各种配置项，都可以选择默认，后面如果有需要可以在生成的配置文件中修改。  
生成完毕，可以看到如下结构的目录
```
|-myblog  
    |---content                   #存放markdown源文件
    |---output                    #生成的html文件会在这里
    |---develop_server.sh         
    |---fabfile.py
    |---Makefile
    |---pelicanconf.py            #配置文件
    |---publishconf.py
```
### 添加markdown文件 ###
创建一个markdown文件，内容如下
```
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.
```
将文件放入content目录中
### 生成博客 ###
在myblog目录中执行如下命令
```
pelican content
```
命令执行完毕，在output目录下就会生成对应的html文件
### 预览博客 ###
进入output目录，执行如下命令启动服务
```
python -m pelican.server
```
服务启动后，在浏览器中使用地址http://localhost:8000可查看博客效果
### 发布博客 ###
将output目录中的内容上传到github pages工程中或者coding pages工程中，即可通过github pages或coding pages访问博客  
本博客源码参考[这里](https://github.com/wadou/wadou_blog_pelican)

## FAQ ##
### pelican-quickstart 报错如何解决？ ###
#### 问题 ####
执行`pelican-quickstart`报错
> ".....\pelican\tools\pelican_quickstart.py", line 52, in \<module\>
  'lang': locale.getlocale()[0].split('_')[0], 
  AttributeError: 'NoneType' object has no attribute 'split'  
  
参考 [https://github.com/getpelican/pelican/issues/2043](https://github.com/getpelican/pelican/issues/2043)  
因为`locale.getlocale()` returns `(None, None)`
```
(pelican) E:\>python
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (In
tel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import locale
>>> locale.getlocale()
(None, None)
>>> locale.getdefaultlocale()
('zh_CN', 'cp936')
>>> locale.setlocale(locale.LC_ALL, '');
"Chinese_People's Republic of China.936"
>>> locale.getlocale()
("Chinese_People's Republic of China", '936')
```
#### 解决方法 ####
修改源码tools目录中的pelican_quickstart.py文件  
```
'lang': locale.getlocale()[0].split('_')[0],
```
修改为
```
'lang': 'Chinese',
```
直接使用中文，修改后，重新安装pelican使生效，详细修改见[https://github.com/wadou/pelican/commit/24817a5543edf88af73474ce17405eac62758b39](https://github.com/wadou/pelican/commit/24817a5543edf88af73474ce17405eac62758b39)

### 如何使支持markdown的TOC？ ###
1. 安装beautifulsoup4  
进入virtualenv环境，执行以下命令安装，该安装为插件`extract_toc`的必备依赖项
```
pip install beautifulsoup4
```
2. 下载`extract_toc`插件   
到[https://github.com/getpelican/pelican-plugins/tree/master/extract_toc](https://github.com/getpelican/pelican-plugins/tree/master/extract_toc)下载插件
3. 安装插件  
在blog目录下建立`plugins`目录，将下载的插件拷贝至该目录
4. 设置插件  
打开blog目录下的`pelicanconf.py`配置文件，增加如下内容
```
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["extract_toc"]
```
5. MD_EXTENSIONS无法设置的解决办法  
[官方文档](http://docs.getpelican.com/en/stable/settings.html)中说明在`pelicanconf.py`配置文件中的`MD_EXTENSIONS`项中设置markdown属性，但是实际发现`MD_EXTENSIONS`已被废弃
> MD_EXTENSIONS is deprecated use MARKDOWN instead.    

在pelican源码路径中的`settings.py`增加如下代码
```
'MARKDOWN': {
         'extension_configs': {
              'markdown.extensions.codehilite': {'css_class': 'highlight'},
              'markdown.extensions.extra': {},
              'markdown.extensions.meta': {},
              'markdown.extensions.toc': {},
          },
```
修改后需要重新安装pelican使生效  
详细修改参考[https://github.com/wadou/pelican/commit/1c2c662fa0cee857cbfa3c16032bf944d095fe40](https://github.com/wadou/pelican/commit/1c2c662fa0cee857cbfa3c16032bf944d095fe40)  
markdown的详细扩展列表可参考[http://pythonhosted.org/Markdown/extensions/](http://pythonhosted.org/Markdown/extensions/)  

### 如何使用主题？ ###
- 主题预览：[http://www.pelicanthemes.com/](http://www.pelicanthemes.com/)
- 主题源码：[https://github.com/getpelican/pelican-themes](https://github.com/getpelican/pelican-themes)

本博客在elegant主题的基础上进行改造
- elegant文档：[http://oncrashreboot.com/elegant-best-pelican-theme-features](http://oncrashreboot.com/elegant-best-pelican-theme-features)
- elegant文档源码：[https://github.com/talha131/onCrashReboot](https://github.com/talha131/onCrashReboot)
- elegant源码：[https://github.com/talha131/pelican-elegant/](https://github.com/talha131/pelican-elegant/)

使用方法  
1. 在myblog目录下建立`themes`目录
2. 下载elegant源码，并放入`themes`目录
3. 修改`pelicanconf.py`如下，增加主题配置
```
THEME = "themes/pelican-elegant"
```
## 参考 ##
1. http://basov.net/en/pages/about-site.html
2. http://me.blogabs.cc/
3. https://www.zhihu.com/question/20376047
5. http://wonux.github.io/git-pelican-elegant.html
6. http://wonux.github.io/git-pelican.html
7. https://www.zhihu.com/search?type=content&q=pelican
8. https://pypi.python.org/pypi
9. https://www.linuxzen.com/shi-yong-pelicanda-zao-jing-tai-bo-ke.html

## 本博客源码 ##
- pelican：[https://github.com/wadou/pelican](https://github.com/wadou/pelican)
- elegant主题：[https://github.com/wadou/pelican-elegant](https://github.com/wadou/pelican-elegant)
- 博客：[https://github.com/wadou/wadou.github.io](https://github.com/wadou/wadou.github.io)
- 博客工程：[https://github.com/wadou/wadou_blog_pelican](https://github.com/wadou/wadou_blog_pelican)









