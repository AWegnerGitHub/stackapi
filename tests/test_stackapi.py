#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os.path
import unittest
from unittest.mock import patch
from stackapi import StackAPI
from stackapi import StackAPIError

TESTS_DIRECTORY = "tests"
directory = "tests/" if TESTS_DIRECTORY not in os.getcwd() else ""


def fake_stackoverflow_exists(
    self, endpoint=None, page=1, key=None, filter="default", **kwargs
):
    response_file = os.path.normpath(
        "{}mock_objects/test_stackoverflow_exists".format(directory)
    )
    with open(response_file) as json_file:
        j_data = json.load(json_file)
    return j_data


def fake_users(self, endpoint=None, page=1, key=None, filter="default", **kwargs):
    response_file = os.path.normpath(
        "{}mock_objects/test_users_associated".format(directory)
    )
    with open(response_file) as json_file:
        j_data = json.load(json_file)
    return j_data


class Test_StackAPI(unittest.TestCase):
    def test_no_site_provided(self):
        """Testing that it excludes the `site` when no site is provided."""
        site = StackAPI()
        self.assertEqual(first=site._base_url, second="https://api.stackexchange.com/2.3/")

    def test_no_endpoint_provided(self):
        """Testing that it raises the correct error when no endpoint is provided"""
        with self.assertRaises(ValueError) as cm:
            with patch(
                "stackapi.StackAPI.fetch", fake_stackoverflow_exists
            ) as mock_site:
                site = StackAPI("stackoverflow")
            site.fetch()
            self.assertEqual("No end point provided.", str(cm.exception))

    @patch("stackapi.StackAPI.fetch", fake_stackoverflow_exists)
    def test_stackoverflow_exists(self):
        """Simply testing the object is created correctly"""
        self.assertEqual(StackAPI("stackoverflow")._name, "Stack Overflow")

    @patch("stackapi.StackAPI.fetch", fake_stackoverflow_exists)
    def test_asdfghjkl_not_exist(self):
        """Testing that it raises the correct error on unknown site"""
        with self.assertRaises(ValueError) as cm:
            site = StackAPI("asdfghjkl")
            self.assertEqual("Invalid Site Name provided", str(cm.exception))

    def test_nonsite_parameter(self):
        """Testing that it can retrieve data on end points that don't want
        the `site` parameter. Tested using Jeff Atwood's user id"""
        with patch("stackapi.StackAPI.fetch", fake_stackoverflow_exists) as mock_site:
            site = StackAPI("stackoverflow")
        site._api_key = None
        with patch("stackapi.StackAPI.fetch", fake_users) as mock_users:
            self.assertGreaterEqual(len(site.fetch("/users/1/associated")["items"]), 1)

    def test_exceptions_thrown(self):
        """Testing that a StackAPIError is properly thrown

        This test hits the real API."""
        with self.assertRaises(StackAPIError) as cm:
            site = StackAPI("stackoverflow")
            site._api_key = None
            site.fetch("errors/400")
        self.assertEqual(cm.exception.error, 400)
        self.assertEqual(cm.exception.code, "bad_parameter")

    @patch("stackapi.StackAPI.fetch", fake_stackoverflow_exists)
    def test_default_base_url(self):
        """Testing that the base_url uses the default value"""
        self.assertEqual(
            StackAPI("stackoverflow")._base_url, "https://api.stackexchange.com/2.3/"
        )

    @patch("stackapi.StackAPI.fetch", fake_stackoverflow_exists)
    def test_override_base_url(self):
        """Testing that the base_url can be overridden"""
        self.assertEqual(
            StackAPI(
                name="stackoverflow",
                version="2.2",
                base_url="https://mystacksite.com/api",
                key="foo",
            )._base_url,
            "https://mystacksite.com/api/2.2/",
        )


if __name__ == "__main__":
    import sys

    sys.exit(unittest.main())
