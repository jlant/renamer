"""Command line interface for renamer"""

import click

from renamer import __version__, renamer


@click.command()
@click.argument(
    "directory", type=click.Path(exists=True, file_okay=False, dir_okay=True)
)
@click.option(
    "--pattern",
    default=None,
    help="A pattern to apply when renaming with the following placeholders: {index}, {original_name}, {date}",
)
@click.option(
    "--prefix",
    default=None,
    help="A prefix to add to a new file name.",
)
@click.option(
    "--date-format",
    default="%Y-%m-%d",
    help="A date format to use with the {date} placeholder. (default: %Y-%m-%d)",
)
@click.option(
    "--dry_run",
    is_flag=True,
    help="A flag to show what the renaming result would be. (default: False)",
)
@click.version_option(__version__)
def cli(directory, pattern, prefix, date_format, dry_run):
    """Command line interface for renamer

    Renamer is a tool that renames files in a directory based on a pattern along with
    other options.

    DIRECTORY is the path to the directory containing the files to rename.
    """
    renamer.rename_files(
        directory=directory,
        pattern=pattern,
        prefix=prefix,
        date_format=date_format,
        dry_run=dry_run,
    )


if __name__ == "__main__":
    cli()
