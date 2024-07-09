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
    # [Setup]
    file_name = 'a_file.txt'
    
    # [Test]
    result = file_create(file_name)
    assert( result == True)
    assert(file_exists(file_name) == True)
    content = open(file_name).read()
    assert(content=='')

    # [Teardown]
    file_remove(file_name)
    # -----------------------------------------------------------------------

    # [Setup]
    file_name = 'b_file.txt'
    
    # [Test]
    result = file_create(file_name, 'Hello, World!')
    assert( result == True)
    assert(file_exists(file_name) == True)
    content = open(file_name).read()
    assert(content == 'Hello, World!')

    # [Teardown]
    file_remove(file_name)
    # -----------------------------------------------------------------------    

# -----------------------------------------------------------------------
count = 0
# -----------------------------------------------------------------------

@pytest.fixture
def from_file():
    """
    create a test file

    Returns:
        str: file name
    """
    global count 
    count += 1
    file_name = 'file_d.txt'
    with open(file_name, 'w') as f:
        f.write(f'Hello, World {count}!')
    return file_name

    # -----------------------------------------------------------------------

@pytest.fixture
def to_file():
    """
    return a test file

    Returns:
        str: file name
    """
    return 'file_d.txt'

    # -----------------------------------------------------------------------

def test_file_remove(from_file):
    """
    Test file removal.
    """
    # [Setup]
    file_1 = from_file
    
    # [Test]
    assert(file_exists(file_1) == True, "File does exist")    
    result = file_remove(file_1)
    assert(result == True, "File removal true result")
    assert(file_exists(file_1) == False, "File does not exist")

    result = file_remove(file_1)
    assert(result == False, "File removal false result")
    
    # [Teardown]
    # -----------------------------------------------------------------------

def test_file_copy(from_file, to_file):
    """
    Test file copy.
    """
    # [Setup]
    file_1 = from_file
    file_2 = to_file

    # [Test]
    file_copy(file_1, file_2)
    assert(file_exists(file_1) == True)
    content_from = open(from_file).read()
    content_to = open(file_2).read()
    assert(content_from == content_to)

    # [Teardown]
    file_remove(file_1)
    file_remove(file_2)
    # -----------------------------------------------------------------------

def test_file_append():   
    """
    Test file append.
    """
    # [Setup]
    content = 'Hello, World!'
    file_name = 'file_e.txt'
    
    # [Test]
    file_create(file_name, content)
    file_append(file_name, content)
    file_content = open(file_name).read()
    assert(2*content == file_content)
    
    # [Teardown]
    file_remove(file_name)
    # -----------------------------------------------------------------------

def test_file_show(from_file):
    """
    Test file show.
    """
    # [Setup]
    content = 'Hello, World!'
    file_name = 'file_f.txt'
    
    # [Test]
    file_create(file_name, content)
    file_output = file_show(file_name)
    assert(file_output == content)

    additional_content = '\nmore_content\nin multiple lines.'
    file_append(file_name, additional_content)

    file_output = file_show(file_name)
    assert(file_output == content + additional_content)

    # [Teardown]
    file_remove(file_name)
    # -----------------------------------------------------------------------
    # [Setup]
    content = 'first line!\nsecond line\nthird line'
    
    # [Test]
    file_create(file_name, content)
    file_output = file_show(file_name,insert_line_numbers=True)
    print(content)
    print(file_output)
    numbered_output = ''
    for line in enumerate(content.split('\n')):
        numbered_output += f'{line[0]+1:3}: {line[1]}\n'
    numbered_output = numbered_output[:-1]
    assert(numbered_output == file_output)
    
    # [Teardown]
    file_remove(file_name)
    # -----------------------------------------------------------------------