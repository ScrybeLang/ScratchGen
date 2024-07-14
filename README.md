# `ScratchGen`

A Python interface for creating Scratch projects.

## Usage

Use a wildcard import, like so:

```python
from ScratchGen import *
```

The namespace has been curated to avoid pollution.

# Setting up a Project

Initializing a new project takes only one line:

```python
project = Project()
```

## Creating Sprites

To add a sprite to your project, you must specify the sprite's name:

```python
sprite = project.createSprite("Sprite 1")
```

You may create as many sprites as are necessary.

## Adding Costumes and Backdrops

To add a costume to a sprite, provide a filepath and an optional alternative name:

```python
# Costume will be named "scratch cat"
cat_costume = sprite.addCostume("assets/scratch cat.png")

# Costume will be named "balloon"
balloon_costume = sprite.addCostume("balloon", "inflatable.jpg")
```

To add a backdrop to the stage, call `addBackdrop` on the project or on the stage directly.

## Adding Sounds

Call `addSound` in the same place you would call `addCostume` or `addBackdrop` to add sounds.

## Creating Variables and Lists

To create a local variable or list, call these functions from a sprite object:

```python
my_variable = sprite.createVariable("my variable")
my_list = sprite.createList("my list")
```

To make global ones instead, call these functions from the project object (or the stage):

```python
stage = project.stage

global_variable = project.createGlobalVariable("global variable")
global_list = stage.createList("global list")
```

## Creating Scripts

Any sprite or the stage can have as many scripts as necessary. To create one, call `createScript` with the desired sequence of blocks as parameters.

# Blocks

## Motion Category

### ![](blockimages/motion_movesteps.png) - `MoveSteps`

| Parameter | Description            |
| --------- | ---------------------- |
| `steps`   | How many steps to move |

### ![](blockimages/motion_gotoxy.png) - `GoToPosition`

| Parameter | Description |
| --------- | ----------- |
| `x`       | X position  |
| `y`       | Y position  |

### ![](blockimages/motion_goto.png) - `GoTo`

| Parameter | Description      |
| --------- | ---------------- |
| `target`  | Target to go to  |

Possible values for `target`:
 - `RANDOM`
 - `MOUSE`
 - Any other sprite object

### ![](blockimages/motion_turnright.png) - `TurnRight`

| Parameter | Description                         |
| --------- | ----------------------------------- |
| `degrees` | Amount of degrees to turn clockwise |

### ![](blockimages/motion_turnleft.png) - `TurnLeft`

| Parameter | Description                                |
| --------- | ------------------------------------------ |
| `degrees` | Amount of degrees to turn counterclockwise |

### ![](blockimages/motion_pointindirection.png) - `PointInDirection`

| Parameter   | Description                  |
| ----------- | ---------------------------- |
| `direction` | Amount of degrees to turn to |

### ![](blockimages/motion_pointtowards.png) - `PointTowards`

| Parameter   | Description                |
| ----------- | -------------------------- |
| `target`    | The target to turn towards |

Possible values for `target`:
 - `RANDOM`
 - `MOUSE`
 - Any other sprite object

### ![](blockimages/motion_glidesecstoxy.png) - `GlideToPosition`

| Parameter | Description |
| --------- | ----------- |
| `seconds` | Seconds     |
| `x`       | X position  |
| `y`       | Y position  |

### ![](blockimages/motion_glideto.png) - `GlideTo`

| Parameter   | Description                |
| ----------- | -------------------------- |
| `seconds`   | Seconds                    |
| `target`    | The target to turn towards |

Possible values for `target`:
 - `RANDOM`
 - `MOUSE`
 - Any other sprite object

### ![](blockimages/motion_ifonedgebounce.png) - `BounceOffEdge`

### ![](blockimages/motion_setrotationstyle.png) - `SetRotationStyle`

| Parameter   | Description    |
| ----------- | -------------- |
| `style`     | Rotation style |

Possible values for `target`:
 - `LEFT_RIGHT`
 - `DONT_ROTATE`
 - `ALL_AROUND`

### ![](blockimages/motion_changexby.png) - `ChangeX`

| Parameter | Description |
| --------- | ----------- |
| `change`  | Change in X |

