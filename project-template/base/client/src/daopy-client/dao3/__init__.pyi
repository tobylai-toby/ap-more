from typing import Any, Callable, Dict, List, Optional, Tuple, TypeVar, Union
from enum import Enum

K = TypeVar('K')  # 泛型类型变量

# 日志记录方法
GameLoggerMethod = Callable[..., None]

# 控制台日志记录方法
class Console:
    """
    包含控制台日志记录方法的类。
    """
    @staticmethod
    def assert_(condition: bool, message: Any) -> None:
        """
        如果条件为假，则记录错误。可选地包括消息。
        """
        ...

    @staticmethod
    def log(message: Any, *optionalParams: Any) -> None:
        """
        记录消息到控制台。
        """
        ...

    @staticmethod
    def debug(message: Any, *optionalParams: Any) -> None:
        """
        使用“debug”级别记录消息到控制台。
        """
        ...

    @staticmethod
    def error(message: Any, *optionalParams: Any) -> None:
        """
        使用“error”级别记录消息到控制台。
        """
        ...

    @staticmethod
    def warn(message: Any, *optionalParams: Any) -> None:
        """
        使用“warn”级别记录消息到控制台。
        """
        ...

    @staticmethod
    def clear() -> None:
        """
        清空控制台。
        """
        ...

console = Console()

# 事件处理模块
class EventEmitter:
    """
    事件处理模块
    """
    def on(self, type: K, listener: Callable[[Any], None]) -> None:
        """
        添加指定事件类型的事件监听器。
        """
        ...

    def once(self, type: K, listener: Callable[[Any], None]) -> None:
        """
        添加一个只会触发一次的事件监听器。
        """
        ...

    def remove(self, type: K, listener: Callable[[Any], None]) -> None:
        """
        通过类型和监听器函数删除事件监听器。
        """
        ...

    def removeAll(self, type: Optional[K] = None, listener: Optional[Callable[[Any], None]] = None) -> None:
        """
        删除所有事件监听器，或特定类型的监听器和/或监听器函数。
        """
        ...

    def add(self, type: K, listener: Callable[[Any], None]) -> None:
        """
        与on方法相同的别名。
        """
        ...

    def off(self, type: K, listener: Callable[[Any], None]) -> None:
        """
        与remove方法相同的别名。
        """
        ...

    def emit(self, type: K, event: Any) -> None:
        """
        触发指定类型的事件。
        """
        ...

# 客户端-服务器通信的远程通道
ClientRemoteChannelEvents = Dict[str, Any]
class ClientRemoteChannel:
    """
    发送服务器事件和监听客户端事件的远程通道。
    """
    def sendServerEvent(self, event: Any) -> None:
        """
        通过远程通道发送服务器事件。
        """
        ...

    @property
    def events(self) -> EventEmitter[ClientRemoteChannelEvents]:
        """
        监听客户端事件的事件发射器。
        """
        ...

# 坐标类
class Coord2:
    """
    表示带有偏移量和比例的2D坐标。
    """
    offset: 'Vec2'
    scale: 'Vec2'

    @staticmethod
    def create(val: Optional['Coord2'] = None) -> 'Coord2':
        """
        创建新的Coord2实例。
        """
        ...

class Vec2:
    """
    表示2D向量。
    """
    x: float
    y: float

    def copy(self, val: 'Vec2') -> None:
        """
        将另一个Vec2的值复制到当前对象。
        """
        ...

    @staticmethod
    def create(val: Optional['Vec2'] = None) -> 'Vec2':
        """
        创建新的Vec2实例。
        """
        ...

class Vec3:
    """
    表示3D向量。
    """
    x: float
    y: float
    z: float
    r: float
    g: float
    b: float

    def copy(self, val: 'Vec3') -> None:
        """
        将另一个Vec3的值复制到当前对象。
        """
        ...

    @staticmethod
    def create(val: Optional['Vec3'] = None) -> 'Vec3':
        """
        创建新的Vec3实例。
        """
        ...

# UI节点事件
UiEvent = Dict[str, Any]
UiInputEvent = Dict[str, Any]

UiNodeEvents = Dict[str, UiEvent]
UiInputEvents = UiNodeEvents | Dict[str, UiInputEvent]

