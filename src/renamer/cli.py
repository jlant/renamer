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
    help="A pattern to apply when renaming with the following placeholders: {index}, {original_name}",
)
@click.option(
    "--prefix",
    default=None,
    help="A prefix to add to a new file name.",
)
@click.version_option(__version__)
def cli(directory, pattern, prefix):
    """Command line interface for renamer

    Renamer is a tool that renames files in a directory based on a pattern along with
    other options.

    DIRECTORY is the path to the directory containing the files to rename.
    """
    click.echo(f"Renaming files in: {directory}")
    renamer.rename_files(directory=directory, pattern=pattern, prefix=prefix)
    click.echo("Done.")


if __name__ == "__main__":
    cli()
