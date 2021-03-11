# -*- coding: utf-8 -*-

""" tests.test_cli

Integration tests for conda-content-trust/conda_content_trust/cli.py.

Run the tests this way:
    pytest tests/test_cli.py

"""

import subprocess

import conda_content_trust.cli

def test_cli_basics():
  assert not subprocess.call(['conda-content-trust', '-V'])
  assert not subprocess.call(['conda-content-trust', '--version'])
  assert not subprocess.call(['conda-content-trust', '--help'])

def test_that_all_calls_complete():
  assert not subprocess.call(['conda-content-trust', '-V'])
  assert not subprocess.call(['conda-content-trust', '--version'])
  assert not subprocess.call(['conda-content-trust', '--help'])

def test_gpg_key_fingerprint():
  assert not subprocess.call(['conda-content-trust', '-V'])
  raise NotImplementedError()

def test_():
  raise NotImplementedError()

def test_():
  raise NotImplementedError()

def test_():
  raise NotImplementedError()

def test_():
  raise NotImplementedError()

def test_():
  raise NotImplementedError()

def test_():
  raise NotImplementedError()

def test_():
  raise NotImplementedError()

