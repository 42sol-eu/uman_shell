from rich import print          # https://rich.readthedocs.io/en/latest/
from pathlib import Path        # https://docs.python.org/3/library/pathlib.html
from zipfile import ZipFile, is_zipfile
                                 # https://docs.python.org/3/library/zipfile.html

# TODO: add archive_exists

def has_archive_extension(archive_name: str) -> bool:
    """
    Checks if the given name has an archive extension.

    Args:
        archive_name (str): The name of the archive to check.

    Returns:
        bool: True if the name has an archive extension, False otherwise.
    """
    return  is_zipfile(archive_name) \
            or archive_name.endswith('.tar') \
            or archive_name.endswith('.tar.gz') \
            or archive_name.endswith('.tar.bz2') \
            or archive_name.endswith('.tar.xz') \
            or archive_name.endswith('.zip') \
            or archive_name.endswith('.7z') \
            or archive_name.endswith('.docx') \
            or archive_name.endswith('.xlsx') \
            or archive_name.endswith('.pptx') \
            or archive_name.endswith('.app') 
    


def archive_exists(archive_name: str) -> bool:
    """
    (`test -f {{archive_name}}`) - checks if an archive exists.

    Args:
        archive_name (str): The name of the archive to check.

    Returns:
        bool: True if the archive exists, False otherwise.
    """
    condition = Path(archive_name).is_file() \
                and has_archive_extension(archive_name)
    return condition

# TODO: add archive_create
# TODO: add archive_add
# TODO: add archive_comment_add
# TODO: add archive_pack (including password)
# TODO: add archive_extract (including password)
# TODO: add archive_list
# TODO: add archive_comment_show
