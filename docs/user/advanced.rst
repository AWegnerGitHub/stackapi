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

    >>> from stackapi import StackAPI
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

Send data via the API
---------------------

StackAPI can send data to a Stack Exchange site, provided you have an 
application registered on `StackApps <http://stackapps.com/apps/oauth/register>`
and registered a token with `write <http://api.stackexchange.com/docs/write>` 
access. 

The following example assumes that you have a registered application and
registered a user against that application. The ``key`` value is provided
on the `Stack Apps App Management page <http://stackapps.com/apps/oauth/>`. 
The token is provided when a user authorizes the application to act on their
behalf. StackAPI does not perform or support this authorization. Stack Exchange
provides three methods for performing this 
`authorization <http://api.stackexchange.com/docs/authentication>`.

**Reminder**: The ``access_token`` is *per user*. It is associated with a 
single user. If StackAPI is acting on behalf of multiple users, the token
**must** be changed each time ``send_data`` is utilized.

	>>> from stackapi import StackAPI
	>>> SITE = SEAPI.SEAPI('stackoverflow', key=APP_KEY, access_token=ACCESS_TOKEN)
	>>> flag = SITE.send_data('comments/123/flags/add', option_id=option_id)

This block will flag comment ``123`` with the value of ``option_id``. 
This value can be found by checking which options are valid for the flag.

    >>> flag_options = SITE.fetch('comments/123/flags/options')
	
Assuming that comment ``123`` is valid, 
`this call <https://api.stackexchange.com/docs/comment-flag-options>`
will return a list of valid flags. From here, you select the ``option_id``
that matches the reason you want to flag. When you pass that via ``send_data``
in the ``option_id`` flag, StackAPI will issue a flag on behalf of the user
associated with the provided ``access_token``.