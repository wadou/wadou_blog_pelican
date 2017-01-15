Title: java环境变量设置
Date: 2017-01-15 11:29
Modified: 2017-01-15 11:29
Category: java
Tags: java,环境变量

[TOC]

# java环境变量设置 #

## windows xp ##
### 配置 ###
1. 右键`我的电脑-->属性`打开系统属性界面
2. 在`高级`页签下点击`环境变量`按钮，打开环境变量设置页面
3. 在`系统变量`下点击`新建`，设置**JAVA_HOME**，如图，变量名为**JAVA_HOME**，变量值为安装的jdk路径  
![d4f0450c-0e45-40c7-bdef-93e53b2e5bbf](https://raw.githubusercontent.com/wadou/image_hosting_01/master/d4f0450c-0e45-40c7-bdef-93e53b2e5bbf.png)
4. 在`系统变量`中找到`Path`，在`Path`的值中增加`%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin`，注意，不同的值之间要用分号隔开，如图  
![d245111a-0a82-40bd-a569-b57a0f0e7993](https://raw.githubusercontent.com/wadou/image_hosting_01/master/d245111a-0a82-40bd-a569-b57a0f0e7993.png)
5. 在`系统变量`中找到`CLASSPATH`，在`CLASSPATH`的值中增加`%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar`，注意，不同的值之间要用分号隔开，如图  
![309063fc-33dc-4611-8a30-186fae58d2e8](https://raw.githubusercontent.com/wadou/image_hosting_01/master/309063fc-33dc-4611-8a30-186fae58d2e8.png)
### 检查配置 ###
打开命令行窗口，输入`java -version`可以查看到java版本，如下
```
C:\Documents and Settings\Administrator>java -version
java version "1.8.0_102"
Java(TM) SE Runtime Environment (build 1.8.0_102-b14)
Java HotSpot(TM) Client VM (build 25.102-b14, mixed mode, sharing)
```
输入`javac`可以查看到帮助信息，如下
```
C:\Documents and Settings\Administrator>javac
用法: javac <options> <source files>
其中, 可能的选项包括:
  -g                         生成所有调试信息
  -g:none                    不生成任何调试信息
  -g:{lines,vars,source}     只生成某些调试信息
  -nowarn                    不生成任何警告
  -verbose                   输出有关编译器正在执行的操作的消息
  -deprecation               输出使用已过时的 API 的源位置
  -classpath <路径>            指定查找用户类文件和注释处理程序的位置
  -cp <路径>                   指定查找用户类文件和注释处理程序的位置
  -sourcepath <路径>           指定查找输入源文件的位置
  -bootclasspath <路径>        覆盖引导类文件的位置
  -extdirs <目录>              覆盖所安装扩展的位置
  -endorseddirs <目录>         覆盖签名的标准路径的位置
  -proc:{none,only}          控制是否执行注释处理和/或编译。
  -processor <class1>[,<class2>,<class3>...] 要运行的注释处理程序的名称; 绕过默
认的搜索进程
  -processorpath <路径>        指定查找注释处理程序的位置
  -parameters                生成元数据以用于方法参数的反射
  -d <目录>                    指定放置生成的类文件的位置
  -s <目录>                    指定放置生成的源文件的位置
  -h <目录>                    指定放置生成的本机标头文件的位置
  -implicit:{none,class}     指定是否为隐式引用文件生成类文件
  -encoding <编码>             指定源文件使用的字符编码
  -source <发行版>              提供与指定发行版的源兼容性
  -target <发行版>              生成特定 VM 版本的类文件
  -profile <配置文件>            请确保使用的 API 在指定的配置文件中可用
  -version                   版本信息
  -help                      输出标准选项的提要
  -A关键字[=值]                  传递给注释处理程序的选项
  -X                         输出非标准选项的提要
  -J<标记>                     直接将 <标记> 传递给运行时系统
  -Werror                    出现警告时终止编译
  @<文件名>                     从文件读取选项和文件名
```

