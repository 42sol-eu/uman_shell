from pathlib import Path        # https://docs.python.org/3/library/pathlib.html
from rich import print          # https://rich.readthedocs.io/en/latest/
from rich.console import Console

console = Console()

# TODO: add chmod for file
# TODO: add chown for file
# TODO: how to add ln (hard and soft links)


def file_exists(file_path: str) -> bool:
    """
    `if [ -f {{file_path}}` - checks if a file exists at the given path.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return Path(file_path).is_file()

def file_create(file_name : str, content = '') -> bool:
    """
    `touch {{file_name}}` 
    and `echo {{content}} > {{file_name}}` - create a file with the given name.

    Args:
        file_name (str): The name of the file to create.
        content (str): The content to write to the file.

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

def file_remove(file_name: str, missing_ok : bool = False) -> bool:
    """
    `rm` - removes a file with the given name.

    Args:
        file_name (str): The name of the file to remove.
        missing_ok (bool): If True, don't raise an error if the file is missing.

    Note:
        The `rm -r {{file_name}}` command is not supported, because it is a directory operation.
        Use `remove_directory {{directory_path}}` instead.
        
    Returns:
        bool: True if the file was removed successfully, False otherwise.
    """
    try:
        Path(file_name).unlink(missing_ok=missing_ok)
        return True
    
    except Exception as e:
        console.print(f'[red]Error removing file: {e}[/red]')
        return False

def file_copy(from_file: str, to_file: str) -> bool:
    """
     `cp` - copys the contents of one file to another.

    Args:
        from_file (str): The file to copy from.
        to_file (str): The file to copy to.

    Returns:
        bool: True if the file was copied successfully, False otherwise.
    """
    if Path(to_file).is_dir():
        console.print(f'[red]Error moving file: {to_file} is a directory use `directory_copy` instead.[/red]')
        return False


    try:
        with open(from_file, 'r') as f:
            content = f.read()
        with open(to_file, 'w') as f:
            f.write(content)
        return True
    
    except Exception as e:
        console.print(f'[red]Error copying file: {e}[/red]')
        return False
    
def file_move(from_file: str, to_file: str) -> bool:
    """
    (`mv {{from_file}} {{to_file}}`) - moves a file from one location to another.

    Args:
        from_file (str): The file to move from.
        to_file (str): The file to move to.

    Note:
        If the `to_file` already exists, it will be overwritten.
        If the `from_file` is a directory the action will fail.

    Returns:
        bool: True if the file was moved successfully, False if a directory or the move did not work.
    """
    if Path(to_file).is_dir():
        console.print(f'[red]Error moving file: {to_file} is a directory. Use `directory_move` instead.[/red]')
        return False

    try:        
        Path(from_file).rename(to_file)
        return True
    
    except Exception as e:
        console.print(f'[red]Error moving file: {e}[/red]')
        return False
def file_append(file_name: str, add_content: str) -> bool:
    """
    `echo {{add_content}} >> {{file_name}}` - appends content to a file.

    Args:
        file_name (str): The name of the file to append to.
        add_content (str): The content to append.

    Note: 
        This will create a file if it does not exists.
        
    Returns:
        bool: True if the content was appended successfully, False otherwise.
    """
    if Path(file_name).is_dir():
        console.print(f'[red]Error appending file: {to_file} is a directory[/red]')
        return False

    try:
        with open(file_name, 'a') as f:
            f.write(add_content)
        return True
    
    except Exception as e:
        console.print(f'[red]Error appending to file: {e}[/red]')
        return False
    

def file_show(file_name, insert_line_numbers=False):
    """
    (`cat` or `nl`) - shows the content of a file.

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

# TODO: add function file_size(file_path: str, unit: str = 'B', human_readable=False) -> int:
# TODO: check is text file 
# TODO: check is script (#!{executable})
# TODO: check is binary file or executable (magic number)
# TODO: check is image file
# TODO: check is audio file
# TODO: check is video file
# TODO: check is pdf file   
# TODO: check if is office file (word, exel, powerpoint, also apple?)
# TODO: add anaysers (here or in seperate modules) like wc, grep, sed, awk, sort, uniq, cut, tr, head, tail, split, join, paste, diff, cmp, comm, tee, nl, od, strings, file, find, locate, which, whereis, type, time, date, cal, bc, seq, factor, expr
# TODO: add tools `less`, `more`, 