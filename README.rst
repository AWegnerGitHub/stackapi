This is a Python wrappers for the `Stack Exchange
API <http://api.stackexchange.com/>`__. This library supports Stack
Exchange API v2.2.

.. image:: https://readthedocs.org/projects/stackapi/badge/?version=latest
  :target: http://stackapi.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

This library has support for:

-  The Stack Exchange backoff parameter. It will automatically force a
   delay to match the parameter.
-  Read and write functionality via the API.
-  Can retrieve multiple pages of results with a single call and merges
   all the results into a single response.
-  Throws exceptions returned by the API for easier troubleshooting.
-  Utilizes `Requests <http://docs.python-requests.org/>`__.


Example usage:
==============

Establish a connection to Stack Overflow and gather some comments
-----------------------------------------------------------------

::

    from stackapi import StackAPI
    SITE = StackAPI('stackoverflow')
    comments = SITE.fetch('comments')

The above, will issue a call to the
|comments|_. end point on Stack Overflow.

.. |comments| replace:: ``comments``
.. _comments: http://api.stackexchange.com/docs/comments

Much more detailed documentation is available on
`ReadTheDocs <http://stackapi.readthedocs.io/>`__.
