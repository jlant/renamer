"""Command line interface for renamer

Notes
-----
Click is a great Python package for creating command line interfaces.

Please see `Click documentation <https://click.palletsprojects.com/en/stable/>`_.
"""
import click

import renamer


@click.command()
@click.option("--verbose", is_flag=True, help="Print additional details.")
@click.version_option(renamer.__version__)
def cli(verbose):
    """Command line interface for renamer

    Renamer is a tool that renames files in a directory based on a pattern along with other options.
    """
    click.echo(
        "This is the command line interface for "
        "renamer"
    )
    click.echo("View help using option --help")
    click.echo("Check version using option --version")
    click.echo(
        "Add Click commands and groups to the command line interface at "
        "src/renamer/cli.py"
    )
    click.echo("See Click documenation at https://click.palletsprojects.com/en/stable/")
    click.echo(
        "Add your code as your see fit to the module at "
        "src/renamer/renamer.py"
    )
    if verbose:
        click.secho("VERBOSE mode is on", fg="green")


if __name__ == "__main__":
    cli()
