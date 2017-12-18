import pytest
from ..main import main


def test_hello(capsys):
    with pytest.raises(SystemExit) as exc:
        main(['hello', '--help'])
    out, err = capsys.readouterr()
    assert exc.value.args[0] == 0
    assert 'usage: greet hello [-h]' in out
    assert err == ''
