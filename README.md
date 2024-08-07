# AP-dpy
> ⚠ 使用前须知！
>
> 这不是一个由[box3lab神岛实验室](https://box3lab.com)官方发布的项目
>
> 本项目未完全测试，存在不可预测的风险，不建议用于生产！！

> **如果使用本项目进行游戏开发，带来的后果作者不承担责任，本项目应该被视为整活项目**

> **如果使用本项目进行游戏开发，带来的后果作者不承担责任，本项目应该被视为整活项目**

> **如果使用本项目进行游戏开发，带来的后果作者不承担责任，本项目应该被视为整活项目**


将`Python`集成到[神岛ArenaPro](https://www.yuque.com/box3lab/doc/fi2z90g00qp2hwac)的项目里！
（arenapro+daopy=啥？不知道，反正daopy的1m体积够神岛编辑器喝一壶的）

## 使用
### 创建Ap-dpy项目
在ArenaPro上使用Python需要一定修改，所以这样的项目要通过本插件创建。

打开一个空的文件夹

按下<kbd>Ctrl-Shift-P</kbd> 打开命令面板，输入并找到：
```
Ap-dpy: 创建 AP-dpy 项目
```
请等待一切执行完成，查看终端提示。
### 编写Ap-dpy代码
找到`client/src/daopy-client/index.py` 和 `server/src/daopy-server/index.py`，它们分别是`client端`和`server端`的入口文件
```python
# 假设这是server端
from dao3 import * # 引入当前端的所有全局对象（api）
@world.onPlayerJoin
def onPlayerJoin(ev):
    world.say(f"{ev.entity.player.name} 加入了这个游戏！")

```
### 关于api
> 提示：
> - `MicroPython WASM`支持目前存在无法解决的bug，不想理会的话请使用`Skulpt.js`支持： 
> `from dao3 import *` 不可用，原因未知。需要精确导入，例如`from dao3 import world,voxels`

Python的API与js的几乎没有区别，所以直接阅读box3api文档即可。编写代码时有自动补全的。但是编写时要注意以下几点：
1. 需要引入API：`from dao3 import *`
会引入当前端所有的API
2. 再也没有异步了：所有的`async函数`或者返回`Promise`的函数会被同步执行，直接阻塞返回结果（这个是`Skulpt.js`的`Suspension`特性），例如`dialog`不需要`await`了。如果你需要写一段不断执行的脚本，那么推荐你用`@world.onTick`事件
3. 事件使用：以下是推荐的事件使用方式：
```python
# server端
from dao3 import *

# 1.装饰器形式,函数名随意
@world.onPlayerJoin
def onPlayerJoin(ev:GameEntityEvent):
    # ev 是事件对象，冒号后面的可加可不加，加了自动补全会更方便，至于加什么嘛，看box3api文档
    world.say(f"{ev.entity.player.name} 加入了这个游戏！")

# 2.普通函数形式
def onPlayerJoin(ev:GameEntityEvent):
    world.say(f"{ev.entity.player.name} 加入了这个游戏！")
world.onPlayerJoin(onPlayerJoin) # 注册事件
```

### 预构建、构建和上传
1. 预构建：这个在命令面板里输入`预构建`可以找到，会把daopy文件编译成`_daopy_bundle.ts`
2. 构建+上传：这个是原ArenaPro的功能了，本插件直接调用它来完成预构件以后的操作。
3. **预构建+构建+上传**，这个可以在命令面板找到，直接执行所有操作上传到地图。（一键三连了属于是，这个是最常用的）

### 注意事项
- 创建AP-dpy不要使用原版的ArenaPro插件，这样创建的是纯TypeScript项目。
- 使用本插件时请使用命令面板中的**预构建+构建+上传**来部署

## 相关链接

### 以下是ArenaPro官方的链接：
> 本项目与只是个人项目，作为ArenaPro的功能扩展，以下是ArenaPro官方的链接
1. [Box3lab: ArenaPro插件](https://www.yuque.com/box3lab/doc/fi2z90g00qp2hwac): 
告别繁琐，拥抱高效！神岛ArenaPro插件，专为游戏开发者设计，旨在通过无缝集成`VSCode`与`神岛Arena编辑器`，为游戏开发带来前所未有的便捷与效率。本插件不仅解决了Arena编辑器功能单一、开发体验不佳的问题，还引入了TypeScript支持与精通神岛API的Chat吉PT，为游戏开发提供更丰富的功能和体验。

2. [神岛实验室](https://box3lab.com): 这是`ArenaPro`的开发团队的官网。

### 以下是非官方（本插件）的链接：
1. [daopy-runtime](https://github.com/tobylai-toby/daopy-runtime): 神岛中运行Python的运行时组件+Python版API代理，基于Skulpt。

2. [daopy-npm](https://www.npmjs.com/package/daopy-npm): 发布在npm上的daopy运行时，更好地适配`ArenaPro`

3. [tobylai的小站](https://tobylai.fun)

### 其他链接：
1. [Skulpt.js](https://github.com/skulpt/skulpt): Skulpt 是一个用 JavaScript 编写的 Python 解释器，可以在浏览器中运行 Python 代码。本项目运行时基于它修改，删删改改。

## 鸣谢
- [神奇代码岛](https://dao3.fun)
- [神岛实验室](https://box3lab.com)
- [岛研所(非官方)](https://github.com/Box3TRC)
- [Skulpt.js](https://github.com/skulpt/skulpt)
- 图标部分使用了 [Python 的图标 Icons8](https://icons8.com/icon/12584/python)