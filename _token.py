# This file is part of Coog. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import os
import binascii

from trytond.pool import PoolMeta
from trytond.model import ModelSQL, ModelView, fields

__all__ = [
    'Token',
    ]


class Token(ModelSQL, ModelView, metaclass=PoolMeta):
    'API Token'
    __name__ = 'api.token'

    active = fields.Boolean('Active')
    name = fields.Char('Name', required=True)
    key = fields.Char('Key', required=True)
    user = fields.Many2One('res.user', 'User', required=True)
    party = fields.Many2One('party.party', 'Party')

    @classmethod
    def default_active(cls):
        return True

    @classmethod
    def default_key(cls):
        return binascii.hexlify(os.urandom(24)).decode('utf-8')

    @classmethod
    def check(cls, key):
        tokens = cls.search([('key', '=', key)])
        if tokens:
            token = tokens[0]
            return token.user.id, token.party.id if token.party else None
        else:
            return None, None
