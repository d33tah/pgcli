import pytest
from pgcli.main import has_ddl_commannd, has_change_db_command


@pytest.mark.parametrize('sql', [
    'DROP TABLE foo',
    'SELECT * FROM foo; DROP TABLE foo',
])
def test_detect_ddl(sql):
    assert not has_change_db_command(sql)
    assert has_ddl_commannd(sql)


@pytest.mark.parametrize('sql', [
    '\\c foo',
    'SELECT * FROM foo; \\c foo',
])
def has_detect_change_db(sql):
    assert not has_ddl_commannd(sql)
    assert has_change_db_command(sql)
