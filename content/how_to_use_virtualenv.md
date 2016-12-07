Title: virtualenv的使用
Date: 2016-07-10 09:52
Modified: 2016-07-10 09:52
Category: python
Tags: python,virtualenv

[TOC]

# virtualenv的使用 #

## 简介 ##
virtualenv可以创建隔离的python环境，详情可参考[官方网站](https://virtualenv.pypa.io/en/latest/index.html)。

## 安装 ##
这里使用pip安装，命令如下
```
pip install virtualenv
```
安装过程如下图
![83d27173-3d84-4ec3-9513-ea16b41dd365](https://raw.githubusercontent.com/wadou/image_hosting_01/master/83d27173-3d84-4ec3-9513-ea16b41dd365.png)

## 查看帮助 ##
安装完成后，查看帮助命令如下
```
virtualenv -h
```
如下图
![76536961-a9dc-467c-96d2-3bd0a525385c](https://raw.githubusercontent.com/wadou/image_hosting_01/master/76536961-a9dc-467c-96d2-3bd0a525385c.png)

这里关注如下几个参数
*  **-p** : 如果当前系统安装了多个版本的python环境，可以使用该参数指定virtualenv环境使用的python版本，帮助中可以看到默认的python版本。
*  **--no-site-packages** : 创建的virtualenv环境不使用系统python环境的安装包，这个选项是默认的。
*  **--system-site-packages** ：创建的virtualenv环境使用系统python环境的安装包。




## 创建virtualenv环境 ##
以创建名称为test的隔离环境为例，使用命令如下
```
virtualenv test
```
如下图
![b00d2eda-cdfa-4e14-a3c8-7749bdddff49](https://raw.githubusercontent.com/wadou/image_hosting_01/master/b00d2eda-cdfa-4e14-a3c8-7749bdddff49.jpg)

默认安装下，会将setuptools、pip、wheel安装到隔离环境中。

## 激活virtualenv环境 ##
进入隔离环境目录，执行如下即激活隔离环境
```
activate
```
如下图，可以通过pip list看到当前隔离环境已安装了哪些软件
![48be61cc-a1ca-4f9e-a13f-262d253d6bf5](https://raw.githubusercontent.com/wadou/image_hosting_01/master/48be61cc-a1ca-4f9e-a13f-262d253d6bf5.jpg)

## 退出virtualenv环境 ##
执行如下命令即可退出隔离环境
```
deactivate
```
