class TestCheckPhrase:
    def test_check_phrase(self):
        phrase = input("Set a phrase: ")
        len_ph = len(phrase)
        assert len_ph < 15, f"Phrase '{phrase}' contains more or equal to 15 symbols"

