from GA_ver2.const import PRESENTATION_SIZE


all_modifiers = {
    "init":{
        "macrodetails/Gender": 0,
        "macrodetails/Age": 0.365,
        "macrodetails/African": 0,
        "macrodetails/Asian": 0.275,
    },
    "general":{
        "1st": {
            "eyes/l-eye-push1-in|out": 0,
            # "eyes/l-eye-push2-in|out": 0,
            "eyes/l-eye-size-small|big": 0,
        },
        "2nd":{
            "eyes/l-eye-height2-min|max": 0,
            "eyes/l-eye-move-in|out": 0,
            "eyes/r-eye-push1-in|out": 0,
            "eyes/r-eye-push2-in|out": 0,
            "eyes/r-eye-height2-min|max": 0,
            "eyes/r-eye-move-in|out": 0,
            "eyes/r-eye-size-small|big": 0,
            "head/head-scale-horiz-less|more": 0,
            "chin/chin-height-min|max": 0,
            "nose/nose-scale-horiz-incr|decr": 0,
            "nose/nose-scale-vert-incr|decr": 0,
            "mouth/mouth-trans-up|down": 0,
        }
    },
    "eyes":{
        "eyes/l-eye-height1-min|max": 0,
        "eyes/l-eye-height3-min|max": 0,
        "eyes/l-eye-corner1-up|down": 0,
        "eyes/l-eye-corner2-up|down": 0,
        "eyes/r-eye-height1-min|max": 0,
        "eyes/r-eye-height3-min|max": 0,
        "eyes/r-eye-corner1-up|down": 0,
        "eyes/r-eye-corner2-up|down": 0,
    },
}