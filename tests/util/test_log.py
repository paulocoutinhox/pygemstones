import pytest

import pygemstones.util.log as l


# -----------------------------------------------------------------------------
def test_debug(capsys):
    message = "debug test"
    l.d(message)

    captured = capsys.readouterr()
    assert message in captured.out


# -----------------------------------------------------------------------------
def test_info(capsys):
    message = "info test"
    l.i(message)

    captured = capsys.readouterr()
    assert message in captured.out


# -----------------------------------------------------------------------------
def test_warn(capsys):
    message = "warning test"
    l.w(message)

    captured = capsys.readouterr()
    assert message in captured.out


# -----------------------------------------------------------------------------
def test_success(capsys):
    message = "success test"
    l.s(message)

    captured = capsys.readouterr()
    assert message in captured.out


# -----------------------------------------------------------------------------
def test_ok(capsys):
    message = "[OK]"
    l.ok()

    captured = capsys.readouterr()
    assert message in captured.out


# -----------------------------------------------------------------------------
def test_failed(capsys):
    message = "[FAILED]"
    l.failed("failed test")

    captured = capsys.readouterr()
    assert message in captured.out


# -----------------------------------------------------------------------------
def test_colored(capsys):
    message = "colored test"
    l.colored(message, l.PURPLE)

    captured = capsys.readouterr()
    assert message in captured.out


# -----------------------------------------------------------------------------
def test_error():
    message = "error test"

    with pytest.raises(SystemExit) as info:
        l.e(message)

        assert info.value.args[0] == 10
        assert message in info.value.args[1]


# -----------------------------------------------------------------------------
def test_fatal():
    message = "fatal test"

    with pytest.raises(SystemExit) as info:
        l.f(message)

        assert info.value.args[0] == 10
        assert message in info.value.args[1]


# -----------------------------------------------------------------------------
def test_bullet(capsys):
    message = "bullet test"
    l.bullet(message, l.GREEN)

    captured = capsys.readouterr()
    assert message in captured.out
    assert "•" in captured.out


# -----------------------------------------------------------------------------
def test_clean_message(capsys):
    message = "clean message test"
    l.m(message)

    captured = capsys.readouterr()
    assert message in captured.out


# -----------------------------------------------------------------------------
def test_bold(capsys):
    message = "bold test"
    l.bold(message)

    captured = capsys.readouterr()
    assert message in captured.out


# -----------------------------------------------------------------------------
def test_bold_with_color(capsys):
    message = "bold test"
    l.bold(message, l.GREEN)

    captured = capsys.readouterr()
    assert message in captured.out
