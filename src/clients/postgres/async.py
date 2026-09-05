from collections.abc import Mapping, Sequence
from contextlib import asynccontextmanager
from typing import Any, AsyncIterator

from psycopg import AsyncConnection
from psycopg.rows import dict_row
from psycopg_pool import AsyncConnectionPool

from src.clients.postgres.config import PostgresClientConfig


Params = Sequence[Any] | Mapping[str, Any] | None
Row = dict[str, Any]


class AsyncPostgresClient:
    def __init__(self, config: PostgresClientConfig) -> None:
        self._config = config

        self._pool = AsyncConnectionPool(
            conninfo=config.dsn,
            min_size=config.min_pool_size,
            max_size=config.max_pool_size,
            timeout=config.connection_timeout,
            kwargs={
                "row_factory": dict_row,
            },
            open=True,
        )

    async def execute(
        self,
        query: str,
        params: Params = None,
    ) -> int:
        async with self._pool.connection() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(query, params)
                return cursor.rowcount

    async def fetch_one(
        self,
        query: str,
        params: Params = None,
    ) -> Row | None:
        async with self._pool.connection() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(query, params)
                return await cursor.fetchone()

    async def fetch_all(
        self,
        query: str,
        params: Params = None,
    ) -> list[Row]:
        async with self._pool.connection() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(query, params)
                return await cursor.fetchall()

    @asynccontextmanager
    async def connection(
        self,
    ) -> AsyncIterator[AsyncConnection[Row]]:
        async with self._pool.connection() as connection:
            yield connection

    @asynccontextmanager
    async def transaction(
        self,
    ) -> AsyncIterator[AsyncConnection[Row]]:
        async with self._pool.connection() as connection:
            async with connection.transaction():
                yield connection

    async def close(self) -> None:
        await self._pool.close()

    async def __aenter__(self) -> "AsyncPostgresClient":
        return self

    async def __aexit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ) -> None:
        await self.close()