### ![](blockimages/motion_setx.png) - `SetX`

| Parameter | Description    |
| --------- | -------------- |
| `x`       | New X position |

### ![](blockimages/motion_changeyby.png) - `ChangeY`

| Parameter | Description |
| --------- | ----------- |
| `change`  | Change in Y |

### ![](blockimages/motion_sety.png) - `SetY`

| Parameter | Description    |
| --------- | -------------- |
| `y`       | New Y position |

### ![](blockimages/motion_xposition.png) - `XPosition`

### ![](blockimages/motion_yposition.png) - `YPosition`

### ![](blockimages/motion_direction.png) - `Direction`

## Looks Category

### ![](blockimages/looks_say.png) - `Say`

| Parameter | Description |
| --------- | ----------- |
| `message` | What to say |

### ![](blockimages/looks_sayforsecs.png) - `SayForSeconds`

| Parameter | Description |
| --------- | ----------- |
| `message` | What to say |
| `seconds` | Seconds     |

### ![](blockimages/looks_think.png) - `Think`

| Parameter | Description   |
| --------- | ------------- |
| `message` | What to think |

### ![](blockimages/looks_thinkforsecs.png) - `ThinkForSeconds`

| Parameter | Description   |
| --------- | ------------- |
| `message` | What to think |
| `seconds` | Seconds       |

### ![](blockimages/looks_show.png) - `Show`

### ![](blockimages/looks_hide.png) - `Hide`

### ![](blockimages/looks_switchcostumeto.png) - `SwitchCostume`

| Parameter | Description          |
| --------- | -------------------- |
| `costume` | Costume to switch to |

### ![](blockimages/looks_switchbackdropto.png) - `SwitchBackdrop`

| Parameter  | Description           |
| ---------- | --------------------- |
| `backdrop` | Backdrop to switch to |

### ![](blockimages/looks_switchbackdroptoandwait.png) - `SwitchBackdropAndWait`

| Parameter  | Description           |
| ---------- | --------------------- |
| `backdrop` | Backdrop to switch to |

### ![](blockimages/looks_nextcostume.png) - `NextCostume`

### ![](blockimages/looks_nextbackdrop.png) - `NextBackdrop`

### ![](blockimages/looks_changeeffectby.png) - `ChangeGraphicEffect`

| Parameter | Description    |
| --------- | -------------- |
| `effect`  | Graphic effect |
| `change`  | Change amount  |

Possible values for `effect`:
 - `COLOR`
 - `FISHEYE`
 - `WHIRL`
 - `PIXELATE`
 - `MOSAIC`
 - `BRIGHTNESS`
 - `GHOST`

### ![](blockimages/looks_seteffectto.png) - `SetGraphicEffect`

| Parameter | Description    |
| --------- | -------------- |
| `effect`  | Graphic effect |
| `value`   | Effect value   |

Possible values for `effect`:
 - `COLOR`
 - `FISHEYE`
 - `WHIRL`
 - `PIXELATE`
 - `MOSAIC`
 - `BRIGHTNESS`
 - `GHOST`

### ![](blockimages/looks_cleargraphiceffects.png) - `ClearGraphicEffects`

### ![](blockimages/looks_changesizeby.png) - `ChangeSize`

| Parameter | Description        |
| --------- | ------------------ |
| `change`  | Size change amount |

### ![](blockimages/looks_setsizeto.png) - `SetSize`

| Parameter | Description |
| --------- | ----------- |
| `size`    | New size    |

### ![](blockimages/looks_gotofrontback.png) - `SetLayer`

| Parameter | Description         |
| --------- | ------------------- |
| `layer`   | Layer to be sent to |

Possible values for `layer`:
 - `FRONT`
 - `BACK`

### ![](blockimages/looks_goforwardbackwardlayers.png) - `ChangeLayer`

| Parameter   | Description                      |
| ----------- | -------------------------------- |
| `direction` | What layer direction to go in    |
| `change`    | Amount of layers to move through |

Possible values for `direction`:
 - `FORWARD`
 - `BACKWARD`

### ![](blockimages/looks_size.png) - `Size`

### ![](blockimages/looks_costumenumbername.png) - `Costume`

