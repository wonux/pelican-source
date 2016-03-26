Title: Git子模块引用外部项目
Date: 2014-11-14 13:38
Modified: 2015-01-06 08:19
Category: Git
Tags: apps, git,
Slug: git-git-submodule
Authors: 孤逐王
Summary:

[TOC]

## Git子模块(submodule)简介

经常有这样的事情，当你在一个项目上工作时，你需要在其中使用另外一个项目。也许它是一个第三方开发的库或者是你独立开发和并在多个父项目中使用的。这个场景下一个常见的问题产生了：你想将两个项目单独处理但是又需要在其中一个中使用另外一个。
子模块允许你将一个 Git 仓库当作另外一个Git仓库的子目录。这允许你克隆另外一个仓库到你的项目中并且保持你的提交相对独立。


## Git子模块用法

### 添加一个子模块

首先你要把外部的仓库克隆到你的子目录中。
假设你想把`elegant`项目加入到你的blog项目中，你通过`git submodule add`将外部项目加为子模块：

```
cd blog
git submodule add https://github.com/wonux/pelican-elegant.git pelican-themes/elegant
```

现在你就在项目里的`pelican-themes/elegant`子目录下有了一个`elegant`项目。你可以进入那个子目录，进行变更，加入你自己的远程可写仓库来推送你的变更，从原始仓库拉取和归并等等。

> `.gitmodules`配置文件，保存了项目 URL 和你拉取到的本地子目录。

### 克隆一个带子模块的项目

克隆你刚才创建子模块的项目。你将得到了包含子项目的目录，但里面没有文件：`elegant`目录存在了，但是是空的。
你必须运行两个命令：`git submodule init`来初始化你的本地配置文件，`git submodule update`来从那个项目拉取所有数据并检出你上层项目里所列的合适的提交。

``` 
cd blog
git submodule init pelican-themes/elegant
git submodule update
```

现在你的pacman子目录就处于你先前提交的确切状态了。

参考：
[Git-子模块](http://git-scm.com/book/zh/v1/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97)