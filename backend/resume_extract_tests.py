import unittest
from unittest.main import main
import os
from resume_extract import extract_text_from_pdf

path = "resume_examples"
class FlaskTest(unittest.TestCase):
    
    def test_regular(self):
        self.assertEqual(extract_text_from_pdf(os.path.join(path, "John Doe.pdf")), "John\nDoe")
    def test_newline(self):
        self.assertEqual(extract_text_from_pdf(os.path.join(path, "NewLine.pdf")), "Henry\nCash\nThis\nis\na\nsecond\nline.")
    def test_split(self):
        self.assertEqual(extract_text_from_pdf(os.path.join(path, "split.pdf")), "Henry\nCash\nThis\nis\na\nsecond\nline.\nThis\ntext\nis\nsplit")
if __name__=="__main__":
     unittest.main()