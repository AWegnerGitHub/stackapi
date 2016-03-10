.. _complex:

Complex API Queries
===================

The `API Documentation <http://api.stackexchange.com/docs/min-max>`__ 
explains that advanced queries can be generated using combinations of the
``min``, ``max``, ``sort``, ``fromdate`` and ``todate`` parameters. This
portion of the documentation explains how to replicate the examples provided
using StackAPI.

All Stack Overflow Users Created on Feb. 27th of 2011
-----------------------------------------------------

	>>> from stackapi import StackAPI
	>>> from datetime import datetime
	>>> SITE = StackAPI('stackoverflow')
	>>> SITE.max_pages=10
	>>> users = SITE.fetch('users', fromdate=datetime(2011,02,27), todate=datetime(2011,02,28))
	>>> len(users['items'])
	623
	
This one is pretty straight forward. The biggest thing here is that 
``max_pages`` is adjusted upward because there are more new users created
on that day than StackAPI returns by default.

Comments with at least a score of 10 on Ask Ubuntu
--------------------------------------------------

	>>> from stackapi import StackAPI
	>>> SITE = StackAPI('askubuntu')
	>>> comments = SITE.fetch('comments', min=10, sort='votes')
	>>> len(comments['items'])
	769
	
**Note** This value differs from the result in the ``total`` element. This is
*not* a StackAPI bug, but appears to be a problem on the Stack Exchange side.
This has been reported as a `bug <http://meta.stackexchange.com/q/276712/186281>`__
and this documentation will be adjusted depending on the outcome of the bug.

Of three specific posts on Server Fault, which one has the most recent activity
-------------------------------------------------------------------------------

	>>> from stackapi import StackAPI
	>>> SITE = StackAPI('serverfault')
	>>> SITE.max_pages=1
	>>> SITE.page_size=1
	>>> post = SITE.fetch('posts', ids=[3743, 327738, 339426], sort='activity', order='desc')
	>>> post['items'][0]['post_id']
	339426
	
Any favorites added in the month of December 2011 by Darin Dimitrov
-------------------------------------------------------------------

	>>> SITE = StackAPI('stackoverflow')
	>>> from datetime import datetime
	>>> favorites = SITE.fetch('users/{ids}/favorites', min=datetime(2011, 12, 1), max=datetime(2012, 1, 1), sort='added', ids=[29407])
	>>> len(favorites['items'])
	9

Questions created during the Modern Warfare 3 VS Skyrim Contest with the ``skryim`` tag and a score greater than 10 on Gaming Stack Exchange
--------------------------------------------------------------------------------------------------------------------------------------------

	>>> SITE = StackAPI('gaming')
	>>> from datetime import datetime
	>>> questions = SITE.fetch('questions', fromdate=datetime(2011,11,11), todate=datetime(2011,11,19), min=10, sort='votes', tagged='skyrim')
	>>> len(questions['items'])
	231
	
