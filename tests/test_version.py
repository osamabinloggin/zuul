# coding: utf-8

import pytest


@pytest.fixture(params=['ingress', 'slack', 'zuul'])
def package_module(request):
    mod = __import__(request.param)
    return mod


def test_has_version(package_module):
    assert package_module.__version__ >= '18.7.0'
