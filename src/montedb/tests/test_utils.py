from config.utils import find_neighbours


class TestAdult:

    def test_find_neighbours(self, df_school_fee):
        lower, upper = find_neighbours(1958, df_school_fee, 'income')
        assert lower == 4
        assert upper == 5
        exact_match = find_neighbours(2000, df_school_fee, 'income')
        assert exact_match.to_list()[0] == 5
