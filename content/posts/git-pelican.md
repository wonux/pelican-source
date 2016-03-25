Title: Pelican + Github 搭建静态个人博客
Date: 2015-05-06 16:45
Modified: 2015-05-14 18:19
Category: Git
Tags: apps, pelican, blog, git, python,
Slug: git-pelican
Authors: 孤逐王
Summary:

[TOC]

## 前言

一直以来都希望拥有属于自己的个人博客，随性发点信息，写点技术感想，记录自己的生活，重要的是不受广告的影响、不被河蟹、不会担心有一天被莫名其妙地消失。

之前看过一篇[文章](http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html)：“像黑客一样写博客”，一下子就被这种简单的方式深深的吸引住了。你只需要一个称手的文本编辑器（Markdown编辑器），再配合终端的git命令就OK了，其余的都不用管了，交给第三方去。几条简单的命令就可以发布博客。

优点：
- 直接使用Markdown写文章
- 全站静态化，根据Markdown生成文章的静态页面
- 直接在Terminal把文章push到Github上即可，有版本管理真好，然后加之Github Page的支持，虽然有一些些小问题，比如缓存，但瑕不掩瑜
- 整个写作过程和写代码的过程是一致的，符合码农的行为习惯，也就是所谓的“像黑客一样写博客”

本博客是在Gentoo Linux环境下搭建完成，托管到Github Pages。
效果见我的博客:[http://wonux.github.io](http://wonux.github.io)

## 知识储备

搭建博客的工具选用了Pelican，Pelican是一个用Python语言编写的静态网站生成器，支持使用restructuredText和Markdown写文章，配置灵活，扩展性强，有许多优秀的主题和插件可供使用。Pelican 的Github地址是：[https://github.com/getpelican/pelican](https://github.com/getpelican/pelican);主页：[http://blog.getpelican.com/](http://blog.getpelican.com/)

搭建过程中涉及如下技术知识，不过你不必害怕，只是使用它们的开源框架而已，并不需要自己编码，点击可以了解它们是如何的强大，当然你也可以略过它们，后面遇到时再进行了解。
假如你不能打开它们，原因你懂的，请爬墙解决~

> Github:[https://github.com/](https://github.com/)
Github Ppages:[http://pages.github.com/](http://pages.github.com/)
git:[http://git-scm.com/](http://git-scm.com/)
python:[http://www.python.org/](http://www.python.org/)
pip:[https://pypi.python.org/pypi](https://pypi.python.org/pypi)
pelican:[http://blog.getpelican.com/](http://blog.getpelican.com/)
markdown:[http://daringfireball.net/projects/markdown/syntax](http://daringfireball.net/projects/markdown/syntax)

## 搭建Pelican环境

### 安装git,pip

```
emerge --ask dev-cvs/git
emerge --ask dev-python/pip
```

### 使用virtualenv工具创建pelican虚拟环境

```
emerge --ask virtualenv  ## or  pip install virtualenv
virtualenv ~/virtualenvs/pelican
cd ~/virtualenvs/pelican
source bin/activate
```

### 安装pelican

```
pip install pelican
```

###  安装markdown,typogrify

```
pip install Markdown
pip install typogrify
```

## 搭建博客站点

```
mkdir blog //创建文件夹，名称可根据自己喜欢定
cd blog
pelican-quickstart
```

`pelican-quickstart`执行命令后，会提示输入博客的配置项，除了少数几个必填以外，其它都可以选择默认，而且都可以在pelicanconf.py文件中进行更改，所以你可以随意选择。
命令成功执行后，会出现pelican的框架，如下所示

```
blog/
├── content                # 存放输入的markdown或RST源文件
│   └── (pages)            # 存放手工创建的静态页面，可选
│   └── (posts)            # 存放手工创建的文章，可选
├── output                 # 存放最终生成的静态博客
├── develop_server.sh      # 测试服务器
├── Makefile               # 管理博客的Makefile
├── pelicanconf.py         # 配置文件
└── publishconf.py         # 发布文件，可删除
```

### 选择博客主题

回到`blog`目录下，按如下步骤下载pelican官方主题，从里面挑选出自己喜欢的主题吧，大多数主题预览界面你可以打开这个网页[主题预览](http://pelicanthemes.com/)进行查看。不过如今pelican又新出了很多主题，所以你需看看[pelican主题开源库](https://github.com/getpelican/pelican-themes)。

- 克隆主题到本地

```
git clone https://github.com/getpelican/pelican-themes.git
```

- 使用主题
打开`pelicanconf.py`配置文件，更改或添加THEME为自己喜欢的主题，例如本博客所挑选的elegant，更多的配置含义请关注[官方文档](http://docs.getpelican.com/en/3.5.0/index.html)。

```
THEME = 'pelican-themes/pelican-elegant'
```

### 添加评论系统

开启个人博客的原因在于分享知识，分享就需要交流，评论模块当然少不了。大多数主题默认支持Disqus。在[Disqus](https://disqus.com/)上申请帐号，按照流程Disqus会分配给你站点的Shortname，记牢Shortname，如果忘了请进入admin/settings中查看。然后同理，在`pelicanconf.py`添加
国内也可以选择[多说](http://duoshuo.com)和[友言](http://www.uyan.cc).

```
DISQUS_SITENAME = Shortname
```

### 书写文章

完成上述博客主体搭建后，使用markdownpad创建一个.md文件，保存于content文件夹中（或自己加入posts文件夹）。
Metadata syntax for Markdown posts should follow this pattern:

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

### 发布博客站点
[Publish your site](http://docs.getpelican.com/en/3.5.0/publish.html#publish-your-site)
有三种方法可以发布博客：
- pelican命令
- make 
详细用法查看`Makefile`文件
- fabric


#### 生成博客站点

[Site generation](http://docs.getpelican.com/en/3.5.0/publish.html#site-generation)

```
pelican /path/to/your/content/ [-s path/to/your/settings.py]
```

或

```
make html
```

生成的站点放在`output/`目录下。

#### 预览生成的站点

For Python 2, run:
```
cd output
python -m SimpleHTTPServer
```

For Python 3, run:
```
cd output
python -m http.server
```

或

```
make serve
```

浏览[http://localhost:8000/](http://localhost:8000/)地址预览效果.

#### 部署博客站点

[Deployment](http://docs.getpelican.com/en/3.5.0/publish.html#deployment)
原理：将`output`目录下生成的站点部署到自己的github pages.

#### 自动化操作

- Fabric
```
pip install Fabric
fab build
fab regenerate
fab serve
fab publish
```

- Make
```
make html
make regenerate
make serve
make devserver
make stopserver
./develop_server.sh stop
```

>> 备注：发布的简单流程：`pelican content`生成页面至`output`目录，然后`git push`将`output`目录推送到github站点的`gh-pages`分支，即可自动渲生成染博客。

### 预览我的博客效果

[http://wonux.github.io](http://wonux.github.io)
[http://wonux.coding.me](http://wonux.coding.me)

参考资料：
[http://www.xycoding.com/articles/2013/11/21/blog-create/](http://www.xycoding.com/articles/2013/11/21/blog-create/)