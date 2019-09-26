import pytest
import mainfile

def findAssignment():
    assignmentList = mainfile.selectAssignment()
    assert assgn1 in assignmentList
    #pass

def findAssignment():
    assignmentList = mainfile.selectAssignment()
    assert assgn1 not in assignmentList
    #fail
