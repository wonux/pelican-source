Title: Git创建空白新分支
Date: 2016-03-24 15:38
Modified: 2016-03-26 15:19
Category: Git
Tags: apps, git,
Slug: git-empty-branch
Authors: 孤逐王
Summary:

[TOC]

有时候需要在项目中创建一个空白的新分支，来开发测试与当前分支内容无关的内容。向分支提交一个初始的空commit，保证完全复位。

### 创建并切换新分支

```
git branch <new_branch>
git checkout <new_branch>
git rm --cached -r . 
git clean -f -d
```

### 创建空的commit

```
git commit --allow-empty -m "[empty] initial commit"
```

### 推送新分支

```
git push origin <new_branch>
```