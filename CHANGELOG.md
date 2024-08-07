# 更新记录

## 3.0.1
- 跟进ArenaPro版本，原本的ArenaPro构建上传命令被从xxx.upload改为了xxx.buildNUpload，故不更新此扩展将无法使用。
- 添加了`JavaScript`的实验性支持(去学ts吧~arenapro原本的ts~)，迟一点说不定扩展就改名了

## 3.0.0
- 添加MicroPython WASM支持，但目前存在无法解决的bug，建议使用Skulpt：
 `from dao3 import *`不可用，原因未知。需要精确导入，例如`from dao3 import world,voxels`
## 2.0.4
- 稍微改下介绍而已，凑数的
- 顺便发布`稳定版`试试（

## 2.0.3
- 修复一处默认代码

## 2.0.2
- `prebuild-daopy.js` 进行了修改来修复目录嵌套无法导入的bug，旧用户可能需要创建一个新项目然后复制这个文件。

# 2.0.0~2.0.1
- 一些修复
- 创建的新项目有`pyi`文件。Py文件有自动补全了。
- `"daopy-npm": "^2.0.3-fix"`

## 1.0.0
- Client端支持


## [Unreleased]
- Server端支持
- Initial release