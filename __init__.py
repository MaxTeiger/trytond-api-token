# This file is part of Coog. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import Pool
from . import _token


def register():
    Pool.register(
        token.Token,
        module='api_token', type_='model')
