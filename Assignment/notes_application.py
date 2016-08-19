class NotesApplication(object):
    """NotesApplication class created"""

    def __init__(self, author):
        """
        Create a constructor that does the following
                Takes in a parameter author as the author of the note and saves this as an instance variable.
                Create a notes list to store all the notes as an instance property.
        """
        self.author = author
        self.notes_list = []

    def create(self, note_content):
        """
                This function takes the note content as the parameter and
                adds it to the notes list of the object.
        """
        self.notes_list.append(note_content)

    def list(self):
        """
                This function lists out each of the notes in the notes list
                in the following format. The note_id parameter below represents the
                respective index of each of the items in the list,
                the NOTE_CONTENT represent the note content and the author
                represents the note author.

                Note ID: [note_id]
                [NOTE_CONTENT]
                By Author [author]
        """
        for item in self.notes_list:
            print "Note ID: " + str(self.notes_list.index(item)) + "\n" + "Our Note Content: " \
                + item + "\n\n" + \
                "By Author: " + self.author
        return self.notes_list

    def get(self, note_id):
        """
        This function takes a note_id which refers to
        the index of the note in the notes list and returns the
        content of that note as a string.

        """
        self.note_id = note_id
        for a in range(len(self.notes_list)):
            if self.note_id == a:
                return "Content Gotten AS: \n" + self.notes_list[a] + "\n"
            else:
                return None


    def search(self, search_text):
        """
        This function take a search string,
        search_text and returns all the notes with that
        text within it in the following format
        Showing results for search [<search_text>]
        """
        self.search_text = search_text
        for note in self.notes_list:
            if search_text == note:
                print "\t\t\t Showing for search" + search_text.upper()
                print "Note ID:" + str(self.notes_list.index(note)) + "\n"
                print note
                print "Author is: " + self.author

    def delete(self, note_id):
        """
        This function deletes the note at the index 
        note_id of the notes list.
        """
        try:
            if self.notes_list[note_id]:
                del(self.notes_list[note_id])
                return "Note Deleted"
        except:
            print 'NONE'

    def edit_id(self, note_id, new_content):
        """
         This function replaces the content in
         the note at note_id with new_content.
        """
        if self.notes_list[note_id]:
            self.notes_list[note_id] = new_content


