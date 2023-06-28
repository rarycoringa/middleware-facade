import os

from unittest import mock

import pytest

from application.services.base import BaseService

class DummyServiceWithoutMethods(BaseService):
    ...

class DummyServiceWithMethods(BaseService):
    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "dummyservice.imd.ufrn.br"

    def port(self) -> int:
        return 80
    
    def url_env_var(self) -> str:
        return "DUMMY_SERVICE_URL"

class TestServiceInterface:
    def test_instantiate_abstract_service_interface(self):
        with pytest.raises(TypeError) as err:
            service = BaseService()
    
    def test_abstract_methods_without_rewrite(self):
        abstract_methods = [
            BaseService.protocol,
            BaseService.host,
            BaseService.port,
        ]

        for method in abstract_methods:
            with pytest.raises(NotImplementedError) as err:
                method()

    def test_instantiate_dummy_service_without_rewrite_methods(self):
        with pytest.raises(TypeError) as err:
            service = DummyServiceWithoutMethods()

    def test_instantiate_dummy_service_with_methods(self):
        service = DummyServiceWithMethods()

        assert isinstance(service, BaseService)

    @mock.patch.dict(
        os.environ,
        {},
        clear=True,
    )
    def test_method_base_url_built_from_abstract_methods(self):
        service = DummyServiceWithMethods()
        
        assert service.base_url == "https://dummyservice.imd.ufrn.br:80"

    @mock.patch.dict(
        os.environ,
        {"DUMMY_SERVICE_URL": "http://localhost:8181"},
        clear=True,
    )
    def test_method_base_url_built_from_env_var(self):
        service = DummyServiceWithMethods()
        
        assert service.base_url == "http://localhost:8181"