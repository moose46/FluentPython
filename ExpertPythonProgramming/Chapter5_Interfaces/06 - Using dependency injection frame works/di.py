__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

#
# Author: Robert W. Curtiss
# di.py was created on June 10 2022 @ 10:50 AM
# Project: FluentPython
#

from injector import Module, provider, singleton
from redis import Redis

from interfaces import ViewsStorageBackend
from backends import CounterBackend, RedisBackend, SqlLiteBackend, SqlLiteMemBackend


class CounterModule(Module):
    '''Counter Module'''
    @provider
    @singleton
    def provide_storage(self) -> ViewsStorageBackend:
        print(type(self))
        return CounterBackend()


class RedisModule(Module):
    @provider
    def provide_storage(self, client: Redis) -> ViewsStorageBackend:
        return RedisBackend(client, "my-set")

    @provider
    @singleton
    def provide_redis_client(self) -> Redis:
        return Redis(host="redis")


class SQLiteModule(Module):
    @provider
    def provide_storage(self) -> ViewsStorageBackend:
        return SqlLiteBackend(dbname="backend.db")


class SQLiteMemModule(Module):
    @provider
    def provide_storage(self) -> ViewsStorageBackend:
        return SqlLiteMemBackend()
