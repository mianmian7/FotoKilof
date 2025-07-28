# -*- coding: utf-8 -*-
"""
Copyright (c) 2024 Tomasz Łuczak, TeaM-TL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

module contains function for compression with Tinypng API
"""

import logging
import tinify

module_logger = logging.getLogger(__name__)

def compress_file(api_key, file_in, file_out):
    """
    Compress image with Tinypng API
    """
    if not api_key:
        module_logger.error("Tinypng API key is not provided.")
        return "key_missing"

    tinify.key = api_key

    try:
        source = tinify.from_file(file_in)
        source.to_file(file_out)
        return "success"
    except tinify.errors.AccountError as e:
        module_logger.error("Tinypng account error: %s", e)
        return "account_error"
    except tinify.errors.ClientError as e:
        module_logger.error("Tinypng client error: %s", e)
        return "client_error"
    except tinify.errors.ServerError as e:
        module_logger.error("Tinypng server error: %s", e)
        return "server_error"
    except Exception as e:
        module_logger.error("An unexpected error occurred: %s", e)
        return "unexpected_error"

# EOF
