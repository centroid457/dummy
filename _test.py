import os
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
from configparser import ConfigParser

from dummy import *


# =====================================================================================================================
class Test__1:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        self.VICTIM = type("VICTIM", (Dummy,), {})

    # -----------------------------------------------------------------------------------------------------------------
    def test__1(self):
        assert True


# =====================================================================================================================
