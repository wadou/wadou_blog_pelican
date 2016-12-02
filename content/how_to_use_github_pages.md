Title: GitHub Pages的使用
Date: 2016-07-03 10:52
Modified: 2016-07-03 10:52
Category: git
Tags: git,github,blog

[TOC]

# GitHub Pages的使用 #

## 简介 ##
GitHub Pages可以作为服务器发布静态站点，包括User、Organization、和Project Pages，其区别如下：

|Type of GitHub Pages site|Pages default domain & host location on GitHub|Publishing branch|
|:---|:---|:---|
|User Pages site|username.github.io|master|
|Organization Pages site|orgname.github.io|master|
|Project Pages site owned by a **user account**|username.github.io/projectname|gh-pages|
|Project Pages site owned by an **organization**|orgname.github.io/projectname|gh-pages|


* 个人主站点：repository的名称为username.github.io，通过master分支发布，发布后通过https://username.github.io访问
* 个人子站点：repository的名称随意，为project名，通过gh-pages分支发布，发布后通过https://username.github.io/projectname访问



## User Pages 创建 ##
个人user pages创建步骤如下：

1. 创建repository，名称为**username.github.io**
![fb905862-40ef-11e6-865f-001eecd77418](https://raw.githubusercontent.com/wadou/image_hosting_01/master/fb905862-40ef-11e6-865f-001eecd77418.png)

2. 设置，如图点击***Settings***
![36cb4874-4780-4867-9682-bd0b141ef9eb](https://raw.githubusercontent.com/wadou/image_hosting_01/master/36cb4874-4780-4867-9682-bd0b141ef9eb.png)

3. 在**GitHub Pages**的设置项中点击***Launch automatic page generator***
![28e7dd0c-e180-4c17-914a-0ab48881c58d](https://raw.githubusercontent.com/wadou/image_hosting_01/master/28e7dd0c-e180-4c17-914a-0ab48881c58d.png)

4. 直接点击***Continue to layouts***
![c6ad5879-43f0-4cc1-8d2c-22d0ac1395a2](https://raw.githubusercontent.com/wadou/image_hosting_01/master/c6ad5879-43f0-4cc1-8d2c-22d0ac1395a2.png)

5. 选择主题，然后发布
![8338af88-53d9-4ab6-b76a-101ce268a0ef](https://raw.githubusercontent.com/wadou/image_hosting_01/master/8338af88-53d9-4ab6-b76a-101ce268a0ef.png)

6. 登陆查看效果
![f1026f3e-9c32-4f78-9347-51a03c299caf](https://raw.githubusercontent.com/wadou/image_hosting_01/master/f1026f3e-9c32-4f78-9347-51a03c299caf.png)


## Project Pages 创建 ##
1. 创建repository，名称随意，这里以**projectname**为例
2. 创建**gh-pages**分支
3. 将静态html文件上传到gh-pages分支，即可通过https://username.github.io/projectname/ 访问



## 参考 ##
[1] <https://help.github.com/categories/github-pages-basics/>