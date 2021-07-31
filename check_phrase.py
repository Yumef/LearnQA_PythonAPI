class TestCheckPhrase:
    def test_check_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Phrase '{phrase}' contains more or equal to 15 symbols"