| Parameter | Description       |
| --------- | ----------------- |
| `option`  | Costume attribute |

Possible values for `option`:
 - `NUMBER`
 - `NAME`

### ![](blockimages/looks_backdropnumbername.png) - `Backdrop`

| Parameter | Description        |
| --------- | ------------------ |
| `option`  | Backdrop attribute |

Possible values for `option`:
 - `NUMBER`
 - `NAME`

## Sound Category

### ![](blockimages/sound_play.png) - `Play`

| Parameter | Description   |
| --------- | ------------- |
| `sound`   | Sound to play |

### ![](blockimages/sound_playuntildone.png) - `PlayUntilDone`

| Parameter | Description   |
| --------- | ------------- |
| `sound`   | Sound to play |

### ![](blockimages/sound_stopallsounds.png) - `StopSounds`

### ![](blockimages/sound_seteffectto.png) - `SetSoundEffect`

| Parameter | Description  |
| --------- | ------------ |
| `effect`  | Sound effect |
| `value`   | Effect value |

Possible values for `effect`:
 - `PITCH`
 - `PAN`

### ![](blockimages/sound_changeeffectby.png) - `ChangeSoundEffect`

| Parameter | Description   |
| --------- | ------------- |
| `effect`  | Sound effect  |
| `change`  | Change amount |

Possible values for `effect`:
 - `PITCH`
 - `PAN`

### ![](blockimages/sound_cleareffects.png) - `ClearSoundEffects`

### ![](blockimages/sound_setvolumeto.png) - `SetVolume`

| Parameter | Description |
| --------- | ----------- |
| `volume`  | New volume  |

### ![](blockimages/sound_changevolumeby.png) - `ChangeVolume`

| Parameter | Description      |
| --------- | ---------------- |
| `change`  | Change in volume |

### ![](blockimages/sound_volume.png) - `Volume`

## Events Category

### ![](blockimages/event_whenflagclicked.png) - `WhenFlagClicked`

### ![](blockimages/event_whenkeypressed.png) - `WhenKeyPressed`

| Parameter | Description   |
| --------- | ------------- |
| `key`     | Key to detect |

Possible values for `key`:
 - Any character in U+0021 to U+007E
 - `SPACE`
 - `ENTER`
 - `UP_ARROW`
 - `DOWN_ARROW`
 - `LEFT_ARROW`
 - `RIGHT_ARROW`

### ![](blockimages/event_whenthisspriteclicked.png) - `WhenThisSpriteClicked`

### ![](blockimages/event_whenbackdropswitchesto.png) - `WhenBackdropSwitchesTo`

| Parameter  | Description        |
| ---------- | ------------------ |
| `backdrop` | Backdrop to detect |

### ![](blockimages/event_whengreaterthan.png) - `WhenGreaterThan`

| Parameter   | Description           |
| ----------- | --------------------- |
| `value`     | Value to detect       |
| `threshold` | Maximum allowed value |

### ![](blockimages/event_whenbroadcastreceived.png) - `WhenBroadcastReceived`

| Parameter   | Description         |
| ----------- | ------------------- |
| `broadcast` | Broadcast to detect |

### ![](blockimages/event_broadcast.png) - `Broadcast`

| Parameter   | Description       |
| ----------- | ----------------- |
| `broadcast` | Broadcast to send |

### ![](blockimages/event_broadcastandwait.png) - `BroadcastAndWait`

| Parameter   | Description       |
| ----------- | ----------------- |
| `broadcast` | Broadcast to send |

## Control Category

### ![](blockimages/control_wait.png) - `Wait`

| Parameter  | Description     |
| ---------- | --------------- |
| `duration` | Seconds to wait |

### ![](blockimages/control_repeat.png) - `Repeat`

| Parameter | Description     |
| --------- | --------------- |
| `times`   | Times to repeat |

### ![](blockimages/control_forever.png) - `Forever`

### ![](blockimages/control_if.png) - `If`

| Parameter   | Description        |
| ----------- | ------------------ |
| `condition` | Condition to check |

You may call `.Else(...)` on this block to provide an alternative substack, like so:

