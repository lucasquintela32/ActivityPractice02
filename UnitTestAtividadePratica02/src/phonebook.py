class Phonebook:

    invalid_characters = ['#', '@', '!', '$', '%']
    invalid_number = 'Invalid number'
    number_add = 'number added'
    invalid_name = 'invalid name'
    phonebook_limpo = 'cleaned phonebook'
    deleted_number = 'deleted number'
    name_doesnt_exist = 'Name does not exist in Phonebook'
    number_not_changed = 'number not changed'
    changed_number = 'changed number'

    def __init__(self):
        self.entries = {'URGENCY': '185'}

    def add(self, name, number):
        """
        Add a new contact to the phonebook
        :param name: name of person in string
        :param number: number of person in string
        :return: 'invalid name' or 'Invalid number' or 'number added'
        """
        # Improvement: in the failure returns, reducing the amount of if in the validation of invalid characters
        # Improvement: in checking names, validating if invalid characters exist in the name
        if any(char in name for char in self.invalid_characters):
            return self.invalid_name

        # Improvement: Invalid number check, validating if the length is greater than 0
        if len(number) == 0:
            return self.invalid_number

        # Improvement: invalid name check, validating if length is greater than 0
        if len(name) == 0:
            return self.invalid_name

        # Improvement: number added callbacks and addition of callback for invalid name
        if name not in self.entries:
            self.entries[name] = number
            return self.number_add
        else:
            return self.invalid_name

    def lookup(self, name):
        """
        Consult a name in phonebook
        :param name: name of person in string
        :return: return number of person with name
        """
        # Improvement: failure returns, reducing the amount of if in validating invalid characters
        if any(char in name for char in self.invalid_characters):
            return self.invalid_name

        # Improvement: invalid name check, validating if length is greater than 0
        if len(name) == 0:
            return self.invalid_name

        # Improvement: returns the number of the queried name and addition of the return for invalid name
        if name in self.entries:
            return self.entries[name]
        else:
            return self.invalid_name

    def get_names(self):
        """
        Consult all names in phonebook
        :return: return all names in phonebook
        """
        # Improvement: consultation of all existing names in the phonebook, returning in list format

    def get_numbers(self):
        """
        Consult all numbers in phonebook
        :return: return all numbers in phonebook
        """
        # Improvement: consultation of all existing numbers in the phonebook, returning in list format
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'cleaned phonebook'
        """
        self.entries = {}
        return self.phonebook_limpo

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        # Improvement: querying the data, searching and comparing part of the name with those existing in the phonebook,
        # returning in list format
        result = []
        for name, number in self.entries.items():
            if len(search_name) != 0:
                if search_name in name:
                    result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """
        Retrieve all entries in the phonebook in a sorted order
        :return: return phonebook in sorted order
        """
        # Improvement: data consultation, searching and organizing all existing entries in the phonebook,
        # returning in alphabetical list format
        phonebook_sorted = sorted(self.entries.items())
        return phonebook_sorted

    def get_phonebook_reverse(self):
        """
        Retrieve all entries in the phonebook in a reverse order
        :return: return phonebook in reverse sorted order
        """
        # Improvement: data consultation, searching and organizing all existing entries in the phonebook,
        # returning in list format in alphabetical order but in reverse
        phonebook_reverse = sorted(self.entries.items(), reverse=True)
        return phonebook_reverse

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'deleted number' if name exists, otherwise 'Name does not exist in Phonebook'
        """
        #  Improvement: return if the name does not exist in the phonebook
        if name in self.entries:
            self.entries.pop(name)
            return self.numero_deletado
        else:
            return self.name_doesn't_exist

    def change_number(self, name_on_phonebook, number_changed):
        """
        Change the number associated with a name in the phonebook
        :param name_on_phonebook: The name for which the number needs to be changed
        :param number_changed: The new number to be associated with the name
        :return: Return 'changed number' if the name exists and the number is different,
                 otherwise 'Name does not exist in Phonebook' or 'number not changed'
        """
        if name_on_phonebook in self.entries:
            if self.entries[name_on_phonebook] == number_changed:
                return self.number_not_changed

            self.entries[name_on_phonebook] = number_changed
            return self.numero_alterado
        else:
            return self.name_doesn't_exist

    def get_name_by_number(self, number_on_phonebook):
        """
        Get names associated with a specific number in the phonebook
        :param number_on_phonebook: The number for which names need to be retrieved
        :return: Return a list of dictionaries with names and the specified number
        """
        result = []
        for name, number in self.entries.items():
            if number_on_phonebook == number:
                result.append({name, number})
        return result
