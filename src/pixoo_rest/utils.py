"""Utility functions for Pixoo REST API."""

from datetime import datetime

import httpx


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

        with httpx.Client(timeout=5.0) as client:
            response = client.get(url)
            if response.status_code == 200:
                print('OK.')
                return True
    except httpx.TimeoutException:
        print('FAILED (timeout after 5s).')
        return False
    except httpx.HTTPError as e:
        print(f'FAILED (HTTP error: {e}).')
        return False
    except Exception as e:
        print(f'FAILED (unexpected error: {e}).')
        return False

    print('FAILED.')
    return False
