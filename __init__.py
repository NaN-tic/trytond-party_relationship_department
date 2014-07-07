# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .party import *


def register():
    Pool.register(
        RelationDepartment,
        PartyRelation,
        PartyRelationAll,
        module='party_relationship_department', type_='model')
