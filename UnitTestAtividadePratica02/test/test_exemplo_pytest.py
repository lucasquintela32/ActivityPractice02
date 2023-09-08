class TestPhonebook:

    # Comparison between numbers with different values
    def test_add_1(self):
        assert 1 == 2

    # Comparison between numbers with the same value, but String and Integer
    def test_add_2(self):
        assert "1" == 1

    # Comparison between 2 identical characters, but between uppercase and lowercase
    def test_add_3(self):
        assert "F" == "f"

    # Assertion with boolean with false value, resulting in the test as false
    def test_add_4(self):
        assert False

    # Assertion with boolean value true, resulting in test as true
    def test_add_5(self):
        assert True
