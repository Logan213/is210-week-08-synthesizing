#! usr/bin/env pythong
# -*- coding: utf-8 -*-
"""Docstring"""


def get_matches(players):
    """A list of player names.

    Args:
        players(list, str): A list of strings with player names.

    Returns:
        A list of player names matched with no duplicates (half-cartesian).

    Examples:
        >>> get_matches(['Logan', 'Nora', 'Cameron'])
        [('Logan', 'Nora'), ('Logan', 'Cameron'), ('Nora', 'Cameron')]

        >>> get_matches(['Chad', 'Modesto'])
        [('Chad', 'Modesto')]

    """
    mylist = []
    for idx1, name in enumerate(players):
        for idx2, name in enumerate(players):
            if idx1 < idx2:
                mylist.append((players[idx1], name))
    return mylist
