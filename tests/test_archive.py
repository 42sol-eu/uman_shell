import pytest
from modern_shell import has_archive_extension, archive_exists #, archive_create

def test_has_archive_extension():
    """
    Test archive extension check.
    """
    # [Setup]
    archive_name = 'a_directory.zip'
    
    # [Test]
    assert has_archive_extension(archive_name) == True
    assert has_archive_extension("tests/test_nonexisting_archive") == False

def test_archive_exists():
    """
    Test archive existence.
    """
    # [Setup]
    archive_name = 'a_directory.zip'
    
    # [Test]
    assert archive_exists(archive_name) == False
    assert archive_exists("tests/test_nonexisting_archive") == False

    # [Teardown]
    # archive_create(archive_name)
    # assert archive_exists(archive_name) == True
    # archive_remove(archive_name)
    # assert archive_exists(archive_name) == False