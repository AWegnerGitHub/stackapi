.. _advanced:

.. automodule:: stackapi

Advanced Usage
==============

This portion of the documentation covers some of the more advanced features of
StackAPI.

Proxy Usage
-----------

Some users sit behind a proxy and need to get through that before accessing
the internet at large. StackAPI can handle this workflow.

A failure due to a proxy may look like this::

    >>> from stackapi import StackAPI, StackAPIError
    >>> try:
    ...     SITE = StackAPI('stackoverflow')
    ... except StackAPIError as e:
    ...     print(e.message)
    ...
    ('Connection aborted.', error(10060, 'A connection attempt failed
    because the connected party did not properly respond after a period of
    time, or established connection failed because connected host has failed
    to respond'))

This can be fixed, by passing a dictionary of http and https proxy addresses
when creating the :class:`StackAPI <stackapi.StackAPI>` class::

    >>> from stackapi import StackAPI, StackAPIError
    >>> proxies = {'http': 'http://proxy.example.com', 'https': 'http://proxy.example.com'}
    >>> try:
    ...     SITE = StackAPI('stackoverflow', proxy=proxies)
    ... except StackAPIError as e:
    ...     print(e.message)
    ...

The two important lines are where ``proxies`` is defined and the
modified :class:`StackAPI <stackapi.StackAPI>` initialization, which passes the
``proxies`` dictionary to the ``proxy`` argument.

End points that don't accept ``site`` parameter
-----------------------------------------------

Not all end points accept a site parameter. This is limited to only a few
end points. In this case, you'll receive a
:class:`StackAPIError <stackapi.StackAPIError>` with

- ``code`` equal to ``bad_parameter``
- ``message`` equal to ``This method does not accept a 'site' parameter``

The solution is to clear the ``_api_key``.

    >>> SITE = StackAPI('stackoverflow')
    >>> SITE._api_key = None
    >>> associated_users = SITE.fetch('/users/{}/associated'.format(63984), pagesize=1)
    >>> associated_users
    {
        "items": [
            {
                "badge_counts": {
                    "bronze": 91,
                    "silver": 56,
                    "gold": 11
                },
            "question_count": 94,
            "answer_count": 627,
            "last_access_date": 1457107832,
            "creation_date": 1255441385,
            "account_id": 63984,
            "reputation": 17438,
            "user_id": 189134,
            "site_url": "http://stackoverflow.com",
            "site_name": "Stack Overflow"
            }
        ],
        "has_more": true,
        "quota_max": 10000,
        "quota_remaining": 9989
    }

