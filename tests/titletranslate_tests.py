# -*- coding: utf-8  -*-
"""TitleTranslate test module."""
#
# (C) Pywikibot team, 2007-2015
#
# Distributed under the terms of the MIT license.
#

import pywikibot.page
import pywikibot.site
import pywikibot.titletranslate

import unittest

class TestTitleTranslate(unittest.TestCase):
    """ Tests for titletranslate.py
    """

    def test_translate(self):
        print("")
        try:
            site = pywikibot.Site()
            page = pywikibot.Page(site, u"Wikimedia_Foundation")
        except Exception as error:
            print("fail to load " + page.title)
        self.assertEqual(pywikibot.titletranslate.translate(page=page), [])

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
