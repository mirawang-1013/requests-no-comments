"""Requests HTTP library API.

This module provides the main public API for the Requests library,
offering convenient functions for making HTTP requests.
"""

from . import sessions





def request(method, url, **kwargs):
    """Constructs and sends a Request.

    Args:
        method: Method for the new Request object (GET, POST, PUT, etc.).
        url: URL for the new Request object.
        **kwargs: Optional arguments that request takes.

    Returns:
        Response object.

    Example:
        >>> import requests
        >>> response = requests.request('GET', 'https://httpbin.org/get')
        >>> response.status_code
        200
    """
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)





def get(url, params=None, **kwargs):
    """Sends a GET request.

    Args:
        url: URL for the new Request object.
        params: Dictionary or bytes to be sent in the query string.
        **kwargs: Optional arguments that request takes.

    Returns:
        Response object.
    """
    return request("get", url, params=params, **kwargs)





def options(url, **kwargs):
    """Sends an OPTIONS request.

    Args:
        url: URL for the new Request object.
        **kwargs: Optional arguments that request takes.

    Returns:
        Response object.
    """
    return request("options", url, **kwargs)





def head(url, **kwargs):
    """Sends a HEAD request.

    Args:
        url: URL for the new Request object.
        **kwargs: Optional arguments that request takes.

    Returns:
        Response object.
    """
    kwargs.setdefault("allow_redirects", False)
    return request("head", url, **kwargs)





def post(url, data=None, json=None, **kwargs):
    """Sends a POST request.

    Args:
        url: URL for the new Request object.
        data: Dictionary, list of tuples, bytes, or file-like object to send.
        json: JSON serializable Python object to send in the body.
        **kwargs: Optional arguments that request takes.

    Returns:
        Response object.
    """
    return request("post", url, data=data, json=json, **kwargs)





def put(url, data=None, **kwargs):
    """Sends a PUT request.

    Args:
        url: URL for the new Request object.
        data: Dictionary, list of tuples, bytes, or file-like object to send.
        **kwargs: Optional arguments that request takes.

    Returns:
        Response object.
    """
    return request("put", url, data=data, **kwargs)





def patch(url, data=None, **kwargs):
    """Sends a PATCH request.

    Args:
        url: URL for the new Request object.
        data: Dictionary, list of tuples, bytes, or file-like object to send.
        **kwargs: Optional arguments that request takes.

    Returns:
        Response object.
    """
    return request("patch", url, data=data, **kwargs)





def delete(url, **kwargs):
    """Sends a DELETE request.

    Args:
        url: URL for the new Request object.
        **kwargs: Optional arguments that request takes.

    Returns:
        Response object.
    """
    return request("delete", url, **kwargs)

