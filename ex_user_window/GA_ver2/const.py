PRESENTATION_SIZE = 4
POPULATION_SIZE = 800
CROSSOVER_RATIO = 0.7
MUTATION_RATIO = 0.01

chromosome_templates = {
    "general": {
        "eye-out": 0,
        # "eye-in": 0,
        "eye-size": 0,
        # "l-eye-height": 0,
        # "l-eye-distance": 0,
        # "r-eye-out": 0,
        # "r-eye-in": 0,
        # "r-eye-height": 0,
        # "r-eye-distance": 0,
        # "head-width": 0,
        # "head-height": 0,
        # "nose-width": 0,
        # "nose-height": 0,
        # "mouth-vertical": 0,
        # "chin-vertical": 0
    },
    "eyes": {
        "l-eye-height1": 0,
        "l-eye-height3": 0,
        "l-eye-corner1": 0,
        "l-eye-corner2": 0,
        "r-eye-height1": 0,
        "r-eye-height3": 0,
        "r-eye-corner1": 0,
        "r-eye-corner2": 0,
    },
    "nose": {
        "nose/nose-width1-min|max": 0,
        "nose/nose-width2-min|max": 0,
    },
    "mouth": {
        "mouth/mouth-angles-up|down": 0,
        "mouth/mouth-lowerlip-height-min|max": 0,
        "mouth/mouth-upperlip-height-min|max": 0,
    }
}