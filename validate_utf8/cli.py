import click
from validate_utf8 import find_utf8_errors


@click.command()
@click.argument(
    "path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, allow_dash=False),
)
def cli(path):
    "Validate UTF8 content of file"
    for error in find_utf8_errors(open(path, "rb").read()):
        print(error.reason)
        print(error.extract)
