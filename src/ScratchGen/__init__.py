from .project import *
from .blocks import *
# Not sure why this import works with *dir but we don't ask
from .constants import *

__all__ = (
    "Project",

    # Pythonista (add every constant)
    *dir(constants),

    # Motion category
    "MoveSteps",
    "GoToPosition",
    "GoTo",
    "TurnRight",
    "TurnLeft",
    "PointInDirection",
    "PointTowards",
    "GlideToPosition",
    "GlideTo",
    "BounceOffEdge",
    "SetRotationStyle",
    "ChangeX",
    "SetX",
    "ChangeY",
    "SetY",
    "XPosition",
    "YPosition",
    "Direction",

    # Looks category
    "Say",
    "SayForSeconds",
    "Think",
    "ThinkForSeconds",
    "Show",
    "Hide",
    "SwitchCostume",
    "SwitchBackdrop",
    "SwitchBackdropAndWait",
    "NextCostume",
    "NextBackdrop",
    "ChangeGraphicEffect",
    "SetGraphicEffect",
    "ClearGraphicEffects",
    "ChangeSize",
    "SetSize",
    "SetLayer",
    "ChangeLayer",
    "Size",
    "Costume",
    "Backdrop",

    # Sound category
    "Play",
    "PlayUntilDone",
    "StopSounds",
    "SetSoundEffect",
    "ChangeSoundEffect",
    "ClearSoundEffects",
    "SetVolume",
    "ChangeVolume",
    "Volume",

    # Events category
    "WhenFlagClicked",
    "WhenKeyPressed",
    "WhenThisSpriteClicked",
    "WhenBackdropSwitchesTo",
    "WhenGreaterThan",
    "WhenBroadcastReceived",
    "Broadcast",
    "BroadcastAndWait",

    # Control category
    "Wait",
    "Repeat",
    "Forever",
    "If",
    "WaitUntil",
    "RepeatUntil",
    "Stop",
    "WhenStartAsClone",
    "CreateCloneOf",
    "DeleteThisClone",

    # Sensing category
    "TouchingObject",
    "TouchingColor",
    "ColorTouchingColor",
    "DistanceTo",
    "Timer",
    "ResetTimer",
    "GetAttribute",
    "MouseX",
    "MouseY",
    "SetDragMode",
    "MouseDown",
    "KeyPressed",
    "Current",
    "DaysSince2000",
    "Loudness",
    "Loud",
    "AskAndWait",
    "Answer",
    "Username",

    # Operators category
    "Add",
    "Subtract",
    "Multiply",
    "Divide",
    "LessThan",
    "Equals",
    "GreaterThan",
    "And",
    "Or",
    "Not",
    "PickRandom",
    "Join",
    "LetterOf",
    "LengthOf",
    "Contains",
    "Modulo",
    "Round",
    "Operation",

    # Variables category
    "SetVariable",
    "ChangeVariable",
    "HideVariable",
    "ShowVariable",

    # Lists category
    "AddToList",
    "DeleteOfList",
    "ClearList",
    "InsertIntoList",
    "ReplaceInList",
    "ItemOfList",
    "ListIndexOf",
    "ListLength",
    "ListContains",
    "HideList",
    "ShowList",

    # My blocks
    "CustomBlock"
)
