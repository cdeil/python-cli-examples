import pytest
from ..main import main


def test_main_help(capsys):
    with pytest.raises(SystemExit) as exc:
        main(['--help'])
    out, err = capsys.readouterr()
    assert exc.value.args[0] == 0
    assert 'usage: greet [-h]' in out
    assert err == ''


def test_main_success(capsys):
    ret = main(['--loglevel', 'info'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert 'usage: greet [-h]' in out
    assert err == ''


def test_main_argparse_error(capsys):
    with pytest.raises(SystemExit) as exc:
        main(['--loglevel', 'spam'])
    out, err = capsys.readouterr()
    assert exc.value.args[0] == 2
    assert out == ''
    assert "error: argument --loglevel: invalid choice: 'spam'" in err
