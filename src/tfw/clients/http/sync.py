from tfw.clients.http.config import HttpClientConfig
import httpx

from tfw.utils.utils_classes import ILoggable


class SyncHttpClient(ILoggable):
    def __init__(self, config: HttpClientConfig):
        self._config = config
        self._http = httpx.Client(
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

    def request(
        self,
        method: str,
        url: str,
        **kwargs,
    ) -> httpx.Response:

        try:
            response = self._http.request(
                method=method,
                url=url,
                **kwargs
            )
            return response
        except httpx.HTTPError:
            self.logger.exception(
                "HTTP request failed. Method=%s URL=%s",
                method,
                url,
            )
            raise

    def get(self, url: str, **kwargs) -> httpx.Response:
        return self.request("GET", url, **kwargs)

    def post(self, url: str, **kwargs) -> httpx.Response:
        return self.request("POST", url, **kwargs)

    def put(self, url: str, **kwargs) -> httpx.Response:
        return self.request("PUT", url, **kwargs)

    def patch(self, url: str, **kwargs) -> httpx.Response:
        return self.request("PATCH", url, **kwargs)

    def delete(self, url: str, **kwargs) -> httpx.Response:
        return self.request("DELETE", url, **kwargs)

    def close(self):
        self._http.close()

    def __enter__(self) -> "SyncHttpClient":
        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):
        self.close()
