__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# backends.py was created on June 10 2022 @ 10:24 AM
# Project: FluentPython
#

from collections import Counter
from typing import Dict
from redis import Redis

from interfaces import ViewsStorageBackend


class CounterBackEnd(ViewsStorageBackend):
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
        self._client.zincrby(self._set_name,1,key)

    def most_common(self, n: int) -> Dict[str, int]:
        return {
            key.dcode(): int(value)
            for key, value in self._client.zrange(
                self._set_name,0,n - 1,
                desc=True,
                withscores=True,
            )
        }
