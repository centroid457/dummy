from typing import *
from _aux__release_files import release_files_update


# =====================================================================================================================
VERSION = (0, 0, 3)   # 1/deprecate _VERSION_TEMPLATE from PRJ object +2/place update_prj here in __main__ +3/separate finalize attrs


# =====================================================================================================================
class PROJECT:
    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"

    # PROJECT ----------------------------------------------
    NAME_IMPORT: str = "dummy_module"
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
    VERSION: Tuple[int, int, int] = (0, 0, 3)
    TODO: List[str] = [
        "ALL ARE ALREADY PERFECT!"
    ]
    FIXME: List[str] = [
        "ALL ARE ALREADY PERFECT!"
    ]
    NEWS: List[str] = [
        "[__INIT__.py] fix import",
        "apply last pypi template",
    ]

    # FINALIZE -----------------------------------------------
    VERSION_STR: str = ".".join(map(str, VERSION))
    NAME_INSTALL: str = NAME_IMPORT.replace("_", "-")


# =====================================================================================================================
if __name__ == '__main__':
    release_files_update(PROJECT)


# =====================================================================================================================
