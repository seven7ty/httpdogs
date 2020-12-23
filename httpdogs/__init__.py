# -*- coding: utf-8 -*-

"""
MIT License
Copyright (c) 2020-2020 itsmewulf

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import enum
import requests
import bs4

BASE_URL: str = "https://httpstatusdogs.com/"


class InvalidDog(ValueError):
    pass


class StatusCode(enum.Enum):
    """:class:`Enum` representing all HTTP status codes."""
    CONTINUE: int = 100
    SWITCHING_PROTOCOLS: int = 101
    PROCESSING: int = 102
    OK: int = 200
    SUCCESS: int = 200
    CREATED: int = 201
    ACCEPTED: int = 202
    NO_CONTENT: int = 204
    PARTIAL_CONTENT: int = 206
    MULTI_STATUS: int = 207
    MULTIPLE_CHOICES: int = 300
    MOVED_PERMANENTLY: int = 301
    FOUND: int = 302
    SEE_OTHER: int = 303
    NOT_MODIFIED: int = 304
    USE_PROXY: int = 305
    TEMPORARY_REDIRECT: int = 307
    BAD_REQUEST: int = 400
    UNAUTHORIZED: int = 401
    PAYMENT_REQUIRED: int = 402
    FORBIDDEN: int = 403
    NOT_FOUND: int = 404
    METHOD_NOT_ALLOWED: int = 405
    NOT_ACCEPTABLE: int = 406
    REQUEST_TIMEOUT: int = 408
    CONFLICT: int = 409
    GONE: int = 410
    LENGTH_REQUIRED: int = 411
    PRECONDITION_FAILED: int = 412
    PAYLOAD_TOO_LARGE: int = 413
    REQUEST_URI_TOO_LONG: int = 414
    UNSUPPORTED_MEDIA_TYPE: int = 415
    REQUEST_RANGE_NOT_SATISFIABLE: int = 416
    EXPECTATION_FAILED: int = 417
    IM_A_TEAPOT: int = 418
    ENHANCE_YOUR_CALM: int = 420
    MISDIRECTED_REQUEST: int = 421
    UNPROCESSABLE_ENTITY: int = 422
    LOCKED: int = 423
    FAILED_DEPENDENCY: int = 424
    UNORDERED_COLLECTION: int = 425
    UPGRADE_REQUIRED: int = 426
    TOO_MANY_REQUESTS: int = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE: int = 431
    NO_RESPONSE: int = 444
    BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS: int = 450
    UNAVAILABLE_FOR_LEGAL_REASONS: int = 451
    CLIENT_CLOSED_REQUEST: int = 499
    INTERNAL_SERVER_ERROR: int = 500
    NOT_IMPLEMENTED: int = 501
    BAD_GATEWAY: int = 502
    SERVICE_UNAVAILABLE: int = 503
    GATEWAY_TIMEOUT: int = 504
    VARIANT_ALSO_NEGOTIATES: int = 506
    INSUFFICIENT_STORAGE: int = 507
    LOOP_DETECTED: int = 508
    BANDWIDTH_LIMIT_EXCEEDED: int = 509
    NOT_EXTENDED: int = 510
    NETWORK_AUTHENTIDogION_REQUIRED: int = 511
    NETWORK_CONNECT_TIMEOUT_ERROR: int = 599


class HTTPDog:
    """
    Represents an HTTP Dog.

    Attributes
    ----------
    code: :class:`int`
        Status Code associated with this :class:`HTTPDog`
    name: :class:`str`
        Status Code Name associated with this :class:`HTTPDog`
    url: :class:`str`
        The URL associated with this :class:`HTTPDog`
    description: :class:`str`
        A string describing the status code's meaning.
    image: :class:`bytes`
        The image bytes associated with this :class:`HTTPDog`
    image_url: :class:`str`
        URL associated with the HTTP Dog image
    """

    def __init__(self, code: int, name: str, url: str, description: str, image: bytes, image_url: str):
        self.code: int = code
        self.name: str = name
        self.url: str = url
        self.description: str = description
        self.image: bytes = image
        self.image_url: str = image_url

    def __int__(self) -> int:
        return self.code

    def __str__(self) -> str:
        return self.name

    def __bytes__(self) -> bytes:
        return self.image


def _make_valid_name(name: str) -> str:
    """
    Transform a string in order to make it a valid Enum name

    Parameters
    -----------
    name: [:class:`str`]
        The status code name to make a valid :class:`StatusCode`
    Returns
    ---------
    :class:`str`
        The name that can be used to get a :class:`StatusCode`
    """

    return name.replace(" ", "_").upper()


def _pretty(name: str) -> str:
    """
    Make :class:`StatusCode` name pretty again
    Parameters
    -----------
    name: [:class:`str`]
        The status code name to make pretty
    Returns
    ---------
    :class:`str`
        The pretty name for the status code name given
    """

    return name.replace("_", " ").lower().title()


def _get_description(html: str) -> str:
    """
    Get the description of an HTTP Dog from the associated HTMl document.

    Parameters
    ----------
    html: :class:`str`
        The HTML document to scavenge for description

    Returns
    -------
    :class:`str`
        The recovered description
    """

    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html, "html.parser")
    _description: str = soup.find('p', {"class": "lead"}).get_text()
    return _description[_description.find(":") + 1:].strip()


def _get_image(html: str) -> tuple:
    """
    Get the image associated with the HTTP Dog.

    Parameters
    ----------
    html: :class:`str`
        The HTML document to scavenge for the image

    Returns
    -------
    :class:`str`
        The recovered image
    """
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html, "html.parser")
    image = soup.find('img', {"class": "thumbnail", "itemprop": "image"})
    url = BASE_URL + str(image.attrs['src'])[1:]
    return requests.get(url).content, url


def dog_by_code(code: int):
    """
    Get an :class:`HTTPDog` by status code

    Parameters
    -----------
    code: [:class:`int`]
        The status code to search for.

    Returns
    ---------
    :class:`HTTPDog`
        The :class:`HTTPDog` object.
    """

    res = requests.get(BASE_URL + str(code))
    content: str = str(res.content)
    try:
        dog_enum: StatusCode = StatusCode(code)
        url: str = BASE_URL + str(dog_enum.value)
        image = _get_image(content)
        return HTTPDog(int(code), _pretty(dog_enum.name), url, _get_description(res.text), image[0], image[1])
    except ValueError:  # Couldn't get the status code
        raise InvalidDog(f"{code} is not a valid status code")


def dog_by_name(name: str) -> HTTPDog:
    """
    Get an :class:`HTTPDog` by status code name

    Parameters
    -----------
    name: [:class:`str`]
        The status code name to search for.

    Returns
    ---------
    :class:`HTTPDog`
        The :class:`HTTPDog` object.
    """

    try:
        name: str = _make_valid_name(name)
        dog_enum: StatusCode = StatusCode[name]
        url: str = BASE_URL + str(dog_enum.value)
        res = requests.get(BASE_URL + str(dog_enum.value))
        content: str = str(res.content)
        image = _get_image(content)
        return HTTPDog(int(dog_enum.value), _pretty(dog_enum.name), url, _get_description(res.text), image[0], image[1])
    except ValueError:  # Couldn't get the status code name
        raise InvalidDog(f"{name} is not a valid status code name")
