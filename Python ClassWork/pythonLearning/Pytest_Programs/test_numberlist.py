from app.number_list import num_list


def test_number_list(setup_teardown_listmanip):
    l = num_list()

    assert l == 5, 'Count does not match'
