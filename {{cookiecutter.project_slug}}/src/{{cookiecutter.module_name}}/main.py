import click

@click.command()
def {{ cookiecutter.first_subcommand }}:
    print("{{ cookiecutter.first_subcommand }}")