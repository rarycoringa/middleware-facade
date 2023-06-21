import pytest

from urllib3.connectionpool import HTTPConnectionPool

@pytest.fixture(autouse=True)
def prevent_http_requests(monkeypatch):
    def urlopen_mock(self: HTTPConnectionPool, method, url, *args, **kwargs):
        raise RuntimeError(
            f"External HTTP connection attempt blocked: {method} {self.scheme}://{self.host}{url}"
        )
    
    monkeypatch.setattr(
        "urllib3.connectionpool.HTTPConnectionPool.urlopen",
        urlopen_mock,
    )