# UI节点基类
class UiNode:
    """
    UI节点的基类。
    """
    name: str
    children: List['UiNode']
    parent: Optional['UiNode']

    def findChildByName(self, name: str) -> Optional['UiNode']:
        """
        通过名称查找子节点。
        """
        ...

    events: EventEmitter[UiNodeEvents]

    uiScale: Optional['UiScale']

    def clone(self) -> 'UiNode':
        """
        克隆当前UI节点。
        """
        ...

# 可渲染的UI节点
class UiRenderable(UiNode):
    """
    可以渲染的UI节点。
    """
    anchor: Vec2
    position: Coord2
    backgroundColor: Vec3
    backgroundOpacity: float
    size: Coord2
    zIndex: int
    autoResize: str
    visible: bool
    pointerEventBehavior: 'PointerEventBehavior'

# 特定的UI元素
class UiBox(UiRenderable):
    """
    Box UI元素。
    """
    def __init__(self) -> None:
        ...

    @staticmethod
    def create() -> 'UiBox':
        """
        创建新的UiBox实例。
        """
        ...

class UiText(UiRenderable):
    """
    文本UI元素。
    """
    textContent: str
    textFontSize: int
    textColor: Vec3
    textXAlignment: str
    textYAlignment: str
    autoWordWrap: bool
    textLineHeight: int

    @staticmethod
    def create() -> 'UiText':
        """
        创建新的UiText实例。
        """
        ...

class UiInput(UiText):
    """
    输入UI元素。
    """
    placeholder: str
    placeholderColor: Vec3
    placeholderOpacity: float
    isFocus: bool

    def focus(self) -> None:
        """
        设置输入元素的焦点。
        """
        ...

    def blur(self) -> str:
        """
        移除输入元素的焦点。
        """
        ...

    @staticmethod
    def create() -> 'UiInput':
        """
        创建新的UiInput实例。
        """
        ...

class UiImage(UiRenderable):
    """
    图像UI元素。
    """
    image: str
    imageOpacity: float

    @staticmethod
    def create() -> 'UiImage':
        """
        创建新的UiImage实例。
        """
        ...

# UI组件
class UiComponent:
    """
    UI组件的基类。
    """
    ...

class UiScale(UiComponent):
    """
    缩放其他UI元素的UI组件。
    """
    scale: float

    @staticmethod
    def create() -> 'UiScale':
        """
        创建新的UiScale实例。
        """
        ...

# 指针事件行为
class PointerEventBehavior(Enum):
    """
    指定UI元素上指针事件的行为。
    """
    DISABLE_AND_BLOCK_PASS_THROUGH = 0
    DISABLE = 1
    BLOCK_PASS_THROUGH = 2
    ENABLE = 3

# 屏幕尺寸
screenWidth: int
screenHeight: int

# 指针锁定更改事件
PointerLockChangeEvent = Dict[str, bool]

# 指针锁定事件
PointerLockEvents = Dict[str, PointerLockChangeEvent]

# 输入系统
class InputSystem:
    """
    管理UI事件和指针锁定事件的系统。
    """
    uiEvents: EventEmitter[UiNodeEvents]
    pointerLockEvents: EventEmitter[PointerLockEvents]

    def unlockPointer(self) -> None:
        """
        解锁指针。
        """
        ...

    def lockPointer(self) -> None:
        """
        锁定指针。
        """
        ...

# 全局UI节点
ui: UiNode

# 全局远程通道
remoteChannel: ClientRemoteChannel

# 异步休眠函数
async def sleep(ms: int) -> None:
    """
    暂停执行指定数量的毫秒。
    """
    ...

# 定时器函数
def setTimeout(callback: Callable[[], None], delayMs: int) -> int:
    """
    在指定数量的毫秒后调用函数。
    """
    ...

def clearTimeout(id: int) -> None:
    """
    取消之前由setTimeout设置的定时器。
    """
    ...

def setInterval(callback: Callable[[], None], intervalMs: int) -> int:
    """
    以固定间隔重复调用函数。
    """
    ...

def clearInterval(id: int) -> None:
    """
    取消之前由setInterval设置的定时器。
    """
    ...

# 全局输入系统
input: InputSystem