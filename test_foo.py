#! /usr/bin/env python3

import pytest
import shutil
import os

@pytest.fixture
def datadir(tmpdir, request):
    '''
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    '''
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        if os.path.exists(str(tmpdir)):
            shutil.rmtree(str(tmpdir))
        shutil.copytree(test_dir, str(tmpdir))

    return tmpdir

def test_foo(datadir):
    expected_config_1 = datadir.join('expected_config_1.ini')
    expected_config_2 = datadir.join('expected_config_2.ini')
    content_1 = expected_config_1.read()
    content_2 = expected_config_2.read()
    assert content_1 == "expected1\nexpected1\nexpected1\nexpected1\nexpected1\nexpected1\nexpected1\nexpected1"
    assert content_2 == "expected2\nexpected4\nexpected2\nexpected3\nexpected2\nexpected2\nexpected2\nexpected2"
