# Match class names to opcodes
opcodes = {
    # Motion category
    "MoveSteps":                     "motion_movesteps",
    "GoToPosition":                  "motion_gotoxy",
    "GoTo":                          "motion_goto",
    "TurnRight":                     "motion_turnright",
    "TurnLeft":                      "motion_turnleft",
    "PointInDirection":              "motion_pointindirection",
    "PointTowards":                  "motion_pointtowards",
    "GlideToPosition":               "motion_glidesecstoxy",
    "GlideTo":                       "motion_glideto",
    "BounceOffEdge":                 "motion_ifonedgebounce",
    "SetRotationStyle":              "motion_setrotationstyle",
    "ChangeX":                       "motion_changexby",
    "SetX":                          "motion_setx",
    "ChangeY":                       "motion_changeyby",
    "SetY":                          "motion_sety",
    "XPosition":                     "motion_xposition",
    "YPosition":                     "motion_yposition",
    "Direction":                     "motion_direction",

    # Looks category
    "Say":                           "looks_say",
    "SayForSeconds":                 "looks_sayforsecs",
    "Think":                         "looks_think",
    "ThinkForSeconds":               "looks_thinkforsecs",
    "Show":                          "looks_show",
    "Hide":                          "looks_hide",
    "SwitchCostume":                 "looks_switchcostumeto",
    "SwitchBackdrop":                "looks_switchbackdropto",
    "SwitchBackdropAndWait":         "looks_switchbackdroptoandwait",
    "NextCostume":                   "looks_nextcostume",
    "NextBackdrop":                  "looks_nextbackdrop",
    "ChangeGraphicEffect":           "looks_changeeffectby",
    "SetGraphicEffect":              "looks_seteffectto",
    "ClearGraphicEffects":           "looks_cleargraphiceffects",
    "ChangeSize":                    "looks_changesizeby",
    "SetSize":                       "looks_setsizeto",
    "SetLayer":                      "looks_gotofrontback",
    "ChangeLayer":                   "looks_goforwardbackwardlayers",
    "Size":                          "looks_size",
    "Costume":                       "looks_costumenumbername",
    "Backdrop":                      "looks_backdropnumbername",

    # Sound category
    "Play":                          "sound_play",
    "PlayUntilDone":                 "sound_playuntildone",
    "StopSounds":                    "sound_stopallsounds",
    "SetSoundEffect":                "sound_seteffectto",
    "ChangeSoundEffect":             "sound_changeeffectby",
    "ClearSoundEffects":             "sound_cleareffects",
    "SetVolume":                     "sound_setvolumeto",
    "ChangeVolume":                  "sound_changevolumeby",
    "Volume":                        "sound_volume",

    # Events category
    "WhenFlagClicked":               "event_whenflagclicked",
    "WhenKeyPressed":                "event_whenkeypressed",
    "WhenThisSpriteClicked":         "event_whenthisspriteclicked",
    "WhenBackdropSwitchesTo":        "event_whenbackdropswitchesto",
    "WhenGreaterThan":               "event_whengreaterthan",
    "WhenBroadcastReceived":         "event_whenbroadcastreceived",
    "Broadcast":                     "event_broadcast",
    "BroadcastAndWait":              "event_broadcastandwait",

    # Control category
    "Wait":                          "control_wait",
    "Repeat":                        "control_repeat",
    "Forever":                       "control_forever",
    "If":                            "control_if",
    "WaitUntil":                     "control_wait_until",
    "RepeatUntil":                   "control_repeat_until",
    "Stop":                          "control_stop",
    "WhenStartAsClone":              "control_start_as_clone",
    "CreateCloneOf":                 "control_create_clone_of",
    "DeleteThisClone":               "control_delete_this_clone",

    # Sensing category
    "TouchingObject":                "sensing_touchingobject",
    "TouchingColor":                 "sensing_touchingcolor",
    "ColorTouchingColor":            "sensing_coloristouchingcolor",
    "DistanceTo":                    "sensing_distanceto",
    "Timer":                         "sensing_timer",
    "ResetTimer":                    "sensing_resettimer",
    "GetAttribute":                  "sensing_of",
    "MouseX":                        "sensing_mousex",
    "MouseY":                        "sensing_mousey",
    "SetDragMode":                   "sensing_setdragmode",
    "MouseDown":                     "sensing_mousedown",
    "KeyPressed":                    "sensing_keypressed",
    "Current":                       "sensing_current",
    "DaysSince2000":                 "sensing_dayssince2000",
    "Loudness":                      "sensing_loudness",
    "Loud":                          "sensing_loud",
    "AskAndWait":                    "sensing_askandwait",
    "Answer":                        "sensing_answer",
    "Username":                      "sensing_username",

    # Operators category
    "Add":                           "operator_add",
    "Subtract":                      "operator_subtract",
    "Multiply":                      "operator_multiply",
    "Divide":                        "operator_divide",
    "LessThan":                      "operator_lt",
    "Equals":                        "operator_equals",
    "GreaterThan":                   "operator_gt",
    "And":                           "operator_and",
    "Or":                            "operator_or",
    "Not":                           "operator_not",
    "PickRandom":                    "operator_random",
    "Join":                          "operator_join",
    "LetterOf":                      "operator_letter_of",
    "LengthOf":                      "operator_length",
    "Contains":                      "operator_contains",
    "Modulo":                        "operator_mod",
    "Round":                         "operator_round",
    "Operation":                     "operator_mathop",

    # Variables category
    "SetVariable":                   "data_setvariableto",
    "ChangeVariable":                "data_changevariableby",
    "HideVariable":                  "data_hidevariable",
    "ShowVariable":                  "data_showvariable",

    # Lists category
    "AddToList":                     "data_addtolist",
    "DeleteOfList":                  "data_deleteoflist",
    "ClearList":                     "data_deletealloflist",
    "InsertIntoList":                "data_insertatlist",
    "ReplaceInList":                 "data_replaceitemoflist",
    "ItemOfList":                    "data_itemoflist",
    "ListIndexOf":                   "data_itemnumoflist",
    "ListLength":                    "data_lengthoflist",
    "ListContains":                  "data_listcontainsitem",
    "HideList":                      "data_hidelist",
    "ShowList":                      "data_showlist",

    # My Blocks category
    "CustomBlock":                   "procedures_definition",
    "CustomBlockPrototype":          "procedures_prototype",
    "CustomBlockCallable":           "procedures_call",
    "s":                             "argument_reporter_string_number",
    "b":                             "argument_reporter_boolean"
}

menu_opcodes = {
    "motion_goto":                   "motion_goto_menu",
    "motion_glideto":                "motion_glideto_menu",
    "motion_pointtowards":           "motion_pointtowards_menu",

    "looks_switchcostumeto":         "looks_costume",
    "looks_switchbackdropto":        "looks_backdrops",
    "looks_switchbackdroptoandwait": "looks_backdrops",

    "sound_play":                    "sound_sounds_menu",
    "sound_playuntildone":           "sound_sounds_menu",

    "event_broadcast":               "event_broadcast_menu",
    "event_broadcastandwait":        "event_broadcast_menu",

    "control_create_clone_of":       "control_create_clone_of_menu",

    "sensing_touchingobject":        "sensing_touchingobjectmenu",
    "sensing_distanceto":            "sensing_distancetomenu",
    "sensing_keypressed":            "sensing_keyoptions",
    "sensing_of":                    "sensing_of_object_menu"
}

def _get(key):
    # Usually key will be a class instance ("self")
    key = key if isinstance(key, str) else key.__class__.__name__
    return opcodes[key]
