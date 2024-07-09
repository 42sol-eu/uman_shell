from pathlib import Path        # https://docs.python.org/3/library/pathlib.html
from rich import print          # https://rich.readthedocs.io/en/latest/
from rich.console import Console

console = Console()


def file_exists(file_path: str) -> bool:
    """
    Check if a file exists at the given path.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return Path(file_path).is_file()

def file_create(file_name : str, content = '') -> bool:
    """
    Create a file with the given name.

    Args:
        file_name (str): The name of the file to create.

    Returns:
        bool: True if the file was created successfully, False otherwise.
    """
    try:
        with open(file_name, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        console.print(f'[red]Error creating file: {e}[/red]')
        return False

def file_remove(file_name: str) -> bool:
    """
    Remove a file with the given name.

    Args:
        file_name (str): The name of the file to remove.

    Returns:
        bool: True if the file was removed successfully, False otherwise.
    """
    try:
        Path(file_name).unlink()
        return True
    
    except Exception as e:
        console.print(f'[red]Error removing file: {e}[/red]')
        return False

def file_copy(from_file: str, to_file: str) -> bool:
    """
    Copy the contents of one file to another.

    Args:
        from_file (str): The file to copy from.
        to_file (str): The file to copy to.

    Returns:
        bool: True if the file was copied successfully, False otherwise.
    """
    try:
        with open(from_file, 'r') as f:
            content = f.read()
        with open(to_file, 'w') as f:
            f.write(content)
        return True
    
    except Exception as e:
        console.print(f'[red]Error copying file: {e}[/red]')
        return False
    
def file_append(file_name: str, add_content: str) -> bool:
    """
    Append content to a file.

    Args:
        file_name (str): The name of the file to append to.
        add_content (str): The content to append.

    Returns:
        bool: True if the content was appended successfully, False otherwise.
    """
    try:
        with open(file_name, 'a') as f:
            f.write(add_content)
        return True
    
    except Exception as e:
        console.print(f'[red]Error appending to file: {e}[/red]')
        return False
    

def file_show(file_name, insert_line_numbers=False):
    """
    (`cat`) Show the content of a file.

    Args:
        file_name (str): The name of the file to show.
    """
    first_line = True 
    with open(file_name, 'r') as f:
        bare_content = f.read()
        output = ''
    for i, line in enumerate(bare_content.split('\n')):
        if insert_line_numbers:
            next_line = f'{i+1:3}: {line}'
        else:
            next_line = line 
        
        print(next_line)
        if first_line:
            first_line = False
        else:
            output += '\n'
        output += next_line
    return output
