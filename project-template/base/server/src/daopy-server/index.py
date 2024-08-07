from dao3 import * # 导入岛三（当前端）的所有全局对象
print("你好，世界！这条信息来自于ap-dpy的server端!")
world.say("你好，世界！这条信息(world.say)来自于ap-dpy的server端!")
@world.onPlayerJoin
def onPlayerJoin(ev:GameEntityEvent):
    world.say(f"玩家{ev.entity.player.name}加入游戏！")
    