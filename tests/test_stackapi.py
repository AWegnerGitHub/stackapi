#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This testing package makes anonymous API calls the Stack Exchange API. As a result, if you are receiving
`StackAPIError` exceptions on a majority of these, you have exceeded your anonymous calls to the API for the
day.

This will be corrected, by mocking the responses, at some point in the future.
"""

import unittest
from stackapi import StackAPI, StackAPIError


class Test_StackAPI(unittest.TestCase):
    def test_stackoverflow_exists(self):
        """Simply testing the object is created correctly"""
        self.assertEqual(StackAPI('stackoverflow')._name, "Stack Overflow")

    def test_asdfghjkl_not_exist(self):
        """Testing that it raises the correct error on unknown site"""
        with self.assertRaises(ValueError) as cm:
            StackAPI('asdfghjkl')
            self.assertEqual('Invalid Site Name provided', str(cm.exception))

    def test_no_site_provided(self):
        """Testing that it raises the correct error when no site is provided"""
        with self.assertRaises(ValueError) as cm:
            StackAPI()
            self.assertEqual('No Site Name provided', str(cm.exception))

    def test_nonsite_parameter(self):
        """Testing that it can retrieve data on end points that don't want
        the `site` parameter. Tested using Jeff Atwood's user id"""
        site = StackAPI('stackoverflow')
        site._api_key = None
        self.assertGreaterEqual(len(site.fetch('/users/1/associated')['items']), 1)

    def test_exceptions_thrown(self):
        """Testing that a StackAPIError is properly thrown"""
        with self.assertRaises(StackAPIError) as cm:
            site = StackAPI('stackoverflow')
            site._api_key = None
            site.fetch('errors/400')
        self.assertEqual(cm.exception.error, 400)
        self.assertEqual(cm.exception.code, 'bad_parameter')


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())