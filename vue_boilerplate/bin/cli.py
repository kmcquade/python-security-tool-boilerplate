import click
from vue_boilerplate.command.generate_report import generate_report
from vue_boilerplate.bin.version import __version__


@click.group()
@click.version_option(version=__version__)
def vue_boilerplate():
    """
    vue_boilerplate: Boilerplate code for Python based security assessment tools that generate HTML reports.
    """


vue_boilerplate.add_command(generate_report)


def main():
    vue_boilerplate()


if __name__ == '__main__':
    vue_boilerplate()
