import pytest
import mainfile

def findStudent():
    studentList = mainfile.searchStudent()
    assert 'bob' in studentList
    #pass

def findStudent():
    studentList = mainfile.searchStudent()
    assert 'bob' not in studentList
    #fail
