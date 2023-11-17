.. _advanced:

.. automodule:: stackapi

Advanced Usage
==============

This portion of the documentation covers some of the more advanced features of
StackAPI.

.. _more-parameters-fetch:

Calling ``fetch`` with various API parameters
---------------------------------------------

The various `end points <http://api.stackexchange.com/>`__ all take multiple
parameters to help filter the number of results you return. StackAPI will
accept all of these parameters.

As an example, let's look at the `comments <http://api.stackexchange.com/docs/comments>`__
end point. This end point will accept the following parameters:

- page
- pagesize
- fromdate
- todate
- order
- min
- max
- sort

``page`` and ``pagesize`` are handled by StackAPI through usage of the
``max_pages`` and ``page_size`` values of the :class:`StackAPI <stackapi.StackAPI>`
class. The others, are part of the ``kwargs`` accepted by
:meth:`fetch <stackapi.StackAPI.fetch>`.

Let's create an example using several of these parameters. This should return
a list of questions created between March 5, 2016 and March 6, 2016 that have
a score of at least 20 and are tagged ``python``::

    >>> from stackapi import StackAPI
    >>> SITE = StackAPI('stackoverflow')
    >>> questions = SITE.fetch('questions', fromdate=1457136000, todate=1457222400,
        min=20, tagged='python', sort='votes')
    >>> questions
    {
        'backoff': 0,
        'has_more': False,
        'items': [
                    {
                        u'accepted_answer_id': 35818398,
                        u'answer_count': 2,
                        u'creation_date': 1457186774,
                        u'is_answered': True,
                        u'last_activity_date': 1457246584,
                        u'last_edit_date': 1457200889,
                        u'link': u'http://stackoverflow.com/questions/35815093/sine-calculation-orders-of-magnitude-slower-than-cosine',
                        u'owner': {u'accept_rate': 80,
                                   u'display_name': u'Finwood',
                                   u'link': u'http://stackoverflow.com/users/1525423/finwood',
                                   u'profile_image': u'https://i.stack.imgur.com/xkRry.png?s=128&g=1',
                                   u'reputation': 1575,
                                   u'user_id': 1525423,
                                   u'user_type': u'registered'},
                        u'question_id': 35815093,
                        u'score': 22,
                        u'tags': [u'python', u'numpy', u'scipy', u'signal-processing'],
                        u'title': u'sine calculation orders of magnitude slower than cosine',
                        u'view_count': 404
                    }
                 ],
        'page': 1,
        'quota_max': 300,
        'quota_remaining': 171,
        'total': 0
    }

We can see that a single question matched our criteria.

**Note**: In the above example, we passed a timestamp value to the ``fromdate``
and ``todate`` parameters. StackAPI will also allow you to pass in 
``datetime`` objects and automatically perform this conversion for you.

StackAPI will perform this conversion to the following parameters:

- fromdate
- todate
- since
- min
- max

The ``min`` and ``max`` parameters are not exclusively date fields in the API.
StackAPI will only convert these to timestamps if a ``datetime`` object is 
passed.

.. _query-ids:

Calling ``fetch`` for specific IDs
----------------------------------

Some of the end points accept IDs. The documentation says these are semicolon
delimited lists of values. StackAPI, however, can handle this for you. You
just need to pass a ``list`` to the ``ids`` keyword argument::

    >>> from stackapi import StackAPI
    >>> SITE = StackAPI('stackoverflow')
    >>> badges = SITE.fetch('badges', ids=[222, 1306, 99999])
    >>> badges
    {
        'backoff': 0,
        'has_more': False,
        'items': [
                    {
                        u'award_count': 6036,
                        u'badge_id': 222,
                        u'badge_type': u'named',
                        u'link': u'http://stackoverflow.com/badges/222/altruist',
                        u'name': u'Altruist',
                        u'rank': u'bronze'
                    },
                    {
                        u'award_count': 43954,
                        u'badge_id': 1306,
                        u'badge_type': u'named',
                        u'link': u'http://stackoverflow.com/badges/1306/analytical',
                        u'name': u'Analytical',
                        u'rank': u'bronze'
                    }
                ],
        'page': 1,
        'quota_max': 300,
        'quota_remaining': 160,
        'total': 0
    }

Notice that we searched for 3 badges and only 2 results were returned. This is
how the API operates. If an ID doesn't exist, a result will not be returned or
indicated that it has been missed. It may be important for you to compare
results to what you searched for to see if any values are missing.

Another thing to notice here is that only ``badges`` was passed as the end
point. This works because the official end point is ``badges/{ids}``. If you
leave the ``{ids}`` off and it is the last part of the end point, StackAPI will
automatically add it for you. An identical call would look like this, with
``{ids}`` included in the end point declaration.

    >>> badges = SITE.fetch('badges/{ids}', ids=[222, 1306, 99999])

If ``{ids}`` is not at the end of the end point, then leaving it out of the
target end point is **not** optional. This will **not work**::

    >>> answers = SITE.fetch('/answers/comments', ids=[1, 2, 3])

However, this will work and will return comments associated with the selected
answers::

    >>> answers = SITE.fetch('/answers/{ids}/comments', ids=[1, 2, 3])

.. _proxy-usage:

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

.. _unwanted-parameter:

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
	
.. _send-data:

Send data via the API
---------------------

StackAPI can send data to a Stack Exchange site, provided you have an 
application registered on `StackApps <http://stackapps.com/apps/oauth/register>`__
and registered a token with `write <http://api.stackexchange.com/docs/write>`__ 
access. 

The following example assumes that you have a registered application and
registered a user against that application. The ``key`` value is provided
on the `Stack Apps App Management page <http://stackapps.com/apps/oauth/>`__. 
The token is provided when a user authorizes the application to act on their
behalf. StackAPI does not perform or support this authorization. Stack Exchange
provides three methods for performing this 
`authorization <http://api.stackexchange.com/docs/authentication>`__.

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
`this call <https://api.stackexchange.com/docs/comment-flag-options>`__
will return a list of valid flags. From here, you select the ``option_id``
that matches the reason you want to flag. When you pass that via ``send_data``
in the ``option_id`` flag, StackAPI will issue a flag on behalf of the user
associated with the provided ``access_token``.
