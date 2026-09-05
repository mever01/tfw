from pydantic import BaseModel, ConfigDict, Field


class PostgresClientConfig(BaseModel):
    model_config = ConfigDict(frozen=True)

    dsn: str

    min_pool_size: int = Field(default=1, ge=0)
    max_pool_size: int = Field(default=10, ge=1)

    connection_timeout: float = Field(default=10.0, gt=0)
