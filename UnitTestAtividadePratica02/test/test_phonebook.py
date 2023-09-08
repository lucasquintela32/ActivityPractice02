import pytest

from src.phonebook import Phonebook


class TestPhonebook:

    @pytest.fixture
    def setup(self):
        # Setup
        phonebook = Phonebook()
        phonebook.__init__()
        yield phonebook

    @pytest.mark.parametrize('name, number, result',
                             [
                                 ('Lucas', '8912675', 'number added'),
                                 ('#', '11111111', 'invalid name'),
                                 ('@', '11111111', 'invalid name'),
                                 ('!', '11111111', 'invalid name'),
                                 ('$', '11111111', 'invalid name'),
                                 ('%', '11111111', 'invalid name'),
                                 ('URGENCY', '185', 'invalid name'),
                                 ('Pedroa', '', 'Invalid number'),
                                 ('', '11111111', 'invalid name')
                             ])
    def test_add(self, setup, name, number, result):
        # Setup
        phonebook = setup
        expected_outcome = result

        # call
        result = phonebook.add(name, number)

        # Assessment
        assert result == expected_outcome

    @pytest.mark.parametrize('name, result',
                             [
                                 ('URGENCY', '185'),
                                 ('#', 'invalid name'),
                                 ('@', 'invalid name'),
                                 ('!', 'invalid name'),
                                 ('$', 'invalid name'),
                                 ('%', 'invalid name'),
                                 ('', 'invalid name')
                             ])
    def test_lookup(self, setup, name, result):
        # Setup
        phonebook = setup
        expected_outcome = result

        # call
        result = phonebook.lookup(name)

        # Assessment
        assert result == expected_outcome

    @pytest.mark.parametrize('result',
                             [
                                 ['URGENCY']
                             ])
    def test_get_names(self, setup, result):
        # Setup
        phonebook = setup
        expected_outcome = result

        # call
        result = phonebook.get_names()

        # Assessment
        assert result == expected_outcome

    @pytest.mark.parametrize('result',
                             [
                                 ['185']
                             ])
    def test_get_numbers(self, setup, result):
        # Setup
        phonebook = setup
        expected_outcome = result

        # call
        result = phonebook.get_numbers()

        # Assessment
        assert result == expected_outcome

    @pytest.mark.parametrize('result',
                             [
                                 'cleaned phonebook'
                             ])
    def test_clear(self, setup, result):
        # Setup
        phonebook = setup
        expected_outcome = result

        # call
        result = phonebook.clear()

        # Assessment
        assert result == expected_outcome

    @pytest.mark.parametrize('name, result',
                             [
                                 ('URGENCY', [{'URGENCY', '185'}]),
                                 ('POLI', [{'URGENCY', '185'}]),
                                 ('Pedro', [{'Pedrinho', '220'},
                                  {'220', 'Pedrinho2'}]),
                                 ('', [])
                             ])
    def test_search(self, setup, name, result):
        # Setup
        phonebook = setup
        phonebook.add('Pedrinho', '220')
        phonebook.add('Pedrinho2', '220')
        expected_outcome = result

        # call
        result = phonebook.search(name)

        # Assessment
        assert result == expected_outcome

    @pytest.mark.parametrize('result',
                             [
                                 [('CPedrinho', '160'),
                                  ('Pedrinho', '220'), ('URGENCY', '185')]
                             ])
    def test_get_phonebook_sorted(self, setup, result):
        # Setup
        phonebook = setup
        phonebook.add('Pedrinho', '220')
        phonebook.add('CPedrinho', '160')
        expected_outcome = result

        # call
        result = phonebook.get_phonebook_sorted()

        # Assessment
        assert result == expected_outcome

    @pytest.mark.parametrize('result',
                             [
                                 [('URGENCY', '185'), ('Pedrinho', '220'),
                                  ('CPedrinho', '160')]
                             ])
    def test_get_phonebook_reverse(self, setup, result):
        # Setup
        phonebook = setup
        phonebook.add('CPedrinho', '160')
        phonebook.add('Pedrinho', '220')
        expected_outcome = result

        # call
        result = phonebook.get_phonebook_reverse()

        # Assessment
        assert result == expected_outcome

    @pytest.mark.parametrize('name, result',
                             [
                                 ('URGENCY', 'deleted number'),
                                 ('Pedroa', 'Name does not exist in Phonebook')
                             ])
    def test_delete(self, setup, name, result):
        # Setup
        phonebook = setup
        expected_outcome = result

        # call
        result = phonebook.delete(name)

        # Assessment
        assert result == expected_outcome

    @pytest.mark.parametrize('name, number, result',
                             [
                                 ('URGENCY', '185', 'number not changed'),
                                 ('URGENCY', '19', 'changed number'),
                                 ('POLIIA', '19', 'Name does not exist in Phonebook')
                             ])
    def test_change_number(self, setup, name, number, result):
        # Setup
        phonebook = setup
        expected_outcome = result

        # call
        result = phonebook.change_number(name, number)

        # Assessment
        assert result == expected_outcome

    @pytest.mark.parametrize('number, result',
                             [
                                 ('185', [{'URGENCY', '185'},
                                  {'URGENCY1', '185'}])
                             ])
    def test_get_name_by_number(self, setup, number, result):
        # Setup
        phonebook = setup
        phonebook.add('URGENCY1', '185')
        phonebook.add('URGENCY2', '191')
        expected_outcome = result

        # call
        result = phonebook.get_name_by_number(number)

        # Assessment
        assert result == expected_outcome
