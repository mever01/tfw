from pydantic import BaseModel, ConfigDict, Field


class HttpClientConfig(BaseModel):
    model_config = ConfigDict(frozen=True)

    base_url: str
    timeout: float = 10.0
    follow_redirects: bool = True
    verify_ssl: bool = True

    headers: dict[str, str] = Field(default_factory=dict)
    cookies: dict[str, str] = Field(default_factory=dict)

    proxy: str | None = None

    max_connections: int = 100
    max_keepalive_connections: int = 20

    http2: bool = False