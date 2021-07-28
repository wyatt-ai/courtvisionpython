#!/usr/bin/env python3
"""Basic regression test to download a match and check that it isn't empty."""

import courtvisionpython as cvp


def test_ao():
    response = cvp.utils.get_match(2021, "MS701", "ao")
    if len(response["courtVisionData"]) == 0:
        return False
    else:
        return True


def test_rg():
    response = cvp.utils.get_match(2021, "SD127", "rg")
    if len(response["courtVisionData"]) == 0:
        return False
    else:
        return True
