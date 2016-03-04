StackAPI: A Python wrapper for the Stack Exchange API
=====================================================

Release v\ |version|. (:ref:`Installation <install>`)

StackAPI is a simple Python wrapper for the `Stack Exchange
API <http://api.stackexchange.com/>`__ and supports the 2.2 API.

Retrieving data from the API is simple:

::

    from stackapi import StackAPI
    SITE = StackAPI('stackoverflow')
    comments = SITE.fetch('comments')

The above, will issue a call to the
|comments|_. end point on Stack Overflow and retrieve the 500 newest comments.

.. |comments| replace:: ``comments``
.. _comments: http://api.stackexchange.com/docs/comments

Supported Features
------------------

-  The Stack Exchange ``backoff`` parameter. It will automatically force a
   delay to match the parameter.
-  Read and write functionality via the API.
-  Retrieve multiple pages of results with a single call and merge
   all the results into a single response.
-  Throw exceptions returned by the API for easier troubleshooting.
-  Utilize `Requests <http://docs.python-requests.org/>`__.

StackAPI is supported on Python 2.7 - 3.5.

User Guide
----------

This portion of documentation provides details on how to utilize the 
library, and provides advanced examples of various use cases.

.. toctree::
   :maxdepth: 2
   
   user/intro
   user/install

The API Documentation
---------------------

Information about specific functions, classes, and methods are available
in this portion of documentation.

.. toctree::
   :maxdepth: 2

   api
   
Contributor Guidelines
----------------------

Information about how to contribute to the project is available in this
portion of the documentation.

.. toctree::
   :maxdepth: 2
   
   dev/contributing
   dev/todo
   dev/authors



