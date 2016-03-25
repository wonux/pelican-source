Title: openbox设置透明效果
Date: 2015-05-13 17:08
Modified: 2015-05-14 11:13
Category: Applications
Tags: apps, xorg, openbox,
Slug: apps-openbox-tranparent
Authors: 孤逐王
Summary:

[TOC]
## X窗口下的透明效果设置

使用` transset` + `devilspie` + `xcompmgr `设置透明效果。

X窗口下没有现成的工具，但可以借助于Xcompmgr和transset。
在运行Xcompmgr之后，就可以用transset来设置窗口透明度了。

### `transset`设置透明度

`opacity`变量：0～1。0表示完全透明，1表示不透明。如果不指定opacity参数，默认值是0.75

```
transset --help
```

查看用法
> options:
    -h, --help           display this message
    -t, --toggle         force toggle of opacity
    -c, --click          select by clicking on window  (default)
    -p, --point          select the window currently under the cursor
    -a, --actual         select the actual window
    -n, --name NAME      select by name, NAME is matched as regular expression
    --no-regex           don't use regular expression for matching name
    -i, --id             select by window id
        --inc            increase by the given opacity
        --dec            decrease by given opacity
    -m, --min OPACITY    minimum possible opacity  (default = 0)
    -x, --max OPACITY    maximum possible opacity  (default = 1)
    -v, --verbose        print some debug info
    -V, --version        print version number


### `xcompmgr`显示透明效果

```
xcompmgr
```

但是，`transset`是一个命令行工具，如何与窗口系统结合起来，开机启动就显示透明效果呢。下面介绍两种使用方式。

### 结合`devilspie`的使用

devilspie支持自动绑定某类窗口，即窗口启动时会触发后台devilspie程序的相应行为。devilspie的配置文件在~/.devilspie/目录中，比如随便建立一个文件opacity.ds。内容为

```
( if
  ( or
    ( contains ( window_class ) "Gvim" )
    ( contains ( application_name ) "sakura" )
    ( contains ( application_name ) "tilda" )
  )
  ( begin
    ( spawn_async (str "transset -t -i " (window_xid)  ))
  )
  )
```

应该比较好理解，当启动Gvim， sakura 或 tilda 时设置其透明度为0.75。如执行`devilspie -a`，然后启动那个应用，它的属性就会在devilspie的输出中显示出来。

> 注意，xcompmgr和devilspie的启动不一定要放在.xinitrc中，只要在X启动之前执行即可，比如在openbox环境中，加入autostart.sh也是可以的。

### openbox下的使用

修改~/.config/openbox/rc.xml中的<context name=”Titlebar”>项下面的鼠标绑定内容。

```
<context name=”Titlebar”>
    <!-- 使用transset-df设置窗口透明效果 -->
    <mousebind button="C-Middle" action="Click">
        <action name="Execute">
            <execute>transset-df -p</execute>
        </action>
    </mousebind>
    <mousebind button="C-Up" action="Click">
        <action name="Execute">
            <execute>transset-df -p --inc 0.2 </execute>
        </action>
    </mousebind>
    <mousebind button="C-Down" action="Click">
        <action name="Execute">
            <execute>transset-df -p -m 0.2 --dec 0.2</execute>
        </action>
    </mousebind>
```

这样，你就可以在窗口标题栏上按Ctrl+中键切换透明度了，Ctrl+向上滚动增加透明度，Ctrl+向下滚动减少透明度。