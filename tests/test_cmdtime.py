#!/usr/bin/env python3
import cmdtime
import platform
import pytest
import subprocess

# common tests
def test_cmdtime_echo():
    result = subprocess.run(['cmdtime', 'echo test_cmdtime_echo'], capture_output=True, text=True)
    assert 'test_cmdtime_echo' in result.stdout
    assert 'Elapsed Time:' in result.stdout
    assert result.stderr == ''

# Linux tests
@pytest.mark.skipif(platform.system() != 'Linux', reason="Linux-only test")
def test_cmdtime_dir_linux():
    result = subprocess.run(['cmdtime', 'ls -al'], capture_output=True, text=True)
    assert 'total' in result.stdout
    assert 'Elapsed Time:' in result.stdout
    assert result.stderr == ''

@pytest.mark.skipif(platform.system() != 'Linux', reason="Linux-only test")
def test_cmdtime_ping_linux():
    result = subprocess.run(['cmdtime', 'ping 127.0.0.1 -c 2'], capture_output=True, text=True)
    assert 'Elapsed Time:' in result.stdout

@pytest.mark.skipif(platform.system() != 'Linux', reason="Linux-only test")
def test_cmdtime_sleep_3sec_linux():
    result = subprocess.run(['cmdtime', 'sleep 3'], capture_output=True, text=True)
    assert 'Elapsed Time:' in result.stdout

# Windows tests
@pytest.mark.skipif(platform.system() != 'Windows', reason="Windows-only test")
def test_cmdtime_dir_windows():
    result = subprocess.run(['cmdtime', 'dir'], capture_output=True, text=True)
    assert 'bytes free' in result.stdout
    assert 'Elapsed Time:' in result.stdout
    assert result.stderr == ''

@pytest.mark.skipif(platform.system() != 'Windows', reason="Windows-only test")
def test_cmdtime_ping_windows():
    result = subprocess.run(['cmdtime', 'ping 127.0.0.1 -n 2'], capture_output=True, text=True)
    assert 'Elapsed Time:' in result.stdout

@pytest.mark.skipif(platform.system() != 'Windows', reason="Windows-only test")
def test_cmdtime_timeout_3sec_windows():
    result = subprocess.run(['cmdtime', 'timeout /t 3'], capture_output=True, text=True)
    assert 'Elapsed Time:' in result.stdout