```python
If(Equals(1, 1),
    Say("one equals one")
).Else(
    Say("something is terribly wrong")
)
```

### ![](blockimages/control_wait_until.png) - `WaitUntil`

| Parameter   | Description        |
| ----------- | ------------------ |
| `condition` | Condition to check |

### ![](blockimages/control_repeat_until.png) - `RepeatUntil`

| Parameter   | Description        |
| ----------- | ------------------ |
| `condition` | Condition to check |

### ![](blockimages/control_stop.png) - `Stop`

| Parameter | Description  |
| --------- | ------------ |
| `mode`    | What to stop |

Possible values for `mode`:
 - `ALL`
 - `OTHER_SCRIPTS`
 - `THIS_SCRIPT`

### ![](blockimages/control_start_as_clone.png) - `WhenStartAsClone`

### ![](blockimages/control_create_clone_of.png) - `CreateCloneOf`

| Parameter | Description               |
| --------- | ------------------------- |
| `target`  | What to create a clone of |

Possible values for `target`:
 - `MYSELF`
 - Any other sprite object

### ![](blockimages/control_delete_this_clone.png) - `DeleteThisClone`

## Sensing Category

### ![](blockimages/sensing_touchingobject.png) - `TouchingObject`

| Parameter | Description    |
| --------- | -------------- |
| `target`  | What to detect |

Possible values for `target`:
 - `MOUSE`
 - `EDGE`
 - Any other sprite object

### ![](blockimages/sensing_touchingcolor.png) - `TouchingColor`

| Parameter  | Description                     |
| ---------- | ------------------------------- |
| `hex_code` | Hex code of the color to detect |

### ![](blockimages/sensing_coloristouchingcolor.png) - `ColorTouchingColor`

| Parameter    | Description                   |
| ------------ | ----------------------------- |
| `hex_code_1` | Hex code of the first color   |
| `hex_code_2` | Hex code of the second color  |

### ![](blockimages/sensing_distanceto.png) - `DistanceTo`

| Parameter | Description    |
| --------- | -------------- |
| `target`  | What to detect |

Possible values for `target`:
 - `MOUSE`
 - Any other sprite object

### ![](blockimages/sensing_timer.png) - `Timer`

### ![](blockimages/sensing_resettimer.png) - `ResetTimer`

### ![](blockimages/sensing_of.png) - `GetAttribute`

| Parameter   | Description      |
| ----------- | ---------------- |
| `attribute` | Attribute to get |
| `target`    | Target object    |

Possible values for `attribute`:
 - Stage-specific:
    - `BACKDROP_NUMBER`
    - `BACKDROP_NAME`
    - Any global variable
 - Sprite-specific:
    - `X_POSITION`
    - `Y_POSITION`
    - `DIRECTION`
    - `COSTUME_NUMBER`
    - `COSTUME_NAME`
    - `SIZE`
    - Any local variable
 - `VOLUME`

### ![](blockimages/sensing_mousex.png) - `MouseX`

### ![](blockimages/sensing_mousey.png) - `MouseY`

### ![](blockimages/sensing_setdragmode.png) - `SetDragMode`

| Parameter | Description |
| --------- | ----------- |
| `mode`    | Drag mode   |

Possible values for `mode`:
 - `DRAGGABLE`
 - `NOT_DRAGGABLE`

### ![](blockimages/sensing_mousedown.png) - `MouseDown`

### ![](blockimages/sensing_keypressed.png) - `KeyPressed`

| Parameter | Description   |
| --------- | ------------- |
| `key`     | Key to detect |

Possible values for `key`:
 - Any character in U+0021 to U+007E
 - `SPACE`
 - `ENTER`
 - `UP_ARROW`
 - `DOWN_ARROW`
 - `LEFT_ARROW`
 - `RIGHT_ARROW`

### ![](blockimages/sensing_current.png) - `Current`

| Parameter | Description   |
| --------- | ------------- |
| `option`  | CURRENT WHAT? |

Possible values for `option`:
 - `YEAR`
 - `MONTH`
 - `DATE`
 - `DAY_OF_WEEK`
 - `HOUR`
 - `MINUTE`
 - `SECOND`

### ![](blockimages/sensing_dayssince2000.png) - `DaysSince2000`

