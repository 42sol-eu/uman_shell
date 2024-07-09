from modern_shell import file_exists, file_create, file_copy, file_remove, file_append, file_show
import pytest 

def test_file_exists():
    """
    Test file existence.
    
    """
    assert file_exists("tests/test_file.py") == True
    assert file_exists("tests/test_nonexisting_file.py") == False

def test_create_file():
    """
    Test file creation.
    """
    file_name = 'a_file.txt'
    result = file_create(file_name)
    assert( result == True)
    assert(file_exists(file_name) == True)
    content = open(file_name).read()
    assert(content=='')
    file_name = 'b_file.txt'
    result = file_create(file_name, 'Hello, World!')
    assert( result == True)
    assert(file_exists(file_name) == True)
    content = open(file_name).read()
    assert(content == 'Hello, World!')

@pytest.fixture
def from_file():
    """
    create a test file

    Returns:
        str: file name
    """
    file_name = 'file_d.txt'
    with open(file_name, 'w') as f:
        f.write('Hello, World!')
    return file_name

@pytest.fixture
def to_file():
    """
    return a test file

    Returns:
        str: file name
    """
    return 'file_d.txt'


def test_file_remove(from_file):
    """
    Test file removal.
    """

    assert(file_exists(from_file) == True, "File does exist")
    result = file_remove(from_file)
    assert(result == True, "File removal true result")
    assert(file_exists(from_file) == False, "File does not exist")

    result = file_remove(from_file)
    assert(result == False, "File removal false result")

def test_file_copy(from_file, to_file):
    """
    Test file copy.
    """
    file_copy(from_file, to_file)
    assert(file_exists(to_file) == True)
    content_from = open(from_file).read()
    content_to = open(to_file).read()
    assert(content_from == content_to)

    # Clean up
    file_remove(from_file)
    file_remove(to_file)
    
def test_file_append(from_file):   
    """
    Test file append.
    """
    content = 'Hello, World!'
    file_name = 'file_e.txt'
    file_create(file_name, content)
    file_append(file_name, content)
    file_content = open(file_name).read()
    assert(2*content == file_content)
    file_remove(file_name)

def test_file_show(from_file):
    """
    Test file show.
    """
    content = 'Hello, World!'
    file_name = 'file_f.txt'
    file_create(file_name, content)
    file_output = file_show(file_name)
    assert(file_output == content)

    additional_content = '\nmore_content\nin multiple lines.'
    file_append(file_name, additional_content)

    file_output = file_show(file_name)
    print('#'  * 20)
    print(file_output)
    print('#'  * 20)
    print(content + additional_content)
    assert(file_output == content + additional_content)
