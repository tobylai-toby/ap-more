from typing import Any, Callable, Generic, Iterable, List, Literal, Optional, TypeVar, Union
import enum
from enum import Enum
from dataclasses import dataclass
from abc import ABC, abstractmethod

class DotDict(dict):
    def __init__(self, *args, **kwargs):
        super(DotDict, self).__init__(*args, **kwargs)
        self.__dict__=self


# Type Variables
T = TypeVar('T')
U = TypeVar('U')

# Placeholder types for game-specific entities
GameWorld = Any
GameVoxels = Any
GameAssetListEntry = Any  # Assume this is defined elsewhere
GameDatabase = Any
GameStorage = Any
GameHttpAPI = Any
GameRTC = Any
GameGUI = Any
ServerRemoteChannel = Any
GameEntity = Any

# Type Aliases
JSONValue = Union[str, int, bool, DotDict[str, 'JSONValue'], List['JSONValue']]
GameLoggerMethod = Callable[..., None]

# Enums
class GameLogLevel(enum.IntEnum):
    ERROR = 0
    WARN = 1
    INFO = 2
    DEBUG = 3

# Classes
class GameConsole:
    def __init__(self, log: Callable[[GameLogLevel, str], None], clear: Callable[[], None]) -> None:
        self.log = log
        self.clear = clear

    def assert_(self, assertion: Any, *args: Any) -> None:
        ...

    def log(self, *args: Any) -> None:
        ...

    def debug(self, *args: Any) -> None:
        ...

    def error(self, *args: Any) -> None:
        ...

    def warn(self, *args: Any) -> None:
        ...

# Interfaces
class GUIData:
    name: str
    attributes: Optional[DotDict[str, Union[str, int]]] = None
    children: Optional[List['GUIData']] = None

class GUIBind:
    event: str
    selector: Optional[str] = None
    action: T

class GUIBindDefinition:
    drag: DotDict[str, str]
    show: DotDict[str, T]
    remove: DotDict[str, str]
    sendMessage: DotDict[str, List[str]]
    clipboardWrite: DotDict[str, str]

GUIBindTypeMap = DotDict[str, GUIBind]
GUIBindTypes = TypeVar('GUIBindTypes', bound=GUIBind)

class GUIConfigItem:
    display: Optional[bool] = None
    bindings: Optional[List[GUIBindTypes]] = None
    data: Union[str, GUIData]

GUIConfig = DotDict[str, GUIConfigItem]

# Global Objects
class ConsoleModule:
    assert_ = lambda *args: ...
    log = lambda *args: ...
    debug = lambda *args: ...
    error = lambda *args: ...
    warn = lambda *args: ...
    clear = lambda: ...

console = ConsoleModule()

world = GameWorld()
voxels = GameVoxels()
resources = type('', (), {'ls': lambda path=None: []})()
db = GameDatabase()
storage = GameStorage()
http = GameHttpAPI()
rtc = GameRTC()
gui = GameGUI()
remoteChannel = ServerRemoteChannel()

# Function
def sleep(ms: int) -> None:
    ...

# Type
TeleportType = Callable[[str, List[GameEntity]], None]

class GameSoundEffectConfig:
    def __init__(
        self,
        sample: str,
        radius: float,
        gain: float,
        gainRange: float,
        pitch: float,
        pitchRange: float,
    ) -> None:
        self.sample = sample
        self.radius = radius
        self.gain = gain
        self.gainRange = gainRange
        self.pitch = pitch
        self.pitchRange = pitchRange

# Class
class GameSoundEffect(GameSoundEffectConfig):
    pass

from typing import Any, Callable, List, Optional, Union
import enum


# Placeholder classes for game-specific entities
class GameEntity:
    pass

class GameTriggerEvent:
    pass

class GameEventChannel:
    pass

class GameEventFuture:
    pass

class GameBounds3:
    pass

class GameSelectorString:
    pass

class GameVector3:
    pass

class GameRGBColor:
    pass

class GameRGBAColor:
    pass

class GameAnimationEvent:
    pass