### ![](blockimages/sensing_loudness.png) - `Loudness`

### ![](blockimages/sensing_loud.png) - `Loud`

### ![](blockimages/sensing_askandwait.png) - `AskAndWait`

| Parameter  | Description |
| ---------- | ----------- |
| `question` | What to ask |

### ![](blockimages/sensing_answer.png) - `Answer`

### ![](blockimages/sensing_username.png) - `Username`

## Operators Category

### ![](blockimages/operator_add.png) - `Add`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_subtract.png) - `Subtract`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_multiply.png) - `Multiply`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_divide.png) - `Divide`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_lt.png) - `LessThan`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_equals.png) - `Equals`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_gt.png) - `GreaterThan`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_and.png) - `And`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_or.png) - `Or`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_not.png) - `Not`

| Parameter   | Description        |
| ----------- | ------------------ |
| `condition` | Condition to check |

### ![](blockimages/operator_random.png) - `PickRandom`

| Parameter | Description |
| --------- | ----------- |
| `start`   | Minimum     |
| `end`     | Maximum     |

### ![](blockimages/operator_join.png) - `Join`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_letter_of.png) - `LetterOf`

| Parameter  | Description     |
| ---------- | --------------- |
| `position` | Index           |
| `string`   | String to index |

### ![](blockimages/operator_length.png) - `LengthOf`

| Parameter | Description   |
| --------- | ------------- |
| `string`  | Target string |

### ![](blockimages/operator_contains.png) - `Contains`

| Parameter   | Description |
| ----------- | ----------- |
| `string`    | String      |
| `substring` | Substring   |

### ![](blockimages/operator_mod.png) - `Modulo`

| Parameter | Description |
| --------- | ----------- |
| `a`       | Operand 1   |
| `b`       | Operand 2   |

### ![](blockimages/operator_round.png) - `Round`

| Parameter | Description    |
| --------- | -------------- |
| `value`   | Value to round |

### ![](blockimages/operator_mathop.png) - `Operation`

| Parameter   | Description          |
| ----------- | -------------------- |
| `operation` | Operation to perform |
| `value`     | Target value         |

Possible values for `operation`:
 - `ABSOLUTE`
 - `FLOOR`
 - `CEILING`
 - `SQUARE_ROOT`
 - `SINE`
 - `COSINE`
 - `TANGENT`
 - `ARCSINE`
 - `ARCCOSING`
 - `ARCTANGENT`
 - `NATURAL_LOGARITHM`
 - `LOGARITHM`
 - `E_TO_THE`
 - `TEN_TO_THE`

## Variables Category

### ![](blockimages/data_setvariableto.png) - `SetVariable`

| Parameter  | Description     |
| ---------- | --------------- |
| `variable` | Variable to set |
| `value`    | New value       |

### ![](blockimages/data_changevariableby.png) - `ChangeVariable`

| Parameter  | Description            |
| ---------- | ---------------------- |
| `variable` | Variable to change     |
| `change`   | Change to the variable |

### ![](blockimages/data_hidevariable.png) - `HideVariable`

| Parameter  | Description      |
| ---------- | ---------------- |
| `variable` | Variable to hide |

### ![](blockimages/data_showvariable.png) - `ShowVariable`

| Parameter  | Description      |
| ---------- | ---------------- |
| `variable` | Variable to show |

### ![](blockimages/data_addtolist.png) - `AddToList`

| Parameter | Description    |
| --------- | -------------- |
| `item`    | Item to add    |
| `list`    | List to add to |

### ![](blockimages/data_deleteoflist.png) - `DeleteOfList`

| Parameter | Description         |
| --------- | ------------------- |
| `index`   | Index to delete     |
| `list`    | List to delete from |

### ![](blockimages/data_deletealloflist.png) - `ClearList`

| Parameter | Description   |
| --------- | ------------- |
| `list`    | List to clear |

### ![](blockimages/data_insertatlist.png) - `InsertIntoList`

| Parameter | Description         |
| --------- | ------------------- |
| `item`    | Item to insert      |
| `index`   | Index to insert at  |
| `list`    | List to insert into |

