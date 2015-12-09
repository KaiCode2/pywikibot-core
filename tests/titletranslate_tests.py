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
            page = pywikibot.Page(site, u"20th_century")
        except Exception as error:
            print("fail to load " + page.title)
        self.assertNotEqual(pywikibot.titletranslate.translate(page=page, auto=True), [])

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
