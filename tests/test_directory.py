import pytest 
from uman_shell import file_exists, file_create, file_copy, file_remove, file_append, file_show
from uman_shell import directory_exists, directory_create, directory_remove
# , directory_copy, directory_show


def test_directory_create():
    """
    Test directory creation.
    """
    # [Setup]
    directory_name = 'a_directory'
    
    # [Test]
    result = directory_create(directory_name)
    assert( result == True)
    assert(directory_exists(directory_name) == True)
    
    # [Teardown]
    directory_remove(directory_name)
    # -----------------------------------------------------------------------
    
    # [Setup]
    directory_name = 'b_directory'
    
    # [Test]
    result = directory_create(directory_name)
    assert( result == True)
    assert(directory_exists(directory_name) == True)
    
    # [Teardown]
    directory_remove(directory_name)
    # ----------------------------------------------------------------------- 

def test_directory_exists():
    """
    Test directory existence.
    
    """
    # [Setup]
    directory_name = 'a_directory'
    directory_create(directory_name)

    # [Test]
    assert directory_exists(directory_name) == True
    assert directory_exists("tests/test_nonexisting_directory") == False
