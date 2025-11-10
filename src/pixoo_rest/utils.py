"""Utility functions for Pixoo REST API."""

from datetime import datetime

import requests


def try_to_request(url: str) -> bool:
    """Test if a URL is reachable.

    Args:
        url: The URL to test

    Returns:
        True if the URL responds with 200, False otherwise
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'[{timestamp}] Trying to request "{url}" ... ', end='')

        if requests.get(url, timeout=5).status_code == 200:
            print('OK.')
            return True
    except Exception:
        pass

    print('FAILED.')
    return False
