import pytest
from src.decorators import log


def test_log_to_file(tmp_path: pytest.TempPathFactory) -> None:
    """Тестирование записи логов в файл."""
    filename = tmp_path / "test_log.txt"

    @log(filename=str(filename))
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        assert "add called" in content
        assert "Inputs: args=(1, 2), kwargs={}" in content
        assert "Result: 3" in content
        assert "add ok" in content


def test_log_to_console(capsys: pytest.CaptureFixture) -> None:
    """Тестирование вывода логов в консоль."""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)

    captured = capsys.readouterr()
    assert "add called" in captured.out
    assert "Inputs: args=(1, 2), kwargs={}" in captured.out
    assert "Result: 3" in captured.out
    assert "add ok" in captured.out


def test_log_error_to_file(tmp_path: pytest.TempPathFactory) -> None:
    """Тестирование записи логов об ошибке в файл."""
    filename = tmp_path / "test_log.txt"

    @log(filename=str(filename))
    def divide(a: int, b: int) -> float:
        return a / b

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        assert "divide called" in content
        assert "Inputs: args=(1, 0), kwargs={}" in content
        assert "divide error: ZeroDivisionError" in content


def test_log_error_to_console(capsys: pytest.CaptureFixture) -> None:
    """Тестирование вывода логов об ошибке в консоль."""

    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    captured = capsys.readouterr()
    assert "divide called" in captured.out
    assert "Inputs: args=(1, 0), kwargs={}" in captured.out
    assert "divide error: ZeroDivisionError" in captured.out
