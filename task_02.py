#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Simple Docstring"""

import authentication
import getpass


def login(username, maxattempts):
    """str, int(optional). Prompt for password and tests if correct or not.

    Args:
        username(str): Arg of username as a string.
        maxattempts(int, optional): attmepts to enter correct password as int.

    Returns:
        Something.

    Example:
        >>>

    """
    authenticated = False

    while not authenticated:
        passinput = getpass.getpass()
        print passinput
        cred = authentication.authenticate(username, passinput)
        if cred == 'Yes':
            authenticated = True
            print 'Correct'
        elif cred == 'No':
            print 'Incorrect'

    print 'after loop'
