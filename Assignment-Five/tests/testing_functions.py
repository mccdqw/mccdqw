import pytest
import mainfile #used for student login


def test_login():
    username = mainfile.getUsername()
    password = mainfile.getPassword()
    assert username != '' and password != ''
    #pass

def test_login():
    username = mainfile.getUsername()
    password = mainfile.getPassword()
    assert username == '' and password == ''
    #fail
