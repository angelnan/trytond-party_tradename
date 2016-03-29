#This file is part party_tradename module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond import backend
from trytond.pyson import Eval

__all__ = ['Party']

STATES = {
    'readonly': ~Eval('active', True),
}
DEPENDS = ['active']


class Party:
    __metaclass__ = PoolMeta
    __name__ = 'party.party'
    trade_name = fields.Char('Trade Name', select=True, states=STATES,
        depends=DEPENDS)

    @classmethod
    def __register__(cls, module_name):
        TableHandler = backend.get('TableHandler')
        super(Party, cls).__register__(module_name)
        table = TableHandler(cls, module_name)
        table.column_rename('tradename', 'trade_name')

    @classmethod
    def search_rec_name(cls, name, clause):
        res = super(Party, cls).search_rec_name(name, clause)
        return ['OR', [res], [('trade_name',) + tuple(clause[1:])]]
