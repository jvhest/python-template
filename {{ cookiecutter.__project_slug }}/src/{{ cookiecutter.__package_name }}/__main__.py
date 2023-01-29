"""Main cli or app entry point."""

import click
from tesje_cc.calculator import add


@click.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a: int, b: int) -> None:
    """CLI command."""
    click.echo(add(a, b))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    add_cli()
