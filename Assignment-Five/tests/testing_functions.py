import pytest
import mainfile 


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
