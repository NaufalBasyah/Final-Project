
class Paragraph(object):
    def __init__(self, path):
        self.path = path

    def open_file(self):
        self.file = open(self.path, 'r')

    def close_file(self):
        self.file.close()

    def get_paragraph(self):
        self.text = self.file.read()
        print(self.text)

