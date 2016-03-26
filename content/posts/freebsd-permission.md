Title: UNIX基础 -- 权限
Date: 2015-04-23 15:34
Modified: 2015-04-23 15:52
Category: FreeBSD
Tags: unix, permission, freebsd,
Slug: freebsd-permission
Authors: 孤逐王
Summary:

[TOC]

## 权限
Permissions

FreeBSD使用传统的UNIX®系统的基本权限。在UNIX®系统中，基本权限分配了三种访问类型：读、写、执行。权限可以用字母r、w、x表示；也可以用二进制数表示，按rwx的顺序，x值1，w值2，r值4。

```
0		---
1		--x
2		-w-
3		-wx
4		r--
5		r-x
6		rw-
7		rwx
```

> 使用命令ls的-l参数可以显示出文件的所属者、 所属组和其他人等属性。

### 权限的符号化表示
Symbolic Permissions

```
Option	    Letter	Represents
(who)	     u	      User
(who)	     g	      Group owner
(who)	     o	      Other
(who)	     a	      All (“world”)
(action)	     +      Adding permissions
(action)	     -	      Removing permissions
(action)	     =      Explicitly set permissions
(permissions)	r	Read
(permissions)	w	Write
(permissions)	x	Execute
(permissions)	t	Sticky bit
(permissions)	s	Set UID or GID
```

### FreeBSD文件标志
FreeBSD File Flags

FreeBSD 还支持使用 “文件标志”。这些标志为文件提供了进一步的安全控制机制，但这些控制并不适用于目录。这些文件标志提供了针对文件的进一步控制， 帮助确保即使是 root 用户也无法删除或修改文件。

### setuid、setgid和sticky 权限

除了前面已经讨论过的那些权限之外，还有三个管理员应该知道的权限配置。它们是setuid、setgid和 sticky。这些配置对于一些 UNIX® 操作而言很重要， 因为它们能提供一些一般情况下不会授予普通用户的功能。