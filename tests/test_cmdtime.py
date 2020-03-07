#!/usr/bin/env python3
import cmdtime
import platform
import pytest
import subprocess

# common tests
def test_cmdtime_echo():
    result = subprocess.run(['cmdtime', 'echo test_cmdtime_echo'], capture_output=True)
    s = result.stdout.decode()
    e = result.stderr.decode()
    assert 'test_cmdtime_echo' in s
    assert 'Elapsed Time:' in s
    assert  e == ''

# Linux tests
@pytest.mark.skipif(platform.system() != 'Linux', reason="Linux-only test")
def test_cmdtime_dir_linux():
    result = subprocess.run(['cmdtime', 'ls -al'], capture_output=True)
    s = result.stdout.decode()
    e = result.stderr.decode()
    assert 'total' in s
    assert 'Elapsed Time:' in s
    assert e == ''

@pytest.mark.skipif(platform.system() != 'Linux', reason="Linux-only test")
def test_cmdtime_ping_linux():
    result = subprocess.run(['cmdtime', 'ping 127.0.0.1 -c 2'], capture_output=True)
    s = result.stdout.decode()
    e = result.stderr.decode()
    assert 'Elapsed Time:' in s
    assert e == ''

@pytest.mark.skipif(platform.system() != 'Linux', reason="Linux-only test")
def test_cmdtime_sleep_3sec_linux():
    result = subprocess.run(['cmdtime', 'sleep 3'], capture_output=True)
    s = result.stdout.decode()
    e = result.stderr.decode()
    assert 'Elapsed Time:' in s
    assert e == ''

# Windows tests
@pytest.mark.skipif(platform.system() != 'Windows', reason="Windows-only test")
def test_cmdtime_dir_windows():
    result = subprocess.run(['cmdtime', 'dir'], capture_output=True)
    s = result.stdout.decode()
    e = result.stderr.decode()
    assert 'bytes free' in s
    assert 'Elapsed Time:' in s
    assert e == ''

@pytest.mark.skipif(platform.system() != 'Windows', reason="Windows-only test")
def test_cmdtime_ping_windows():
    result = subprocess.run(['cmdtime', 'ping 127.0.0.1 -n 2'], capture_output=True)
    s = result.stdout.decode()
    e = result.stderr.decode()
    assert 'Elapsed Time:' in s
    assert e == ''

@pytest.mark.skipif(platform.system() != 'Windows', reason="Windows-only test")
def test_cmdtime_timeout_3sec_windows():
    result = subprocess.run(['cmdtime', 'timeout /t 3'], capture_output=True)
    s = result.stdout.decode()
    #e = result.stderr.decode()
    assert 'Elapsed Time:' in s
    #assert e == ''
