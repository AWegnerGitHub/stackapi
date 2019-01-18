.. _quickstart:

.. automodule:: stackapi

Quickstart
==========

Ready to start talking to the Stack Exchange API? This page gives an
introduction on how to get started with StackAPI.

First, you need to:

* :ref:`Install <install>` StackAPI

.. _basic-retrieval:

Basic Data Retrieval
--------------------

Retrieving data is very simple.

First, import the StackAPI module::

    >>> from stackapi import StackAPI

Now we want to retrieve the most recent comments from Stack Overflow::

    >>> SITE = StackAPI('stackoverflow')
    >>> comments = SITE.fetch('comments')

This will return the 500 most recent comments on Stack Overflow, using the
default filter the API provides. The value passed to
:meth:`fetch <stackapi.StackAPI.fetch>` is an end point defined in the
`Stack Exchange API <http://api.stackexchange.com/>`__.

If you are looking for more information on how to tailor the results of your
queries. Take a look at the :ref:`Advanced Usage <advanced>` examples.

.. _change-num-results:

Change number of results
------------------------

By default, StackAPI will return up to 500 items in a single call. It may be
less than this, if there are less than 500 items to return. This is common
on new or low traffic sites.

The number of results can be modified by changing the ``page_size``
and ``max_pages`` values. These are multiplied together to get the maximum
total number of results. The API paginates the results and StackAPI recombines
those pages into a single result.

The number of API calls that are made is dependant on the ``max_pages`` value.
This will be the maximum number of calls that is made for this particular
request.

All of these changes to ``page_size`` and ``max_pages`` need to occur before
calls to ``fetch`` or ``send_data``.

Let's walk through a few examples::

    >>> SITE.page_size = 10
    >>> SITE.max_pages = 10

This will return up to 100 results. However, it will hit the API up to 10 times.

    >>> SITE.page_size = 100
    >>> SITE.max_pages = 1

This will result up to 100 results as well, but it will only hit the API
one time.

Stack Exchange limits the number of results per page to 100. If you want more
than 100 results, you need to increase the ``max_pages``.

    >>> SITE.page_size = 100
    >>> SITE.max_pages = 2

This will return up to 200 results and hit the API up to twice.

.. _get-exact-num-results:

Getting exact number of results
-------------------------------

If you want a specific number of results, but no more than that, you need to
perform some manipulations of these two values.

    >>> SITE.page_size = 50
    >>> SITE.max_pages = 3

This will return up to 150 results. It will also hit the API 3 times to get
these results. You can save an API hit by changing the values to::

    >>> SITE.page_size = 75
    >>> SITE.max_pages = 2

This will also return up to 150 results, but do so in only 2 API hits.

**Note:** Each "page" in an API call can have up to 100 results. In the first
scenario, above, we are "wasting" 150 results because we only allow each page
50 results. In the second scenario, we are wasting 50 results. If you do not
need an exact number of results, it is more efficient - API quota-wise - to set
the ``page_size`` to 100 and return the highest number of results per page that
the system allows.

.. _quick-errors:

Errors
------

StackAPI will throw an error if the Stack Exchange API returns an error. This
can be caught in an exception block by catching :class:`stackapi.StackAPIError`.
The exception has several values available to help troubleshoot the underlying
issue::

    except stackapi.StackAPIError as e:
        print("   Error URL: {}".format(e.url))
        print("   Error Code: {}".format(e.code))
        print("   Error Error: {}".format(e.error))
        print("   Error Message: {}".format(e.message))

This will print out the URL that was being accessed, the error number that the
API returns, the error code the API returns and the error message the API
returns. Using these values, it should be possible to determine the cause of
the error. The error code, message and number are all available in the
`documentation <http://api.stackexchange.com/docs/errors#filter=default&run=true>`__.

.. _quota-notes:

Note about Quotas
-----------------

Stack Exchange attempts to prevent abuse of their API by implementing a number
of `throttles <https://api.stackexchange.com/docs/throttle>`__. The quote values
that you have remaining are returned with more filters that StackAPI utilizes.
These appear as ``quota_remaining`` and ``quota_max`` values.

In some instances though (for example when using a ``filter='total'``), these
are not part of the Stack Exchange response. In these instances, StackAPI will
set the values to ``-1``. This is to make it clear that StackAPI does not know
the values and not provide you with an incorrect, positive, value.

To get accurate values for these two fields, you need to ensure that your
filters contain ``quota_remaining`` and ``quota_max``.
