# Skipping Tests

import sys
import pytest
from module_02.cg00_apps.employee import Employee
# skip, xfail, xpass, skipif

test_boolean_1_run = "don't run"


@pytest.mark.skipif(sys.version_info < (3, 13), reason="Python 3.13 not found")
#@pytest.mark.skipif(test_boolean_1_run == "don't run", reason = "not ready")
def test_boolean_1():
    status = 100
    assert status == 10


def test_boolean_2():
    status = 100
    assert status == 100


def test_boolean_3():
    status = 100
    assert status == 100
