import pytest
import mainfile

def testLateSubmission():
   lateSubmission = mainfile.lateSubmission(1)
   assert lateSubmission is True
   #pass

def testLateSubmission():
    lateSubmission = mainfile.lateSubmission(2)
    assert lateSubmission is True
    #fail
