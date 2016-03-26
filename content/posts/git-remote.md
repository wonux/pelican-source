Title: Git同时提交到多个远程仓库
Date: 2016-03-06 11:38
Modified: 2016-03-06 12:19
Category: Git
Tags: apps, git,
Slug: git-remote
Authors: 孤逐王
Summary:

[TOC]

在已经习惯使用git同步写代码，github无疑是最的托管平台，但是国内由于“你懂的”原因，速度很慢，有时无法访问，于是想把自己的代码同步到多个不同的远程仓库备份。

### 我的主要仓库:

[github] https://github.com/wonux.test.git  主仓库
[oschina] https://git.oschina.net/wonux/test.git  国内常用仓库

> 另外，国内还有coding(原来的gitcafe合并到了coding),csdn code等。

### 添加同名多个远程仓库

添加一个remote,这里是all,也可以是别的名字(如origin)

```
git remote add all https://github.com/wonux.test.git
```

再添加另一个:

```
git remote set-url --add all https://git.oschina.net/wonux/test.git
```

> 重复向同一个远程仓库名字添加需要`set-url --add`参数

如果有多个,按照上面这一个命令进行添加.

### 向多远程仓库推送代码

```
git push all --all
```

这样就会一次提交到多个库了,上面命令输出如下:

```
git push all --all
Username for 'https://github.com': wonux
Password for 'https://wonux@github.com': 
Counting objects: 68, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (56/56), done.
Writing objects: 100% (68/68), 72.16 KiB | 0 bytes/s, done.
Total 68 (delta 13), reused 0 (delta 0)
To https://github.com/wonux/test.git
 * [new branch]      master -> master
Username for 'https://git.oschina.net': wonux
Password for 'https://wonux@git.oschina.net': 
Counting objects: 68, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (56/56), done.
Writing objects: 100% (68/68), 72.16 KiB | 0 bytes/s, done.
Total 68 (delta 13), reused 0 (delta 0)
To https://git.oschina.net/wonux/test.git
 * [new branch]      master -> master
```

记住不要忘记`--all`参数，如果不加`--all`，则无法推送，提示：

```
git push all
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

fatal: unable to access 'https://github.com/wonux/test.git/': Couldn't resolve host 'github.com'
```

### 分析配置文件

在操作完上面的添加命令后，如果我们打开`.git/config`文件,我们可以看到这样的配置: 

```
[remote "all"]
	url = https://github.com/wonux/test.git
	fetch = +refs/heads/*:refs/remotes/all/*
	url = https://git.oschina.net/wonux/test.git
```

因此，直接在`.git/config`文件中添加：

```
[remote "all"]
	url = https://github.com/wonux/test.git
	fetch = +refs/heads/*:refs/remotes/all/*
	url = ……
```

有多少个远程库,就配置多少个url即可. 
从这里可以看出,第一种方法生成的配置中还有一个fetch配置,这个配置可以完全去掉.