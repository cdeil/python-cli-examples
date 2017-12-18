from click.testing import CliRunner
from .cli import cli


def test_cli_hello_success():
    runner = CliRunner()
    result = runner.invoke(cli, ['hello', 'Guido'])
    assert result.exit_code == 0
    assert result.output == 'Hello Guido\n'
    assert result.exception is None


def test_cli_hello_fail():
    runner = CliRunner()
    result = runner.invoke(cli, ['hello'])  # Forget to pass a "name" argument
    assert result.exit_code == 2
    assert 'Usage: cli hello' in result.output
    assert 'Error: Missing argument "name".' in result.output
    assert isinstance(result.exception, SystemExit)


def test_cli_hello_help():
    runner = CliRunner()
    result = runner.invoke(cli, ['hello', '--help'])
    assert result.exit_code == 0
    assert 'Usage: cli hello [OPTIONS] NAME' in result.output
    assert result.exception is None
