from collections.abc import Mapping, Sequence
from contextlib import contextmanager
from typing import Any, Iterator

from psycopg import Connection
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool

from tfw.clients.postgres.config import PostgresClientConfig

Params = Sequence[Any] | Mapping[str, Any] | None
Row = dict[str, Any]


class SyncPostgresClient:
    def __init__(self, config: PostgresClientConfig) -> None:
        self._config = config

        self._pool = ConnectionPool(
            conninfo=config.dsn,
            min_size=config.min_pool_size,
            max_size=config.max_pool_size,
            timeout=config.connection_timeout,
            kwargs={
                "row_factory": dict_row,
            },
            open=True,
        )

    def execute(
        self,
        query: str,
        params: Params = None,
    ) -> int:
        with self._pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.rowcount

    def fetch_one(
        self,
        query: str,
        params: Params = None,
    ) -> Row | None:
        with self._pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()

    def fetch_all(
        self,
        query: str,
        params: Params = None,
    ) -> list[Row]:
        with self._pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()

    @contextmanager
    def connection(
        self,
    ) -> Iterator[Connection[Row]]:
        with self._pool.connection() as connection:
            yield connection

    @contextmanager
    def transaction(
        self,
    ) -> Iterator[Connection[Row]]:
        with self._pool.connection() as connection:
            with connection.transaction():
                yield connection

    def close(self) -> None:
        self._pool.close()

    def __enter__(self) -> "SyncPostgresClient":
        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):
        self.close()
