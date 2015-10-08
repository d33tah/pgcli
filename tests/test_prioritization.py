from pgcli.packages.prioritization import PrevalenceCounter


def test_prevalence_counter():
    keywords = ['SELECT', 'GROUP BY']
    counter = PrevalenceCounter(keywords)
    sql = '''SELECT * FROM foo WHERE bar GROUP BY baz;
             select * from foo;
             SELECT * FROM foo WHERE bar GROUP
             BY baz'''
    counter.update(sql)

    counts = [counter[k] for k in keywords]
    assert counts == [3, 2]
    assert counter['FROM'] == 0

