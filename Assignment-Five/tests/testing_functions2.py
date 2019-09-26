import pytest
import mainfile

def provideComment():
    comment = mainfile.comment()
    assert len(comment)<100
    #pass

def provideComment():
    comment = mainfile.comment()
    assert len(comment) == 0
    #fail
