import unittest
from os import path
from mailmerge import MailMerge


class MergeFootnoteTest(unittest.TestCase):
    def test(self):
        with MailMerge(path.join(path.dirname(__file__), 'test_merge_footnote.docx')) as document:
            self.assertEqual(document.get_merge_fields(), {'test_field'})
