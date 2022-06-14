import sqlite3
from collections import Counter
from typing import Dict
from redis import Redis

from interfaces import ViewsStorageBackend


class CounterBackend(ViewsStorageBackend):
    def __init__(self):
        self._counter = Counter()

    def increment(self, key: str):
        self._counter[key] += 1

    def most_common(self, n: int) -> Dict[str, int]:
        return dict(self._counter.most_common(n))


class RedisBackend(ViewsStorageBackend):
    def __init__(self, redis_client: Redis, set_name: str):
        self._client = redis_client
        self._set_name = set_name

    def increment(self, key: str):
        self._client.zincrby(self._set_name, 1, key)

    def most_common(self, n: int) -> Dict[str, int]:
        return {
            key.decode(): int(value)
            for key, value in self._client.zrange(
                self._set_name,
                0,
                n - 1,
                desc=True,
                withscores=True,
            )
        }


class SqlLiteBackend(ViewsStorageBackend):
    """
    sqlite database implementation
    """

    def __init__(self, dbname="backend.db"):
        try:
            self._conn = sqlite3.connect(dbname)
            self._c = self._conn.cursor()
            print(type(self._c))
            self._c.execute('''CREATE TABLE IF NOT EXISTS counter (count int, name text) ''')
            self._conn.commit()
        except Exception as e:
            print(e)
            return

    def increment(self, key: str):
        print()
        data = self._c.execute(f'''select count from counter where name = '{key}' ''')
        c = data.fetchone()
        if c is None:
            # insert new referer record into the database
            _cmd = f'''insert into counter values(1, '{key}')'''
            self._c.execute(_cmd)
        else:
            _cmd = f'''update counter set count = count + 1 where name='{key}' '''
            self._c.execute(_cmd)
        self._conn.commit()

    def most_common(self, n: int) -> Dict[str, int]:
        _sql = f'''select counter.count, name from counter
            order by 1 desc
            limit {n}'''
        self._c.execute(_sql)
        data = self._c.fetchall()
        return {http: cnt for cnt, http in data}


class SqlLiteMemBackend(ViewsStorageBackend):
    """
    sqlite database implementation
    """

    def __init__(self):
        try:
            # self._conn = sqlite3.connect(dbname)
            # print(f'{dbname} created ok!')
            self._conn = sqlite3.connect('memory.db:cachedb?mode=memory&cache=shared')
            print(f':memory created ok!')
            self._c = self._conn.cursor()
            self._c.execute('''CREATE TABLE IF NOT EXISTS counter (count int, name text) ''')
            self._conn.commit()
        except Exception as e:
            print(e)

    def increment(self, key: str):
        print()
        data = self._c.execute(f'''select count from counter where name = '{key}' ''')
        c = data.fetchone()
        if c is None:
            # insert new referer record into the database
            _cmd = f'''insert into counter values(1, '{key}')'''
            self._c.execute(_cmd)
        else:
            _cmd = f'''update counter set count = count + 1 where name='{key}' '''
            self._c.execute(_cmd)
        self._conn.commit()

    def most_common(self, n: int) -> Dict[str, int]:
        _sql = f'''select counter.count, name from counter
            order by 1 desc
            limit {n}'''
        self._c.execute(_sql)
        data = self._c.fetchall()
        return {http: cnt for cnt, http in data}
