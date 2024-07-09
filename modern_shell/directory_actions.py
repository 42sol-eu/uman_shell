from pathlib import Path        # https://docs.python.org/3/library/pathlib.html
from rich import print          # https://rich.readthedocs.io/en/latest/
from rich.console import Console

console = Console()

# TODO: add chmod for directory
# TODO: add chown for directory
# TODO: add directory_active
# TODO: add directory_change inlude `.` and `..`
# TODO: add pushd 
# TODO: add popd
# TODO: how to add ln (hard and soft links)

def directory_exists(directory_path: str) -> bool:
    """
    `if [ -d {{directory_path}}` - checks if a directory exists at the given path.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        bool: True if the directory exists, False otherwise.
    """
    return Path(directory_path).is_dir()


def directory_create(directory_name : str, exist_ok = True) -> bool:
    """
    `mkdir {{directory_name}}` - create a directory with the given name.

    Args:
        directory_name (str): The name of the directory to create.
        exist_ok (bool): If True, don't raise an error if the directory already exists.
        
    Returns:
        bool: True if the directory was created successfully, False otherwise.
    """
    try:
        Path(directory_name).mkdir(parents=True, exist_ok=exist_ok)
        return True
    except Exception as e:
        console.print(f'[red]Error creating directory: {e}[/red]')
        return False

def directory_remove(directory_name: str, missing_ok : bool = False) -> bool:
    """
    `rmdir {{direcotry_name}}` or `rm -r {{directory_name}}` - removes a directory with the given name.

    Args:
        directory_name (str): The name of the directory to remove.
        missing_ok (bool): If True, don't raise an error if the directory is missing.
        
    Returns:
        bool: True if the directory was removed successfully, False otherwise.
    """
    try:
        Path(directory_name).rmdir()
        return True
    
    except Exception as e:
        console.print(f'[red]Error removing directory: {e}[/red]')
        return False


# TODO: think about an object orientated interface for Directory