from typing import *


# =====================================================================================================================
class PROJECT:
    # AUX --------------------------------------------------
    _VERSION_TEMPLATE: Tuple[int] = (0, 0, 2)

    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"

    # PROJECT ----------------------------------------------
    NAME_IMPORT: str = "dummy_module"
    NAME_INSTALL: str = NAME_IMPORT.replace("_", "-")
    KEYWORDS: List[str] = [
        "dummy",
        "dummy pypi",
        "dummy pypi module", "dummy pypi package", "dummy pypi pkg",
        "dummy module", "dummy package", "dummy pkg",
        "blank module", "blank package", "blank pkg",
        "zero module", "zero package", "zero pkg",
    ]
    CLASSIFIERS_TOPICS_ADD: List[str] = [
        # "Topic :: Communications",
        # "Topic :: Communications :: Email",
    ]

    # README -----------------------------------------------
    # add DOUBLE SPACE at the end of all lines! for correct representation in MD-viewers
    DESCRIPTION_SHORT: str = "just a zero/dummy pypi package"
    DESCRIPTION_LONG: str = """
designed for test applications which handle with pypi packages (install/uninstall/check versions/upgrade).  
With this module you dont need to handle with some specific pkg!  
"""
    FEATURES: List[str] = [
        # "feat1",
        # ["feat2", "block1", "block2"],

        "It doesn't do anything!",
    ]

    # HISTORY -----------------------------------------------
    VERSION: Tuple[int, int, int] = (0, 0, 1)
    VERSION_STR: str = ".".join(map(str, VERSION))
    TODO: List[str] = [
        "ALL ARE ALREADY PERFECT!"
    ]
    FIXME: List[str] = [
        "ALL ARE ALREADY PERFECT!"
    ]
    NEWS: List[str] = [
        "READY PERFECT DUMMY PKG!"
    ]


# =====================================================================================================================
if __name__ == '__main__':
    pass


# =====================================================================================================================
