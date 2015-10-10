from pgcli.packages.prioritization import PrevalenceCounter


def test_prevalence_counter():
    keywords = ['SELECT', 'GROUP BY']
    counter = PrevalenceCounter(keywords)
    sql = '''SELECT * FROM foo WHERE bar GROUP BY baz;
             select * from foo;
             SELECT * FROM foo WHERE bar GROUP
             BY baz'''
    counter.update(sql)

    kw_counts = [counter.keyword_count(x) for x in keywords]
    assert kw_counts == [3, 2]
    assert counter.keyword_count('FROM') == 0

    names = ['foo', 'bar', 'baz']
    name_counts = [counter.name_count(x) for x in names]
    assert name_counts == [3, 2, 2]
