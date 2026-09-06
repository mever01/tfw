import httpx

from tfw.clients.http.config import HttpClientConfig
from tfw.utils.utils_classes import ILoggable


class AsyncHttpClient(ILoggable):
    def __init__(self, config: HttpClientConfig) -> None:
        self._config = config

        self._http = httpx.AsyncClient(
            base_url=config.base_url,
            timeout=config.timeout,
            follow_redirects=config.follow_redirects,
            verify=config.verify_ssl,
            headers=config.headers,
            cookies=config.cookies,
            proxy=config.proxy,
            http2=config.http2,
            limits=httpx.Limits(
                max_connections=config.max_connections,
                max_keepalive_connections=config.max_keepalive_connections,
            ),
        )

    async def request(
        self,
        method: str,
        url: str,
        **kwargs,
    ) -> httpx.Response:
        try:
            response = await self._http.request(
                method=method,
                url=url,
                **kwargs,
            )
            return response

        except httpx.HTTPError:
            self.logger.exception(
                "HTTP request failed. Method=%s URL=%s",
                method,
                url,
            )
            raise

    async def get(self, url: str, **kwargs,) -> httpx.Response:
        return await self.request("GET", url, **kwargs)

    async def post(self, url: str, **kwargs,) -> httpx.Response:
        return await self.request("POST", url, **kwargs)

    async def put(self, url: str, **kwargs,) -> httpx.Response:
        return await self.request("PUT", url, **kwargs)

    async def patch(self, url: str, **kwargs,) -> httpx.Response:
        return await self.request("PATCH", url, **kwargs)

    async def delete(self, url: str, **kwargs,) -> httpx.Response:
        return await self.request("DELETE", url, **kwargs)

    async def close(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> "AsyncHttpClient":
        return self

    async def __aexit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ) -> None:
        await self.close()
