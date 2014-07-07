from trytond.pool import PoolMeta
from trytond.model import ModelSQL, ModelView, fields

__all__ = ['RelationDepartment', 'PartyRelation', 'PartyRelationAll']
__metaclass__ = PoolMeta


class RelationDepartment(ModelSQL, ModelView):
    'Department'
    __name__ = 'party.relation.department'

    name = fields.Char('Name', required=True, translate=True)


class PartyRelation:
    __name__ = 'party.relation'

    department = fields.Many2One('party.relation.department', 'Department')


class PartyRelationAll(PartyRelation):
    __name__ = 'party.relation.all'
