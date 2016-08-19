import unittest

from notes_application import NotesApplication


class TestNotesApplication(unittest.TestCase):
    """Tests for Note Application"""

    def test_object_is_instance_with_empty_string(self):
        object1 = NotesApplication('')
        self.assertIsInstance(object1, NotesApplication)

    def test_object_instance_with_string(self):
        object2 = NotesApplication('One')
        self.assertIsInstance(object2, NotesApplication)

    def test_init_error_due_to_less_arguments(self):
        with self.assertRaises(TypeError):
            NotesApplication()

    def test_author_exists(self):
        note1 = NotesApplication('Author1')
        self.assertEqual(note1.author, 'Author1')
        note2 = NotesApplication('Author2')
        self.assertEqual(note2.author, 'Author2')
        note3 = NotesApplication('Author3')
        self.assertNotEqual(note3.author, 'author2')

    def test_creates_list(self):
        author1 = NotesApplication('AuthorOne')
        author1.create('Note 1')
        self.assertIs(author1.list(), list)


if __name__ == "__main__":
    unittest.main()
