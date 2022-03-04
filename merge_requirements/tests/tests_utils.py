#!/usr/bin/env python
# encoding: utf-8

from unittest import TestCase
from unittest.mock import MagicMock
from utils import remove_comments, merge_dict

class TestUtils(TestCase):

    def test_remove_comments(self):

        text_file = '#COMENTARIOS\nCherryPy==3.2.4\nDjango==2.1.7\nIPTCInfo==1.9.5-6\nIon==0.6.4.2\n#COMENTARIO2\nJinja2==2.7\nMarkupSafe==0.18\nMySQL-python==1.2.3\nPIL==1.1.7-1\nPillow==2.1.0\nRoutes==2.0\nSQLAlchemy==0.5.8\nSouth==0.7.3\n' # noqa

        expected_text_file = 'CherryPy==3.2.4\nDjango==2.1.7\nIPTCInfo==1.9.5-6\nIon==0.6.4.2\nJinja2==2.7\nMarkupSafe==0.18\nMySQL-python==1.2.3\nPIL==1.1.7-1\nPillow==2.1.0\nRoutes==2.0\nSQLAlchemy==0.5.8\nSouth==0.7.3' # noqa

        self.assertEqual(
            remove_comments(text_file),
            expected_text_file,
            'test_remove_comments ok'
        )

    def test_merge_dict(self):

        bdict = {
            'CherryPy': '3.2.4',
            'Django': '1.4.13',
            'MySQL-python': '1.2.3',
            'Pillow': '2.1.0',
            'MarkupSafe': '0.18'
        }

        mdict = {
            'CherryPy': '3.2.0',
            'Django': '1.4.14',
            'MySQL-python': '1.2.3',
            'Pillow': '2.1.0',
            'MarkupSafe': '0.18',
            'SQLAlchemy': '0.5.8'
        }

        merged_dict = {
            'Django': '1.4.14',
            'MarkupSafe': '0.18',
            'MySQL-python': '1.2.3',
            'Pillow': '2.1.0',
            'SQLAlchemy': '0.5.8',
            'CherryPy': '3.2.4'
        }

        self.assertDictEqual(
            merge_dict(bdict, mdict)[0],
            merged_dict,
            'test_merge_dict'
        )

if __name__ == '__main__':
    unittest.main()
