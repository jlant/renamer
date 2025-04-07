"""Main module for renamer

Renamer is a tool that renames files in a directory based on a pattern along with other
options.

"""

from datetime import datetime
from pathlib import Path


def rename_files(
    directory, pattern=None, prefix=None, date_format="%Y-%m-%d", dry_run=False
):
    """Rename files in a DIRECTORY based on a pattern along with other options.

    Parameters
    ----------
    directory : str
        A path-like string to the directory containing the files to rename.
    pattern : str, optional
        A pattern to apply when renaming.
        It has the following placeholders:
            {index} - an incrementing number
            {original_name} - the original file name without the extension
            {date} - the current date
        The default is None.
    prefix : str, optional
        A prefix to add to a new file name. The default is None.
    date_format : str, optional
        A date format to use with the {date} placeholder. The default is %Y-%m-%d
    dry_run : bool, optional
        A flag to show what the renaming result would be. The default is False.

    Raises
    ------
    ValueError
        If the directory path provided is not a valid directory.
    """
    # Create a Path object
    directory_path = Path(directory)

    # Check directory path
    if not directory_path.is_dir():
        raise ValueError(f"{directory} is not a valid directory.")

    # Loop through all the files in the directory provided and rename the files
    # accordingly
    for index, file_path in enumerate(sorted(directory_path.iterdir())):
        if file_path.is_file():
            original_name = file_path.stem
            extension = file_path.suffix

            # Initially, use original file name without extension
            new_name = original_name

            # Apply the pattern if provided
            if pattern:
                new_name = pattern.format(
                    index=index,
                    original_name=original_name,
                    date=datetime.now().strftime(date_format),
                )

            # Apply the prefix if provided
            if prefix:
                new_name = f"{prefix}{new_name}"

            # Add the extension
            new_name = f"{new_name}{extension}"

            # Create the full file path for the new file
            new_file_path = directory_path / new_name

            # Perform a dry run if provided
            if dry_run:
                print(f"[Dry run] Would rename: {file_path.name} -> {new_name}")
            else:
                # Rename the original full file path with the new full file path
                file_path.rename(new_file_path)


def main():
    """Main function.

    Example usage of the read_files function.
    """
    test_directory = Path(__file__).resolve().parents[2] / "tests" / "test_files"
    pattern = "{index}_{original_name}_hello"
    prefix = "new_"

    rename_files(directory=test_directory, pattern=pattern, prefix=prefix)


if __name__ == "__main__":
    main()