# Enums
class GameAnimationPlaybackState(enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    FINISHED = "finished"

class GameAnimationDirection(enum.Enum):
    NORMAL = "normal"
    REVERSE = "reverse"
    WRAP = "wrap"
    WRAP_REVERSE = "wrap-reverse"
    ALTERNATE = "alternate"
    ALTERNATE_REVERSE = "alternate-reverse"

class GameEasing(enum.Enum):
    NONE = "none"
    LINEAR = "linear"
    QUADRATIC = "quadratic"
    SINE = "sine"
    EXP = "exp"
    BACK = "back"
    ELASTIC = "elastic"
    BOUNCE = "bounce"
    CIRCLE = "circle"

# Classes
class GameZone:
    def __init__(self,
                 entities: Callable[[], List[GameEntity]],
                 onEnter: GameEventChannel,
                 nextEnter: GameEventFuture,
                 onLeave: GameEventChannel,
                 nextLeave: GameEventFuture,
                 remove: Callable[[], None],
                 bounds: Any,
                 selector: Any,
                 massScale: float,
                 force: Any,
                 fogEnabled: bool,
                 fogColor: Any,
                 fogStartDistance: float,
                 fogHeightOffset: float,
                 fogHeightFalloff: float,
                 fogDensity: float,
                 fogMax: float,
                 snowEnabled: bool,
                 snowDensity: float,
                 snowSizeLo: float,
                 snowSizeHi: float,
                 snowFallSpeed: float,
                 snowSpinSpeed: float,
                 snowColor: Any,
                 snowTexture: str,
                 rainEnabled: bool,
                 rainDensity: float,
                 rainDirection: Any,
                 rainSpeed: float,
                 rainSizeLo: float,
                 rainSizeHi: float,
                 rainInterference: float,
                 rainColor: Any,
                 skyEnabled: bool,
                 skyMode: str,
                 skySunPhase: float,
                 skySunFrequency: float,
                 skyLunarPhase: float,
                 skySunDirection: Any,
                 skySunLight: Any,
                 skyLeftLight: Any,
                 skyRightLight: Any,
                 skyBottomLight: Any,
                 skyTopLight: Any,
                 skyFrontLight: Any,
                 skyBackLight: Any):

        self.entities = entities
        self.onEnter = onEnter
        self.nextEnter = nextEnter
        self.onLeave = onLeave
        self.nextLeave = nextLeave
        self.remove = remove
        self.bounds = bounds
        self.selector = selector
        self.massScale = massScale
        self.force = force
        self.fogEnabled = fogEnabled
        self.fogColor = fogColor
        self.fogStartDistance = fogStartDistance
        self.fogHeightOffset = fogHeightOffset
        self.fogHeightFalloff = fogHeightFalloff
        self.fogDensity = fogDensity
        self.fogMax = fogMax
        self.snowEnabled = snowEnabled
        self.snowDensity = snowDensity
        self.snowSizeLo = snowSizeLo
        self.snowSizeHi = snowSizeHi
        self.snowFallSpeed = snowFallSpeed
        self.snowSpinSpeed = snowSpinSpeed
        self.snowColor = snowColor
        self.snowTexture = snowTexture
        self.rainEnabled = rainEnabled
        self.rainDensity = rainDensity
        self.rainDirection = rainDirection
        self.rainSpeed = rainSpeed
        self.rainSizeLo = rainSizeLo
        self.rainSizeHi = rainSizeHi
        self.rainInterference = rainInterference
        self.rainColor = rainColor
        self.skyEnabled = skyEnabled
        self.skyMode = skyMode
        self.skySunPhase = skySunPhase
        self.skySunFrequency = skySunFrequency
        self.skyLunarPhase = skyLunarPhase
        self.skySunDirection = skySunDirection
        self.skySunLight = skySunLight
        self.skyLeftLight = skyLeftLight
        self.skyRightLight = skyRightLight
        self.skyBottomLight = skyBottomLight
        self.skyTopLight = skyTopLight
        self.skyFrontLight = skyFrontLight
        self.skyBackLight = skyBackLight

# Type alias
GameZoneConfig = dict

class GameAnimation:
    def __init__(self,
                 target: Any,
                 keyframes: Callable[[], List[Any]],
                 play: Callable[[Optional[dict]], None],
                 cancel: Callable[[], None],
                 onReady: Any,
                 nextReady: Any,
                 onFinish: Any,
                 nextFinish: Any,
                 currentTime: Callable[[], int],
                 startTime: Callable[[], int],
                 playState: Callable[[], GameAnimationPlaybackState],
                 playbackRate: Callable[[], int]):

        self.target = target
        self.keyframes = keyframes
        self.play = play
        self.cancel = cancel
        self.onReady = onReady
        self.nextReady = nextReady
        self.onFinish = onFinish
        self.nextFinish = nextFinish
        self.currentTime = currentTime()
        self.startTime = startTime()
        self.playState = playState()
        self.playbackRate = playbackRate()

    def then(self, resolve: Callable[[Any], Any], reject: Optional[Callable[[Any], Any]] = None):
        # Implementation would go here if required
        pass

# Interface
class GameWorldKeyframe:
    def __init__(self,
                 duration: int,
                 easeIn: GameEasing,
                 easeOut: GameEasing,
                 fogColor: GameRGBColor,
                 fogStartDistance: float,
                 fogHeightOffset: float,
                 fogHeightFalloff: float,
                 fogUniformDensity: float,
                 maxFog: float,
                 lightMode: str,
                 sunPhase: float,
                 sunFrequency: float,
                 lunarPhase: float,
                 sunDirection: GameVector3,
                 sunLight: GameRGBColor,
                 skyLeftLight: GameRGBColor,
                 skyRightLight: GameRGBColor,
                 skyBottomLight: GameRGBColor,
                 skyTopLight: GameRGBColor,
                 skyFrontLight: GameRGBColor,
                 skyBackLight: GameRGBColor,
                 rainDensity: float,
                 rainDirection: GameVector3,
                 rainSpeed: float,
                 rainSizeLo: float,
                 rainSizeHi: float,
                 rainInterference: float,
                 rainColor: GameRGBAColor,
                 snowDensity: float,
                 snowSizeLo: float,
                 snowSizeHi: float,
                 snowFallSpeed: float,
                 snowSpinSpeed: float,
                 snowColor: GameRGBAColor,
                 snowTexture: str,
                 gravity: float,
                 airFriction: float):
        self.duration = duration
        self.easeIn = easeIn
        self.easeOut = easeOut
        self.fogColor = fogColor
        self.fogStartDistance = fogStartDistance
        self.fogHeightOffset = fogHeightOffset
        self.fogHeightFalloff = fogHeightFalloff
        self.fogUniformDensity = fogUniformDensity
        self.maxFog = maxFog
        self.lightMode = lightMode
        self.sunPhase = sunPhase
        self.sunFrequency = sunFrequency
        self.lunarPhase = lunarPhase
        self.sunDirection = sunDirection
        self.sunLight = sunLight
        self.skyLeftLight = skyLeftLight
        self.skyRightLight = skyRightLight
        self.skyBottomLight = skyBottomLight
        self.skyTopLight = skyTopLight
        self.skyFrontLight = skyFrontLight
        self.skyBackLight = skyBackLight
        self.rainDensity = rainDensity
        self.rainDirection = rainDirection
        self.rainSpeed = rainSpeed
        self.rainSizeLo = rainSizeLo
        self.rainSizeHi = rainSizeHi
        self.rainInterference = rainInterference
        self.rainColor = rainColor
        self.snowDensity = snowDensity
        self.snowSizeLo = snowSizeLo
        self.snowSizeHi = snowSizeHi
        self.snowFallSpeed = snowFallSpeed
        self.snowSpinSpeed = snowSpinSpeed
        self.snowColor = snowColor
        self.snowTexture = snowTexture
        self.gravity = gravity
        self.airFriction = airFriction

class Sound:
    def __init__(self,
                 resume: Callable[[Optional[int]], None],
                 setCurrentTime: Callable[[int], None],
                 pause: Callable[[], None],
                 stop: Callable[[], None]):
        self.resume = resume
        self.setCurrentTime = setCurrentTime
        self.pause = pause
        self.stop = stop



# Placeholder for specific types that are not defined in the original TypeScript code
URL = str
GameVector3 = List[float]
GameBounds3 = List[float]
GameEntity = object
GameEntityConfig = DotDict[str, object]
GameSelectorString = str
GameRaycastOptions = DotDict[str, object]
GameRaycastResult = object
GameWorldKeyframe = DotDict[str, object]
GameEntityKeyframe = DotDict[str, object]
GamePlayerKeyframe = DotDict[str, object]
GameTickEvent = object
GameDamageEvent = object
GameDieEvent = object
GamePlayerEntityEvent = object
GameEntityEvent = object
GameChatEvent = object
GameClickEvent = object
GameInputEvent = object
GameEntityContactEvent = object
GameVoxelContactEvent = object
GameFluidContactEvent = object
GameInteractEvent = object
GamePurchaseSuccessEvent = object
Sound = object
TeleportType = Callable[..., object]

# Event Channel and Future are placeholders for event handling mechanisms
class GameEventChannel:
    def __init__(self, event_type):
        self.event_type = event_type

class GameEventFuture:
    def __init__(self, event_type):
        super().__init__()
        self.event_type = event_type

# GameWorld class definition
class GameWorld:
    lightMode: str
    sunPhase: float
    sunFrequency: float
    lunarPhase: float
    sunDirection: GameVector3
    sunLight: GameRGBColor
    skyLeftLight: GameRGBColor
    skyRightLight: GameRGBColor
    skyBottomLight: GameRGBColor
    skyTopLight: GameRGBColor
    skyFrontLight: GameRGBColor
    skyBackLight: GameRGBColor
    fogColor: GameRGBColor
    fogStartDistance: float
    fogHeightOffset: float
    fogHeightFalloff: float
    fogUniformDensity: float
    maxFog: float
    snowDensity: float
    snowSizeLo: float
    snowSizeHi: float
    snowFallSpeed: float
    snowSpinSpeed: float
    snowColor: GameRGBAColor
    snowTexture: str
    rainDensity: float
    rainDirection: GameVector3
    rainSpeed: float
    rainSizeLo: float
    rainSizeHi: float
    rainInterference: float
    rainColor: GameRGBAColor
    gravity: float
    airFriction: float
    useOBB: bool
    breakVoxelSound: GameSoundEffect
    placeVoxelSound: GameSoundEffect
    playerJoinSound: GameSoundEffect
    playerLeaveSound: GameSoundEffect
    ambientSound: GameSoundEffect
    onChat: GameEventChannel[GameChatEvent]
    nextChat: GameEventFuture[GameChatEvent]
    onClick: GameEventChannel[GameClickEvent]
    nextClick: GameEventFuture[GameClickEvent]
    onPress: GameEventChannel[GameInputEvent]
    nextPress: GameEventFuture[GameInputEvent]
    onRelease: GameEventChannel[GameInputEvent]
    nextRelease: GameEventFuture[GameInputEvent]
    onEntityContact: GameEventChannel[GameEntityContactEvent]
    nextEntityContact: GameEventFuture[GameEntityContactEvent]
    onEntitySeparate: GameEventChannel[GameEntityContactEvent]
    nextEntitySeparate: GameEventFuture[GameEntityContactEvent]
    onVoxelContact: GameEventChannel[GameVoxelContactEvent]
    nextVoxelContact: GameEventFuture[GameVoxelContactEvent]
    onVoxelSeparate: GameEventChannel[GameVoxelContactEvent]
    nextVoxelSeparate: GameEventFuture[GameVoxelContactEvent]
    onFluidEnter: GameEventChannel[GameFluidContactEvent]
    nextFluidEnter: GameEventFuture[GameFluidContactEvent]
    onFluidLeave: GameEventChannel[GameFluidContactEvent]
    nextFluidLeave: GameEventFuture[GameFluidContactEvent]
    zones: Callable[[], List[GameZone]]
    addZone: Callable[[DotDict[str, Any]], GameZone]
    removeZone: Callable[[GameZone], None]
    onInteract: GameEventChannel[GameInteractEvent]
    nextInteract: GameEventFuture[GameInteractEvent]
    onPlayerPurchaseSuccess: GameEventChannel[GamePurchaseSuccessEvent]
    nextPlayerPurchaseSuccess: GameEventFuture[GamePurchaseSuccessEvent]
    sound: Callable[[Union[DotDict[str, Any], str]], Sound]
    teleport=TeleportType
    createTempChat: Callable[[Optional[List[str]]], str]
    destroyTempChat: Callable[[List[str]], List[str]]
    addTempChatPlayer: Callable[[str, List[str]], List[str]]
    removeTempChatPlayer: Callable[[str, List[str]], List[str]]
    getTempChats: Callable[[], List[str]]
    getTempChatUsers: Callable[[str], List[str]]
    def __init__(self):
        self.url = URL
        self.entityQuota = lambda: int
        self.onRespawn = GameEventChannel(GameRespawnEvent)
        self.nextRespawn = GameEventFuture(GameRespawnEvent)
        self.createEntity = lambda config: Optional[Union[GameEntity, None]]
        self.querySelector = lambda selector: Optional[GameEntity]
        self.querySelectorAll = lambda selector: List[GameEntity]
        self.testSelector = lambda selector, entity: bool
        self.addCollisionFilter = lambda aSelector, bSelector: None
        self.removeCollisionFilter = lambda aSelector, bSelector: None
        self.clearCollisionFilters = lambda: None
        self.collisionFilters = lambda: List[List[str]]
        self.raycast = lambda origin, direction, options=None: GameRaycastResult
        self.searchBox = lambda bounds: List[GameEntity]
        self.animate = lambda keyframes, playbackInfo=None: GameAnimation
        self.getAnimations = lambda: List[GameAnimation]
        self.getEntityAnimations = lambda: List[GameAnimation]
        self.getPlayerAnimations = lambda: List[GameAnimation]
        self.onTick = GameEventChannel(GameTickEvent)
        self.nextTick = GameEventFuture(GameTickEvent)
        self.onTakeDamage = GameEventChannel(GameDamageEvent)
        self.nextTakeDamage = GameEventFuture(GameDamageEvent)
        self.onDie = GameEventChannel(GameDieEvent)
        self.nextDie = GameEventFuture(GameDieEvent)
        self.onPlayerJoin = GameEventChannel(GamePlayerEntityEvent)
        self.nextPlayerJoin = GameEventFuture(GamePlayerEntityEvent)
        self.onPlayerLeave = GameEventChannel(GamePlayerEntityEvent)
        self.nextPlayerLeave = GameEventFuture(GamePlayerEntityEvent)
        self.onEntityCreate = GameEventChannel(GameEntityEvent)
        self.nextEntityCreate = GameEventFuture(GameEntityEvent)
        self.onEntityDestroy = GameEventChannel(GameEntityEvent)
        self.nextEntityDestroy = GameEventFuture(GameEntityEvent)
        self.say = lambda message: None
        self.onChat = GameEventChannel(GameChatEvent)
        self.nextChat = GameEventFuture(GameChatEvent)
        self.onClick = GameEventChannel(GameClickEvent)
        self.nextClick = GameEventFuture(GameClickEvent)
        self.onPress = GameEventChannel(GameInputEvent)
        self.nextPress = GameEventFuture(GameInputEvent)
        self.onRelease = GameEventChannel(GameInputEvent)
        self.nextRelease = GameEventFuture(GameInputEvent)
        self.onEntityContact = GameEventChannel(GameEntityContactEvent)
        self.nextEntityContact = GameEventFuture(GameEntityContactEvent)
        self.onEntitySeparate = GameEventChannel(GameEntityContactEvent)
        self.nextEntitySeparate = GameEventFuture(GameEntityContactEvent)
        self.onVoxelContact = GameEventChannel(GameVoxelContactEvent)
        self.nextVoxelContact = GameEventFuture(GameVoxelContactEvent)
        self.onVoxelSeparate = GameEventChannel(GameVoxelContactEvent)
        self.nextVoxelSeparate = GameEventFuture(GameVoxelContactEvent)
        self.onFluidEnter = GameEventChannel(GameFluidContactEvent)
        self.nextFluidEnter = GameEventFuture(GameFluidContactEvent)
        self.onFluidLeave = GameEventChannel(GameFluidContactEvent)
        self.nextFluidLeave = GameEventFuture(GameFluidContactEvent)
        self.zones = lambda: List[GameZone]
        self.addZone = lambda config: GameZone
        self.removeZone = lambda trigger: None
        self.onInteract = GameEventChannel(GameInteractEvent)
        self.nextInteract = GameEventFuture(GameInteractEvent)
        self.onPlayerPurchaseSuccess = GameEventChannel(GamePurchaseSuccessEvent)
        self.nextPlayerPurchaseSuccess = GameEventFuture(GamePurchaseSuccessEvent)
        self.sound = lambda spec: Sound
        self.teleport = TeleportType
        self.createTempChat = lambda userIds=None: Any
        self.destroyTempChat = lambda chatIds: Any
        self.addTempChatPlayer = lambda chatId, userIds: Any
        self.removeTempChatPlayer = lambda chatId, userIds: Any
        self.getTempChats = lambda: Any
        self.getTempChatUsers = lambda chatId: Any
        self.projectName = str
        self.currentTick = int

# Placeholder for GameZone class as it is referenced but not defined in the provided TypeScript snippet
class GameZone:
    pass

# Placeholder for GameAnimation class as it is referenced but not defined in the provided TypeScript snippet
class GameAnimation:
    pass

# Placeholder for GameRespawnEvent class as it is referenced but not defined in the provided TypeScript snippet
class GameRespawnEvent:
    pass

# ... [Previous Python class definition goes here]

class GameVoxels:
    shape: GameVector3
    VoxelTypes: list[str]
    id: Callable[[str], int]
    name: Callable[[int], str]
    setVoxel: Callable[[int, int, int, int | str, int | str | None], int]
    getVoxel: Callable[[int, int, int], int]
    getVoxelRotation: Callable[[int, int, int], int]
    setVoxelId: Callable[[int, int, int, int], int]
    getVoxelId: Callable[[int, int, int], int]

    def __init__(
        self,
        shape: GameVector3,
        VoxelTypes: list[str],
        id: Callable[[str], int],
        name: Callable[[int], str],
        setVoxel: Callable[[int, int, int, int | str, int | str | None], int],
        getVoxel: Callable[[int, int, int], int],
        getVoxelRotation: Callable[[int, int, int], int],
        setVoxelId: Callable[[int, int, int, int], int],
        getVoxelId: Callable[[int, int, int], int]
    ):
        ...


# GamePlayerEntity 结合了 GameEntity 和额外的 player 属性
class GamePlayerEntity(GameEntity):
    player: 'GamePlayer'
    isPlayer: bool

# GamePlayerEntityEvent 结合了 GameEntityEvent 并具有 GamePlayerEntity 类型的 entity 属性
class GamePlayerEntityEvent(GameEntityEvent):
    entity: GamePlayerEntity

# 实体配置接口
class GameEntityConfig:
    position: GameVector3
    velocity: GameVector3
    bounds: GameVector3
    mass: float
    friction: float
    restitution: float
    collides: bool
    fixed: bool
    gravity: bool
    mesh: str
    meshColor: GameRGBAColor
    meshScale: GameVector3
    meshOrientation: 'GameQuaternion'
    meshMetalness: float
    meshEmissive: float
    meshShininess: float
    particleRate: float
    particleRateSpread: float
    particleLimit: int
    particleColor: List[GameRGBColor]
    particleSize: List[float]
    particleSizeSpread: float
    particleLifetime: float
    particleLifetimeSpread: float
    particleVelocity: GameVector3
    particleVelocitySpread: GameVector3
    particleDamping: float
    particleAcceleration: GameVector3
    particleNoise: float
    particleNoiseFrequency: float
    particleTarget: Union['GameEntity', None]
    particleTargetWeight: float
    enableInteract: bool
    interactColor: GameRGBColor
    interactHint: str
    interactRadius: float
    hurtSound: GameSoundEffectConfig
    dieSound: GameSoundEffectConfig
    interactSound: GameSoundEffectConfig
    chatSound: GameSoundEffectConfig
    id: str
    tags: Union[Callable[[], List[str]], List[str]]

# 伤害选项接口
class GameHurtOptions:
    attacker: 'GameEntity'
    damageType: str

class GameEntity(GameEntityConfig):
    tags: Callable[[], List[str]]
    addTag: Callable[[str], None]
    removeTag: Callable[[str], None]
    hasTag: Callable[[str], bool]
    destroy: Callable[[], None]
    onDestroy: GameEventChannel['GameEntityEvent']
    nextDestroy: GameEventFuture['GameEntityEvent']
    onTakeDamage: GameEventChannel[GameDamageEvent]
    nextTakeDamage: GameEventFuture[GameDamageEvent]
    onDie: GameEventChannel[GameDieEvent]
    nextDie: GameEventFuture[GameDieEvent]
    hurt: Callable[[float, Optional[dict]], None]
    say: Callable[[str], None]
    animate: Callable[[List[GameEntityKeyframe], Optional['GameAnimationPlaybackConfig']], GameAnimation[GameEntityKeyframe, 'GameEntity']]
    getAnimations: Callable[[], List[GameAnimation[GameEntityKeyframe, 'GameEntity']]]
    onClick: GameEventChannel[GameClickEvent]
    nextClick: GameEventFuture[GameClickEvent]
    onEntityContact: GameEventChannel[GameEntityContactEvent]
    nextEntityContact: GameEventFuture[GameEntityContactEvent]
    onEntitySeparate: GameEventChannel[GameEntityContactEvent]
    nextEntitySeparate: GameEventFuture[GameEntityContactEvent]
    onVoxelContact: GameEventChannel[GameVoxelContactEvent]
    nextVoxelContact: GameEventFuture[GameVoxelContactEvent]
    onVoxelSeparate: GameEventChannel[GameVoxelContactEvent]
    nextVoxelSeparate: GameEventFuture[GameVoxelContactEvent]
    onFluidEnter: GameEventChannel[GameFluidContactEvent]
    nextFluidEnter: GameEventFuture[GameFluidContactEvent]
    onFluidLeave: GameEventChannel[GameFluidContactEvent]
    nextFluidLeave: GameEventFuture[GameFluidContactEvent]
    onInteract: GameEventChannel[GameInteractEvent]
    nextInteract: GameEventFuture[GameInteractEvent]
    sound: Callable[[Union[dict, str]], 'Sound']
    motion: "GameMotionController['GameEntity']"
    lookAt: Callable[[GameVector3, Optional[str], Optional[GameVector3]], None]

    def __init__(
        self,
        tags: Callable[[], List[str]],
        addTag: Callable[[str], None],
        removeTag: Callable[[str], None],
        hasTag: Callable[[str], bool],
        destroy: Callable[[], None],
        onDestroy: GameEventChannel['GameEntityEvent'], 
        nextDestroy: GameEventFuture['GameEntityEvent'],
        onTakeDamage: GameEventChannel[GameDamageEvent], 
        nextTakeDamage: GameEventFuture[GameDamageEvent],
        onDie: GameEventChannel[GameDieEvent], 
        nextDie: GameEventFuture[GameDieEvent],
        hurt: Callable[[float, Optional[dict]], None],
        say: Callable[[str], None],
        animate: Callable[[List[GameEntityKeyframe], Optional['GameAnimationPlaybackConfig']], GameAnimation[GameEntityKeyframe, 'GameEntity']],
        getAnimations: Callable[[], List[GameAnimation[GameEntityKeyframe, 'GameEntity']]],
        onClick: GameEventChannel[GameClickEvent], 
        nextClick: GameEventFuture[GameClickEvent],
        onEntityContact: GameEventChannel[GameEntityContactEvent], 
        nextEntityContact: GameEventFuture[GameEntityContactEvent],
        onEntitySeparate: GameEventChannel[GameEntityContactEvent], 
        nextEntitySeparate: GameEventFuture[GameEntityContactEvent],
        onVoxelContact: GameEventChannel[GameVoxelContactEvent], 
        nextVoxelContact: GameEventFuture[GameVoxelContactEvent],
        onVoxelSeparate: GameEventChannel[GameVoxelContactEvent], 
        nextVoxelSeparate: GameEventFuture[GameVoxelContactEvent],
        onFluidEnter: GameEventChannel[GameFluidContactEvent], 
        nextFluidEnter: GameEventFuture[GameFluidContactEvent],
        onFluidLeave: GameEventChannel[GameFluidContactEvent], 
        nextFluidLeave: GameEventFuture[GameFluidContactEvent],
        onInteract: GameEventChannel[GameInteractEvent], 
        nextInteract: GameEventFuture[GameInteractEvent],
        sound: Callable[[Union[dict, str]], 'Sound'],
        motion: "GameMotionController['GameEntity']",
        lookAt: Callable[[GameVector3, Optional[str], Optional[GameVector3]], None]
    ):
        ...

class GameMotionConfig:
    name: str
    iterations: int

class GameMotionClipConfig:
    motions: List[GameMotionConfig]
    iterations: int

class GameMotionController:
    loadByName: Callable[[str | List[GameMotionConfig] | GameMotionClipConfig], 'GameMotionHandler[T]']
    pause: Callable[[], None]
    resume: Callable[[], None]
    setDefaultMotionByName: Callable[[Optional[str]], None]

    def __init__(
        self,
        loadByName: Callable[[str | List[GameMotionConfig] | GameMotionClipConfig], 'GameMotionHandler[T]'],
        pause: Callable[[], None],
        resume: Callable[[], None],
        setDefaultMotionByName: Callable[[Optional[str]], None]
    ):
        ...

class GameMotionHandler:
    target: T
    play: Callable[[], None]
    cancel: Callable[[], None]
    onFinish: GameEventChannel['GameMotionEvent[T]']
    nextFinish: GameEventFuture['GameMotionEvent[T]']

    def __init__(
        self,
        target: T,
        play: Callable[[], None],
        cancel: Callable[[], None],
        onFinish: GameEventChannel['GameMotionEvent[T]'],
        nextFinish: GameEventFuture['GameMotionEvent[T]']
    ):
        ...

class GameMotionEvent:
    tick: int
    target: T
    motionHandler: 'GameMotionHandler[T]'
    cancelled: bool

    def __init__(
        self,
        tick: int,
        target: T,
        motionHandler: 'GameMotionHandler[T]',
        cancelled: bool
    ):
        ...

class GameEntityContact:
    def __init__(self, other: 'GameEntity', force: GameVector3, axis: GameVector3):
        self.other = other
        self.force = force
        self.axis = axis

class GameVoxelContact:
    def __init__(self, x: int, y: int, z: int, voxel: int, force: GameVector3, axis: GameVector3):
        self.x = x
        self.y = y
        self.z = z
        self.voxel = voxel
        self.force = force
        self.axis = axis

class GameFluidContact:
    def __init__(self, voxel: int, volume: float):
        self.voxel = voxel
        self.volume = volume

class GamePlayerMoveState(Enum):
    FLYING = "fly"
    GROUND = "ground"
    SWIM = "swim"
    FALL = "fall"
    JUMP = "jump"
    DOUBLE_JUMP = "jump2"

class GamePlayerWalkState(Enum):
    NONE = ""
    CROUCH = "crouch"
    WALK = "walk"
    RUN = "run"

class GameBodyPart(Enum):
    HIPS = "hips"
    TORSO = "torso"
    NECK = "neck"
    HEAD = "head"
    LEFT_SHOULDER = "leftShoulder"
    LEFT_UPPER_ARM = "leftUpperArm"
    LEFT_LOWER_ARM = "leftLowerArm"
    LEFT_HAND = "leftHand"
    LEFT_UPPER_LEG = "leftUpperLeg"
    LEFT_LOWER_LEG = "leftLowerLeg"
    LEFT_FOOT = "leftFoot"
    RIGHT_SHOULDER = "rightShoulder"
    RIGHT_UPPER_ARM = "rightUpperArm"
    RIGHT_LOWER_ARM = "rightLowerArm"
    RIGHT_HAND = "rightHand"
    RIGHT_UPPER_LEG = "rightUpperLeg"
    RIGHT_LOWER_LEG = "rightLowerLeg"
    RIGHT_FOOT = "rightFoot"

GameSkinValue = Union[str, None]

GameSkin = DotDict[GameBodyPart, GameSkinValue]

GameSkinInvisible = DotDict[GameBodyPart, bool]

class GameWearable:
    def __init__(self, player: Optional['GamePlayer'], bodyPart: GameBodyPart, mesh: str, color: GameRGBColor,
                 emissive: float, metalness: float, shininess: float, orientation: 'GameQuaternion',
                 scale: GameVector3, offset: GameVector3):
        self.player = player
        self.bodyPart = bodyPart
        self.mesh = mesh
        self.color = color
        self.emissive = emissive
        self.metalness = metalness
        self.shininess = shininess
        self.orientation = orientation
        self.scale = scale
        self.offset = offset

    def remove(self):
        pass  # Implementation of removal logic


class GameDialogType(Enum):
    TEXT = "text"
    SELECT = "select"
    INPUT = "input"

GameDialogSelectResponse = DotDict[str, Union[int, str]]
GameDialogResponse = Union[GameDialogSelectResponse, str, None]

GameDialogParams = DotDict[str, Any]

GameTextDialogParams = GameDialogParams
GameSelectDialogParams = GameDialogParams
GameInputDialogParams = GameDialogParams

GameDialogCancelOption = DotDict[str, Callable[[], None]]

@dataclass
class GameTextDialogParams:
    type: GameDialogType
    content: str
    title: Optional[str] = None
    titleBackgroundColor: Optional[GameRGBAColor] = None
    titleTextColor: Optional[GameRGBAColor] = None
    contentBackgroundColor: Optional[GameRGBAColor] = None
    contentTextColor: Optional[GameRGBAColor] = None
    hasArrow: Optional[bool] = None
    lookTarget: Optional[Union[GameVector3, 'GameEntity']] = None
    lookTargetOffset: Optional[GameVector3] = None
    lookUp: Optional[GameVector3] = None
    lookEye: Optional[Union[GameVector3, 'GameEntity']] = None
    lookEyeOffset: Optional[GameVector3] = None

@dataclass
class GameSelectDialogParams:
    type: GameDialogType
    content: str
    options: List[str]
    title: Optional[str] = None
    titleBackgroundColor: Optional[GameRGBAColor] = None
    titleTextColor: Optional[GameRGBAColor] = None
    contentBackgroundColor: Optional[GameRGBAColor] = None
    contentTextColor: Optional[GameRGBAColor] = None
    lookTarget: Optional[Union[GameVector3, 'GameEntity']] = None
    lookTargetOffset: Optional[GameVector3] = None
    lookUp: Optional[GameVector3] = None
    lookEye: Optional[Union[GameVector3, 'GameEntity']] = None
    lookEyeOffset: Optional[GameVector3] = None

@dataclass
class GameInputDialogParams:
    type: GameDialogType
    content: str
    placeholder: Optional[str] = None
    confirmText: Optional[str] = None
    title: Optional[str] = None
    titleBackgroundColor: Optional[GameRGBAColor] = None
    titleTextColor: Optional[GameRGBAColor] = None
    contentBackgroundColor: Optional[GameRGBAColor] = None
    contentTextColor: Optional[GameRGBAColor] = None
    lookTarget: Optional[Union[GameVector3, 'GameEntity']] = None
    lookTargetOffset: Optional[GameVector3] = None
    lookUp: Optional[GameVector3] = None
    lookEye: Optional[Union[GameVector3, 'GameEntity']] = None
    lookEyeOffset: Optional[GameVector3] = None


class GameDialogCall:
    def __call__(self, params: Any) -> Union[str, None]:
        pass

    def cancel(self) -> None:
        pass

class GameCameraMode(Enum):
    FOLLOW = "follow"
    FPS = "fps"
    FIXED = "fixed"
    RELATIVE = "relative"

class GameCameraFreezedAxis(Enum):
    NONE = ""
    X = "x"
    Y = "y"
    Z = "z"
    XY = "xy"
    XZ = "xz"
    YZ = "yz"
    XYZ = "xyz"

class GameInputDirection(Enum):
    NONE = "none"
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"
    BOTH = "both"

class GamePlayerKeyframe:
    def __init__(
        self,
        duration: int,
        easeIn: GameEasing,
        easeOut: GameEasing,
        scale: float,
        color: GameRGBColor,
        metalness: float,
        emissive: float,
        shininess: float,
        invisible: bool,
        showName: bool,
        showIndicator: bool,
        colorLUT: str,
        cameraMode: GameCameraMode,
        cameraEntity: Optional[GameEntity],
        cameraTarget: GameVector3,
        cameraUp: GameVector3,
        cameraPosition: GameVector3,
        cameraFreezedAxis: GameCameraFreezedAxis,
        cameraFovY: float,
        cameraDistance: float
    ):
        self.duration = duration
        self.easeIn = easeIn
        self.easeOut = easeOut
        self.scale = scale
        self.color = color
        self.metalness = metalness
        self.emissive = emissive
        self.shininess = shininess
        self.invisible = invisible
        self.showName = showName
        self.showIndicator = showIndicator
        self.colorLUT = colorLUT
        self.cameraMode = cameraMode
        self.cameraEntity = cameraEntity
        self.cameraTarget = cameraTarget
        self.cameraUp = cameraUp
        self.cameraPosition = cameraPosition
        self.cameraFreezedAxis = cameraFreezedAxis
        self.cameraFovY = cameraFovY
        self.cameraDistance = cameraDistance

class PlayerNavigator:
    pass


class GamePlayer:
    def __init__(self, name: str, userId: str, userKey: str, url: str, **kwargs):
        self.name = name
        self.userId = userId
        self.userKey = userKey
        self.url = url
        self.dead = False
        self.cameraMode = GameCameraMode.FOLLOW
        self.cameraEntity = None
        self.cameraTarget = GameVector3()
        self.cameraUp = GameVector3()
        self.cameraPosition = GameVector3()
        self.cameraFreezedAxis = GameCameraFreezedAxis.NONE
        self.cameraFovY = 60.0
        self.cameraDistance = 5.0
        self.canFly = False
        self.spectator = False
        self.walkSpeed = 5.0
        self.walkAcceleration = 0.5
        self.runSpeed = 10.0
        self.runAcceleration = 1.0
        self.crouchSpeed = 2.5
        self.crouchAcceleration = 0.25
        self.swimSpeed = 3.0
        self.swimAcceleration = 0.2
        self.flySpeed = 10.0
        self.flyAcceleration = 1.0
        self.jumpSpeedFactor = 1.0
        self.jumpAccelerationFactor = 0.5
        self.jumpPower = 10.0
        self.doubleJumpPower = 5.0
        self.freezedForwardDirection = None
        self.moveState = None
        self.walkState = None
        self.swapInputDirection = False
        self.reverseInputDirection = None
        self.disableInputDirection = None
        self.walkButton = False
        self.crouchButton = False
        self.jumpButton = False
        self.enableAction0 = True
        self.enableAction1 = True
        self.action0Button = False
        self.action1Button = False
        self.enableJump = True
        self.enableDoubleJump = True
        self.enableCrouch = True
        self.enable3DCursor = True
        self.facingDirection = GameVector3()
        self.cameraYaw = 0.0
        self.cameraPitch = 0.0
        self.spawnSound = GameSoundEffect()
        self.jumpSound = GameSoundEffect()
        self.doubleJumpSound = GameSoundEffect()
        self.landSound = GameSoundEffect()
        self.crouchSound = GameSoundEffect()
        self.stepSound = GameSoundEffect()
        self.swimSound = GameSoundEffect()
        self.action0Sound = GameSoundEffect()
        self.action1Sound = GameSoundEffect()
        self.enterWaterSound = GameSoundEffect()
        self.leaveWaterSound = GameSoundEffect()
        self.startFlySound = GameSoundEffect()
        self.stopFlySound = GameSoundEffect()
        self.music = GameSoundEffect()
        self.muted = False
        self.skin = GameSkin()
        self.skinInvisible = GameSkinInvisible()
        self.navigator = PlayerNavigator()

    def directMessage(self, message: str) -> None:
        # 实现直接向玩家发送私人消息的功能
        pass

    def onChat(self, callback: Callable[[str], None]) -> None:
        # 实现聊天事件监听器
        pass

    def onPress(self, callback: Callable[[str], None]) -> None:
        # 实现按钮按下事件监听器
        pass

    def onRelease(self, callback: Callable[[str], None]) -> None:
        # 实现按钮释放事件监听器
        pass

    def onRespawn(self, callback: Callable[[], None]) -> None:
        # 实现重生事件监听器
        pass

    def forceRespawn(self) -> None:
        # 实现强制重生功能
        pass

    def dialog(self, params: dict) -> None:
        # 实现打开对话框功能
        pass

    def cancelDialogs(self) -> None:
        # 实现取消所有打开的对话框功能
        pass

    def link(self, href: str, options: Optional[dict] = None) -> None:
        # 实现打开网页链接功能
        pass

    def wearables(self, bodyPart: Optional[str] = None) -> List[GameWearable]:
        # 实现列出玩家穿戴物品功能
        return []

    def addWearable(self, spec: dict) -> GameWearable:
        # 实现添加穿戴物品功能
        return GameWearable()

    def removeWearable(self, wearable: GameWearable) -> None:
        # 实现移除穿戴物品功能
        pass

    def setSkinByName(self, skinName: str) -> None:
        # 实现按名称设置皮肤功能
        pass

    def resetToDefaultSkin(self) -> None:
        # 实现重置为默认皮肤功能
        pass

    def clearSkin(self) -> None:
        # 实现清除自定义皮肤功能
        pass

    def sound(self, spec: Union[str, dict]) -> GameSoundEffect:
        # 实现播放声音效果功能
        return GameSoundEffect()

    def animate(self, keyframes: List[dict], playbackConfig: Optional[dict] = None) -> None:
        # 实现播放动画功能
        pass

    def getAnimations(self) -> List[dict]:
        # 实现获取当前动画列表功能
        return []

    def kick(self) -> None:
        # 实现踢出玩家功能
        pass

    def setCameraPitch(self, value: float) -> None:
        # 实现设置相机俯仰角功能
        pass

    def setCameraYaw(self, value: float) -> None:
        # 实现设置相机偏航角功能
        pass

    def openMarketplace(self, productIds: List[int]) -> None:
        # 实现打开商城功能
        pass

    def getMiaoShells(self) -> int:
        # 实现获取玩家拥有的“喵贝壳”数量功能
        return 0

    def share(self, content: str) -> None:
        # 实现分享内容功能
        pass

    def openUserProfileDialog(self, userId: int) -> None:
        # 实现打开用户资料对话框功能
        pass

    def querySocial(self, socialType: str) -> List[int]:
        # 实现查询社交关系功能
        return []

    # 其他属性和方法根据需要添加...

NavigatorEventType = 'message'

class PlayerNavigator:
    def __init__(self, emitEvent: Callable[[str, Any], None], 
                 addEventListener: Callable[[str, Callable[[Any], None]], None], 
                 dispatchEvent: Callable[[str, Any], None]):
        self.emitEvent = emitEvent
        self.addEventListener = addEventListener
        self.dispatchEvent = dispatchEvent


class GameRaycastResult:
    def __init__(self, hit: bool, hitEntity: Optional[GameEntity], hitVoxel: int, 
                 origin: GameVector3, direction: GameVector3, distance: float, 
                 hitPosition: GameVector3, normal: GameVector3, voxelIndex: GameVector3):
        self.hit = hit
        self.hitEntity = hitEntity
        self.hitVoxel = hitVoxel
        self.origin = origin
        self.direction = direction
        self.distance = distance
        self.hitPosition = hitPosition
        self.normal = normal
        self.voxelIndex = voxelIndex


class GameRaycastOptions:
    def __init__(self, maxDistance: float, ignoreFluid: bool, ignoreVoxel: bool, 
                 ignoreEntities: bool, ignoreSelector: GameSelectorString):
        self.maxDistance = maxDistance
        self.ignoreFluid = ignoreFluid
        self.ignoreVoxel = ignoreVoxel
        self.ignoreEntities = ignoreEntities
        self.ignoreSelector = ignoreSelector

T_EventType = TypeVar('T_EventType')

@dataclass
class GameEventHandlerToken:
    cancel: Callable[[], None]
    resume: Callable[[], None]
    active: Callable[[], bool]

    def __init__(self, cancel: Callable[[], None], resume: Callable[[], None], active: Callable[[], bool]):
        ...


@dataclass
class GameTickEvent:
    tick: int
    prevTick: int
    skip: bool
    elapsedTimeMS: int

    def __init__(self, tick: int, prevTick: int, skip: bool, elapsedTimeMS: int):
        ...


@dataclass
class GameEntityEvent:
    tick: int
    entity: Any  # Replace with proper type

    def __init__(self, tick: int, entity: Any):  # Replace with proper type
        ...


@dataclass
class GameTriggerEvent:
    tick: int
    entity: Any  # Replace with proper type

    def __init__(self, tick: int, entity: Any):  # Replace with proper type
        ...


@dataclass
class GameDamageEvent:
    tick: int
    entity: Any  # Replace with proper type
    damage: float
    attacker: Optional[Any]  # Replace with proper type
    damageType: str

    def __init__(self, tick: int, entity: Any, damage: float, attacker: Optional[Any], damageType: str):
        ...


@dataclass
class GameDieEvent:
    tick: int
    entity: Any  # Replace with proper type
    attacker: Optional[Any]  # Replace with proper type
    damageType: str

    def __init__(self, tick: int, entity: Any, attacker: Optional[Any], damageType: str):
        ...


@dataclass
class GameRespawnEvent:
    tick: int
    entity: Any  # Replace with proper type

    def __init__(self, tick: int, entity: Any):  # Replace with proper type
        ...


@dataclass
class GameEntityContactEvent:
    tick: int
    entity: Any  # Replace with proper type
    other: Any  # Replace with proper type
    axis: Any  # Replace with proper type
    force: Any  # Replace with proper type

    def __init__(self, tick: int, entity: Any, other: Any, axis: Any, force: Any):
        ...


@dataclass
class GameVoxelContactEvent:
    tick: int
    entity: Any  # Replace with proper type
    x: int
    y: int
    z: int
    voxel: int
    axis: Any  # Replace with proper type
    force: Any  # Replace with proper type

    def __init__(self, tick: int, entity: Any, x: int, y: int, z: int, voxel: int, axis: Any, force: Any):
        ...


@dataclass
class GameFluidContactEvent:
    tick: int
    entity: Any  # Replace with proper type
    voxel: int

    def __init__(self, tick: int, entity: Any, voxel: int):
        ...


@dataclass
class GameChatEvent:
    tick: int
    entity: Any  # Replace with proper type
    message: str

    def __init__(self, tick: int, entity: Any, message: str):
        ...


@dataclass
class GamePurchaseSuccessEvent:
    tick: int
    userId: str
    productId: int
    orderId: int

    def __init__(self, tick: int, userId: str, productId: int, orderId: int):
        ...


class GameEventChannel(Generic[T_EventType]):
    def __call__(self, handler: Callable[[T_EventType], None]) -> GameEventHandlerToken:
        ...


class GameEventFuture(Generic[T_EventType]):
    def __call__(self, filter: Optional[Callable[[T_EventType], bool]] = None) -> T_EventType:
        ...


# GameEventChannel: _GameEventChannel
# GameEventFuture: _GameEventFuture

class GameButtonType(Enum):
    WALK = "walk"
    RUN = "run"
    CROUCH = "crouch"
    JUMP = "jump"
    DOUBLE_JUMP = "jump2"
    FLY = "fly"
    ACTION0 = "action0"
    ACTION1 = "action1"

class GameInteractEvent:
    def __init__(self, tick: int, entity: GamePlayerEntity, targetEntity: GameEntity):
        self.tick = tick
        self.entity = entity
        self.targetEntity = targetEntity

class GameInputEvent:
    def __init__(self, tick: int, entity: GamePlayerEntity, position: GameVector3, button: GameButtonType, pressed: bool, raycast: GameRaycastResult):
        self.tick = tick
        self.entity = entity
        self.position = position
        self.button = button
        self.pressed = pressed
        self.raycast = raycast

class GameClickEvent:
    def __init__(self, tick: int, entity: GameEntity, clicker: GamePlayerEntity, button: GameButtonType, distance: float, clickerPosition: GameVector3, raycast: GameRaycastResult):
        self.tick = tick
        self.entity = entity
        self.clicker = clicker
        self.button = button
        self.distance = distance
        self.clickerPosition = clickerPosition
        self.raycast = raycast

class GameAnimationEvent:
    def __init__(self, tick: int, target: Any, animation: GameAnimation, cancelled: bool):
        self.tick = tick
        self.target = target
        self.animation = animation
        self.cancelled = cancelled

class GameAssetListEntry:
    def __init__(self, path: str, type: 'GameAssetType'):
        self.path = path
        self.type = type

class GameAssetType(Enum):
    VOXEL_MESH = "mesh"
    DIRECTORY = "directory"
    COLOR_LUT = "lut"
    JS_SCRIPT = "js"
    IMAGE = "image"
    PARTICLE_TEXTURE = "snow"
    SOUND = "sound"

class GameResourceSystem:
    def __init__(self, ls: Callable[[Optional[str]], List[GameAssetListEntry]]):
        self.ls = ls

class GameDatabase:
    def __init__(self):
        pass
    def sql(self,query:str,*params)->'GameQueryResult':
        pass

class GameQueryResult(object):
    def __init__(self, next: Callable[[], Tuple[bool, Any]],
                 abort: Callable[[], Tuple[bool, Any]],
                 error: Callable[[Any], Tuple[bool, Any]],
                 then: Callable[[Callable[[List[Any]], Any], Callable[[Any], Any]], None]):
        self.next = next
        self._abort = abort
        self.error = error
        self.then = then
        self.__aiter__ = lambda: self

    async def __anext__(self) -> Any:
        result = await self.next()
        if result['done']:
            raise StopAsyncIteration
        return result['value']

    async def __aenter__(self) -> 'GameQueryResult':
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self._abort()

class CommonError:
    def __init__(self, status: Any, code: int, msg: str):
        self.status = status
        self.code = code
        self.msg = msg

# T = TypeVar('T')
# U = TypeVar('U', bound=T)

# GUIConfig = DotDict[str, Any]
class GUIConfig(dict):
    # 占位的 我也不知道是啥，毕竟弃用了 ——tobylai
    pass

class GameGUIEvent:
    def __init__(self, entity: GamePlayerEntity, name: str, payload: Any):
        self.entity = entity
        self.name = name
        self.payload = payload

GameGUIEventListener = Callable[[GameGUIEvent], None]

class GameGUI:
    def __init__(self, init: Callable[[GamePlayerEntity, GUIConfig], None],
                 show: Callable[[GamePlayerEntity, str, Optional[bool]], None],
                 remove: Callable[[GamePlayerEntity, str], None],
                 get_attribute: Callable[[GamePlayerEntity, str, str], Any],
                 set_attribute: Callable[[GamePlayerEntity, str, str, Any], None],
                 on_message: Callable[[GameGUIEventListener], None]):
        self.init = init
        self.show = show
        self.remove = remove
        self.get_attribute = get_attribute
        self.set_attribute = set_attribute
        self.on_message = on_message
        self.ui = None  # Placeholder for UI instance

GameHttpFetchHeaders = DotDict[str, Union[str, List[str]]]

GameHttpFetchRequestOptions = DotDict[str, Any]

class GameHttpFetchResponse:
    def __init__(self, status: int, status_text: str, headers: GameHttpFetchHeaders,
                 json: Callable[[], Any],
                 text: Callable[[], str],
                 array_buffer: Callable[[], bytes],
                 close: Callable[[], None]):
        self.status = status
        self.statusText = status_text
        self.headers = headers
        self.json = json
        self.text = text
        self.arrayBuffer = array_buffer
        self.close = close

    @property
    def ok(self) -> bool:
        return 200 <= self.status < 300

class GameHttpRequest:
    pass

class GameHttpResponse:
    pass

GameHttpHandler = Callable[[GameHttpRequest, GameHttpResponse], None]

class GameHttpAPI:
    def __init__(self, fetch: Callable[[str, Optional[GameHttpFetchRequestOptions]],GameHttpFetchResponse]):
        self.fetch = fetch

class GameQuaternion:
    w: float
    x: float
    y: float
    z: float

    def __init__(self, w: float, x: float, y: float, z: float) -> None:
        ...

    @staticmethod
    def rotationBetween(a: GameVector3, b: GameVector3) -> 'GameQuaternion':
        ...

    @staticmethod
    def fromAxisAngle(axis: GameVector3, rad: float) -> 'GameQuaternion':
        ...

    @staticmethod
    def fromEuler(x: float, y: float, z: float) -> 'GameQuaternion':
        ...

    def set(self, w: float, x: float, y: float, z: float) -> 'GameQuaternion':
        ...

    def copy(self, q: 'GameQuaternion') -> 'GameQuaternion':
        ...

    def getAxisAngle(self) -> Tuple[GameVector3, float]:
        ...

    def rotateX(self, rad: float) -> 'GameQuaternion':
        ...

    def rotateY(self, rad: float) -> 'GameQuaternion':
        ...

    def rotateZ(self, rad: float) -> 'GameQuaternion':
        ...

    def dot(self, q: 'GameQuaternion') -> float:
        ...

    def add(self, v: 'GameQuaternion') -> 'GameQuaternion':
        ...

    def sub(self, v: 'GameQuaternion') -> 'GameQuaternion':
        ...

    def angle(self, q: 'GameQuaternion') -> float:
        ...

    def mul(self, q: 'GameQuaternion') -> 'GameQuaternion':
        ...

    def inv(self) -> 'GameQuaternion':
        ...

    def div(self, q: 'GameQuaternion') -> 'GameQuaternion':
        ...

    def slerp(self, q: 'GameQuaternion', n: float) -> 'GameQuaternion':
        ...

    def mag(self) -> float:
        ...

    def sqrMag(self) -> float:
        ...

    def normalize(self) -> 'GameQuaternion':
        ...

    def equals(self, q: 'GameQuaternion') -> bool:
        ...

    def clone(self) -> 'GameQuaternion':
        ...

    def __str__(self) -> str:
        ...

class GameVector3:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        ...

    @staticmethod
    def fromPolar(mag: float, phi: float, theta: float) -> GameVector3:
        ...

    def set(self, x: float, y: float, z: float) -> GameVector3:
        ...

    def copy(self, v: GameVector3) -> GameVector3:
        ...

    def add(self, v: GameVector3) -> GameVector3:
        ...

    def sub(self, v: GameVector3) -> GameVector3:
        ...

    def mul(self, v: GameVector3) -> GameVector3:
        ...

    def div(self, v: GameVector3) -> GameVector3:
        ...

    def addEq(self, v: GameVector3) -> GameVector3:
        ...

    def subEq(self, v: GameVector3) -> GameVector3:
        ...

    def mulEq(self, v: GameVector3) -> GameVector3:
        ...

    def divEq(self, v: GameVector3) -> GameVector3:
        ...

    def dot(self, v: GameVector3) -> float:
        ...

    def cross(self, v: GameVector3) -> GameVector3:
        ...

    def scale(self, n: float) -> GameVector3:
        ...

    def clone(self) -> GameVector3:
        ...

    def lerp(self, v: GameVector3, n: float) -> GameVector3:
        ...

    def mag(self) -> float:
        ...

    def sqrMag(self) -> float:
        ...

    def towards(self, v: GameVector3) -> GameVector3:
        ...

    def distance(self, v: GameVector3) -> float:
        ...

    def normalize(self) -> GameVector3:
        ...

    def angle(self, v: GameVector3) -> float:
        ...

    def max(self, v: GameVector3) -> GameVector3:
        ...

    def min(self, v: GameVector3) -> GameVector3:
        ...

    def exactEquals(self, v: GameVector3) -> bool:
        ...

    def equals(self, v: GameVector3) -> bool:
        ...

    def __str__(self) -> str:
        ...

class GameBounds3:
    lo: GameVector3
    hi: GameVector3

    def __init__(self, lo: GameVector3, hi: GameVector3) -> None:
        ...

    @staticmethod
    def fromPoints(*points: GameVector3) -> GameBounds3:
        ...

    def intersect(self, b: GameBounds3) -> GameBounds3:
        ...

    def contains(self, v: GameVector3) -> bool:
        ...

    def containsBounds(self, b: GameBounds3) -> bool:
        ...

    def intersects(self, b: GameBounds3) -> bool:
        ...

    def set(self, lox: float, loy: float, loz: float, hix: float, hiy: float, hiz: float) -> GameBounds3:
        ...

    def copy(self, b: GameBounds3) -> GameBounds3:
        ...

    def __str__(self) -> str:
        ...

class GameRGBAColor:
    r: float
    g: float
    b: float
    a: float

    def __init__(self, r: float, g: float, b: float, a: float) -> None:
        ...

    def set(self, r: float, g: float, b: float, a: float) -> GameRGBAColor:
        ...

    def copy(self, c: GameRGBAColor) -> GameRGBAColor:
        ...

    def add(self, rgba: GameRGBAColor) -> GameRGBAColor:
        ...

    def sub(self, rgba: GameRGBAColor) -> GameRGBAColor:
        ...

    def mul(self, rgba: GameRGBAColor) -> GameRGBAColor:
        ...

    def div(self, rgba: GameRGBAColor) -> GameRGBAColor:
        ...

    def addEq(self, rgba: GameRGBAColor) -> GameRGBAColor:
        ...

    def subEq(self, rgba: GameRGBAColor) -> GameRGBAColor:
        ...

    def mulEq(self, rgba: GameRGBAColor) -> GameRGBAColor:
        ...

    def divEq(self, rgba: GameRGBAColor) -> GameRGBAColor:
        ...

    def lerp(self, rgba: GameRGBAColor, n: float) -> GameRGBAColor:
        ...

    def blendEq(self, rgb: GameRGBColor) -> GameRGBColor:
        ...

    def equals(self, rgba: GameRGBAColor) -> bool:
        ...

    def clone(self) -> GameRGBAColor:
        ...

    def __str__(self) -> str:
        ...

class GameRGBColor:
    r: float
    g: float
    b: float

    @staticmethod
    def random() -> GameRGBColor:
        ...

    def __init__(self, r: float, g: float, b: float) -> None:
        ...

    def set(self, r: float, g: float, b: float) -> GameRGBColor:
        ...

    def copy(self, c: GameRGBColor) -> GameRGBColor:
        ...

    def add(self, rgb: GameRGBColor) -> GameRGBColor:
        ...

    def sub(self, rgb: GameRGBColor) -> GameRGBColor:
        ...

    def mul(self, rgb: GameRGBColor) -> GameRGBColor:
        ...

    def div(self, rgb: GameRGBColor) -> GameRGBColor:
        ...

    def addEq(self, rgb: GameRGBColor) -> GameRGBColor:
        ...

    def subEq(self, rgb: GameRGBColor) -> GameRGBColor:
        ...

    def mulEq(self, rgb: GameRGBColor) -> GameRGBColor:
        ...

    def divEq(self, rgb: GameRGBColor) -> GameRGBColor:
        ...

    def lerp(self, rgb: GameRGBColor, n: float) -> GameRGBColor:
        ...

    def equals(self, rgb: GameRGBColor) -> bool:
        ...

    def clone(self) -> GameRGBColor:
        ...

    def toRGBA(self) -> GameRGBAColor:
        ...

    def __str__(self) -> str:
        ...

class GameAnimationDirection(Enum):
    FORWARD = 1
    REVERSE = -1

@dataclass
class GameAnimationPlaybackConfig:
    startTick: int
    delay: int
    endDelay: int
    duration: int
    direction: GameAnimationDirection
    iterationStart: int
    iterations: int

SendClientEventType = Callable[[Union['GamePlayerEntity', List['GamePlayerEntity']], JSONValue], None]

# Class declaration for ServerRemoteChannel
class ServerRemoteChannel:
    sendClientEvent: SendClientEventType
    broadcastClientEvent: Callable[[JSONValue], None]
    onServerEvent: Any  # Placeholder for GameEventChannel type

    def __init__(
        self,
        sendClientEvent: SendClientEventType,
        broadcastClientEvent: Callable[[JSONValue], None],
        onServerEvent: Any  # Placeholder for GameEventChannel type
    ) -> None:
        ...

# Class declaration for GameRTCChannel
class GameRTCChannel:
    add: Callable[['GamePlayerEntity'], None]
    remove: Callable[['GamePlayerEntity'], None]
    unpublish: Callable[['GamePlayerEntity'], None]
    publishMicrophone: Callable[['GamePlayerEntity'], None]
    getPlayers: Callable[[], List['GamePlayerEntity']]
    destroy: Callable[[], None]
    getVolume: Callable[['GamePlayerEntity'], float]
    setVolume: Callable[['GamePlayerEntity', float], None]
    getMicrophonePermission: Callable[['GamePlayerEntity'], bool]

    def __init__(
        self,
        add: Callable[['GamePlayerEntity'], None],
        remove: Callable[['GamePlayerEntity'], None],
        unpublish: Callable[['GamePlayerEntity'], None],
        publishMicrophone: Callable[['GamePlayerEntity'], None],
        getPlayers: Callable[[], List['GamePlayerEntity']],
        destroy: Callable[[], None],
        getVolume: Callable[['GamePlayerEntity'], float],
        setVolume: Callable[['GamePlayerEntity', float], None],
        getMicrophonePermission: Callable[['GamePlayerEntity'], bool]
    ) -> None:
        ...

# Class declaration for GameRTC
class GameRTC:
    createChannel: Callable[[Optional[str]], 'GameRTCChannel']

    def __init__(self, createChannel: Callable[[Optional[str]], 'GameRTCChannel']) -> None:
        ...

# Declare type DB_ERROR_STATUS
DB_ERROR_STATUS = Literal[
    'CONSTRAINT_TARGET_INVALID',
    'PARAMS_INVALID',
    'DB_NAME_INVALID',
    'KEY_INVALID',
    'VALUE_INVALID',
    'SERVER_FETCH_ERROR',
    'REQUEST_THROTTLED',
    'UNKNOWN'
]


# Type alias for ResultValue
ResultValue = DotDict[str, Union[str, JSONValue, str, int]]

# Type alias for ListReturnValue
ListReturnValue = DotDict[str, Union[List[ResultValue], bool]]

# Type alias for ReturnValue
ReturnValue = Any  # Assuming I.ReturnValue is not specified further

# Type alias for ListPageOptions
ListPageOptions = Any  # Assuming I.ListPageOptions is not specified further

# Class declaration for GameStorage
class GameStorage:
    getDataStorage: Callable[[str], 'GameDataStorage']
    getGroupStorage: Callable[[str], Optional['GameDataStorage']]

    def __init__(self, getDataStorage: Callable[[str], 'GameDataStorage'], getGroupStorage: Callable[[str], Optional['GameDataStorage']]) -> None:
        ...

# Class declaration for GameDataStorage
class GameDataStorage:
    key: str

    set: Callable[[str, JSONValue], None]
    update: Callable[[str, Callable[[ReturnValue], JSONValue]], None]
    get: Callable[[str], ReturnValue]
    list: Callable[[ListPageOptions], ListReturnValue]
    remove: Callable[[str], ReturnValue]
    destroy: Callable[[], None]

    def __init__(
        self,
        key: str,
        set: Callable[[str, JSONValue], None],
        update: Callable[[str, Callable[[ReturnValue], JSONValue]], None],
        get: Callable[[str], ReturnValue],
        list: Callable[[ListPageOptions], ListReturnValue],
        remove: Callable[[str], ReturnValue],
        destroy: Callable[[], None]
    ) -> None:
        ...

# Class declaration for QueryList
class QueryList:
    getCurrentPage: Callable[[], List[ReturnValue]]
    nextPage: Callable[[], None]
    isLastPage: bool

    def __init__(self, getCurrentPage: Callable[[], List[ReturnValue]], nextPage: Callable[[], None]) -> None:
        ...

# Class declaration for URLSearchParams
class URLSearchParams:
    def __init__(self, args: Any) -> None:
        ...

    def append(self, name: str, value: str) -> None:
        ...

    def delete(self, name: str) -> None:
        ...

    def get(self, name: str) -> Optional[str]:
        ...

    def getAll(self, name: str) -> List[str]:
        ...

    def forEach(self, callback: Callable[[str, str, 'URLSearchParams'], None]) -> None:
        ...

    def has(self, name: str) -> bool:
        ...

    def set(self, name: str, value: str) -> None:
        ...

    def keys(self) -> Iterable[str]:
        ...

    def values(self) -> Iterable[str]:
        ...

    def entries(self) -> Iterable[Tuple[str, str]]:
        ...

    def sort(self) -> None:
        ...

    def toString(self) -> str:
        ...

    def __iter__(self) -> Iterable[Tuple[str, str]]:
        ...

# Class declaration for URL
class URL:
    def __init__(self, url: Any, base: Optional[Any] = None) -> None:
        ...

    @property
    def hash(self) -> str:
        ...

    @hash.setter
    def hash(self, value: str) -> None:
        ...

    @property
    def host(self) -> str:
        ...

    @host.setter
    def host(self, value: str) -> None:
        ...

    @property
    def hostname(self) -> str:
        ...

    @hostname.setter
    def hostname(self, value: str) -> None:
        ...

    @property
    def port(self) -> str:
        ...

    @port.setter
    def port(self, value: str) -> None:
        ...

    @property
    def href(self) -> str:
        ...

    @href.setter
    def href(self, value: str) -> None:
        ...

    @property
    def origin(self) -> str:
        ...

    @property
    def username(self) -> str:
        ...

    @username.setter
    def username(self, value: str) -> None:
        ...

    @property
    def password(self) -> str:
        ...

    @password.setter
    def password(self, value: str) -> None:
        ...

    @property
    def pathname(self) -> str:
        ...

    @pathname.setter
    def pathname(self, value: str) -> None:
        ...

    @property
    def protocol(self) -> str:
        ...

    @protocol.setter
    def protocol(self, value: str) -> None:
        ...

    @property
    def search(self) -> str:
        ...

    @search.setter
    def search(self, value: str) -> None:
        ...

    @property
    def searchParams(self) -> 'URLSearchParams':
        ...

    def toString(self) -> str:
        ...

    def toJSON(self) -> str:
        ...