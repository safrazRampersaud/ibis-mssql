from ibis.tests.expr.mocks import MockConnection
from ibis_mssql import connect
from ibis_mssql.client import MSSQLClient, MSSQLTable
import unittest
import pytest

pytest.importorskip('sqlalchemy')


class TestOps(unittest.TestCase):
    def setUp(self):
        self.con = MockConnection()

    def test_join_column_count(self):
        t1 = self.con.table('star1')
        t2 = self.con.table('star2')

        # msc = MSSQLClient()
        # new_t1 = msc.database(name=t1) <-- we would use this below as instances of ibis_mssql tables
        # new_t2 = msc.database(name=t2) <-- we would use this below as instances of ibis_mssql tables

        predicate = t1['foo_id'] == t2['foo_id']

        joined = t1.inner_join(t2, predicate)[[t1] + t2.get_columns([c for c in t2.columns if c not in t1.columns])]
        assert(len(joined.columns) == 6)