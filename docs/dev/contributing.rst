.. _contributing:

Contributor's Guide
===================

If you're reading this, you're probably interested in contributing to StackAPI.
Thank you! The fact that you're even considering
contributing to the StackAPI project is *very* generous of you.

This document lays out guidelines and advice for contributing to this project.
If you're thinking of contributing, please start by reading this document and
getting a feel for how contributing to this project works. If you have any
questions, feel free to reach out to `Andrew Wegner`_, the primary maintainer.

.. _Andrew Wegner: https://github.com/AWegnerGitHub/stackapi/issues

The guide is split into sections based on the type of contribution you're
thinking of making, with a section that covers general guidelines for all
contributors.

Be Nice
----------

StackAPI has one important rule covering all forms of contribution,
including reporting bugs or requesting features. This golden rule is
"Be Nice".

**All contributions are welcome**, as long as
everyone involved is treated with respect.

.. _early-feedback:

Early Feedback
------------------

If you are contributing, do not feel the need to sit on your contribution until
it is polished and complete. It helps everyone involved for you to
seek feedback as early as you possibly can. Submitting an early, unfinished
version of your contribution for feedback does not decrease your chances of
getting that contribution accepted, and can save you from putting a lot of work
into a contribution that is not suitable for the project.

Contribution Suitability
------------------------

Our project maintainers have the last word on whether or not a contribution is
suitable. All contributions will be considered carefully, but from
time to time, contributions will be rejected because they do not suit the
current goals or needs of the project.

Code Contributions
------------------

Steps for Submitting Code
~~~~~~~~~~~~~~~~~~~~~~~~~

When contributing code, you'll want to follow this checklist:

1. Fork the repository on GitHub.
2. Run the tests to confirm they all pass on your system. If they don't, you'll
   need to investigate why they fail. If you're unable to diagnose this
   yourself, raise it as a bug report by following the guidelines in this
   document: :ref:`bug-reports`.
3. Write tests that demonstrate your bug or feature. Ensure that they fail.
   Note that many of our tests use `mock`_ to prevent burning through API
   quota. We ask that you do them and provide a mocked response.
4. Make your change.
5. Run the entire test suite again, confirming that all tests pass *including
   the ones you just added*.
6. Send a GitHub Pull Request to the main repository's ``master`` branch.
   GitHub Pull Requests are the expected method of code collaboration on this
   project.

.. _mock: https://pypi.python.org/pypi/mock

Code Review
~~~~~~~~~~~

Contributions will not be merged until they've been reviewed. You should
implement any code review feedback unless you strongly object to it. In the
event that you object to the code review feedback, you should make your case
clearly and calmly. If, after doing so, the feedback is judged to still apply,
you must either apply the feedback or withdraw your contribution.

Documentation Contributions
---------------------------

Documentation improvements are always welcome! The documentation files live in
the ``docs/`` directory of the codebase. They're written in
`reStructuredText`_, and use `Sphinx`_ to generate the full suite of
documentation.

When contributing documentation, please do your best to follow the style of the
documentation files. This means a soft-limit of 79 characters wide in your text
files and a semi-formal, but friendly and approachable, prose style.

When presenting Python code, use single-quoted strings (``'hello'`` instead of
``"hello"``).

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org/index.html


.. _bug-reports:

Bug Reports
-----------

Bug reports are hugely important! Before you raise one, though, please check
through the `GitHub issues`_, **both open and closed**, to confirm that the bug
hasn't been reported before. Duplicate bug reports can be a huge drain on the
time of other contributors, and should be avoided as much as possible.

.. _GitHub issues: https://github.com/awegnergithub/stackapi/issues


Feature Requests
----------------

If you believe there is a feature missing, feel free to raise a feature
request. Please provide as much detail about the request as you can including
some of the following information:

- Intended use case(s)
- Short falls you have with the current version
- Possible expected results
