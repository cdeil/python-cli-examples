import pytest
from ..main import main


def test_main_success(capsys):
    # ret = main(['--loglevel', 'info'])
    ret = main(['--help'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert out == 'this is main\n'
    assert err == ''


def test_main_argparse_error(capsys):
    with pytest.raises(SystemExit) as exc:
        main(['--loglevel', 'spam'])
    out, err = capsys.readouterr()
    assert exc.value.args[0] == 2
    assert out == ''
    assert "error: argument --loglevel: invalid choice: 'spam'" in err