### ![](blockimages/data_replaceitemoflist.png) - `ReplaceInList`

| Parameter | Description          |
| --------- | -------------------- |
| `index`   | Index to replace     |
| `list`    | List to replace from |
| `item`    | What to replace with |

### ![](blockimages/data_itemoflist.png) - `ItemOfList`

| Parameter | Description   |
| --------- | ------------- |
| `index`   | List index    |
| `list`    | List to index |

### ![](blockimages/data_itemnumoflist.png) - `ListIndexOf`

| Parameter | Description   |
| --------- | ------------- |
| `item`    | Item to index |
| `list`    | List to index |

### ![](blockimages/data_lengthoflist.png) - `ListLength`

| Parameter | Description     |
| --------- | --------------- |
| `list`    | List to measure |

### ![](blockimages/data_listcontainsitem.png) - `ListContains`

| Parameter | Description    |
| --------- | -------------- |
| `list`    | Target list    |
| `item`    | Item to detect |

### ![](blockimages/data_hidelist.png) - `HideList`

| Parameter | Description  |
| --------- | ------------ |
| `list`    | List to hide |

### ![](blockimages/data_showlist.png) - `ShowList`

| Parameter | Description  |
| --------- | ------------ |
| `list`    | List to show |

# Custom Blocks

Creating a custom block in the stage/a sprite takes several steps. First, initialize the custom block with a proccode:

```python
prototype = sprite.createCustomBlock("move %s steps in direction %s")
```

Use `%s` for number/text input, and use `%b` for boolean input.

Next, grab the function parameters to be used in its definition:

```python
steps, direction = prototype.getParameters()
```

Finally, give the custom block its definition:

```python
move_in_direction = prototype.setScript(
    PointInDirection(direction),
    MoveSteps(steps)
)
```

Now, you can use the custom block as you would any other block.

```python
sprite.createScript(WhenFlagClicked(),
    GoToPosition(0, 0),
    PointInDirection(90),
    Forever(
        move_in_direction(5, PickRandom(0, 359))
    )
)
```

# Saving

To save your completed project, call the `save` function with a filename of your choice:

```python
project.save("my project.sb3")
```

# Examples

## Custom Block

```python
from ScratchGen import *

project = Project()
sprite = project.createSprite("Custom Block Sprite")

prototype = sprite.createCustomBlock("move %s steps in direction %s")
steps, direction = prototype.getParameters()
move_in_direction = prototype.setScript(
    PointInDirection(direction),
    MoveSteps(steps)
)

sprite.createScript(WhenFlagClicked(),
    GoToPosition(0, 0),
    PointInDirection(90),
    Forever(
        move_in_direction(5, PickRandom(0, 359))
    )
)

project.save("Custom Block Test.sb3")
```

## Text Reversal

```python
from ScratchGen import *

project = Project()

sprite = project.createSprite("Text Reversal Sprite")
sprite.addCostume("assets/scratch logo.png")

reversed_text = project.createGlobalVariable("reversed text")

block = sprite.createCustomBlock("reverse text %s")
text = block.getParameters()
reverse_text = block.setScript(
    SetVariable(reversed_text, ""),

    Repeat(LengthOf(text),
        SetVariable(reversed_text,
            Join(
                LetterOf(
                    Add(LengthOf(reversed_text), 1),
                    text
                ), reversed_text
            )
        )
    )
)

sprite.createScript(WhenFlagClicked(),
    reverse_text("Hello, World!"),
    Say(reversed_text)
)

project.save("Text Reversal Test.sb3")
```

## Jetpack Game

```python
from ScratchGen import *

project = Project()

sprite = project.createSprite("Flying Sprite")
sprite.addCostume("assets/linus jetpack.png")

y_velocity = sprite.createVariable("y velocity")

sprite.createScript(WhenFlagClicked(),
    GoToPosition(0, 0),
    SetVariable(y_velocity, 0),

    Forever(
        If(Or(MouseDown(), KeyPressed(SPACE)),
            ChangeVariable(y_velocity, 2)
        ).Else(
            ChangeVariable(y_velocity, -2)
        ),

        ChangeY(y_velocity)
    )
)

project.save("Flying Test.sb3")
```
