import os

from unittest import mock

import pytest

from application.utils.service import ServiceInterface

class DummyServiceWithoutMethods(ServiceInterface):
    ...

class DummyServiceWithMethods(ServiceInterface):
    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "service.imd.ufrn.br"

    def port(self) -> int:
        return 80

class TestServiceInterface:
    def test_instantiate_abstract_service_interface(self):
        with pytest.raises(TypeError) as err:
            service = ServiceInterface()
    
    def test_abstract_methods_without_rewrite(self):
        abstract_methods = [
            ServiceInterface.protocol,
            ServiceInterface.host,
            ServiceInterface.port,
        ]

        for method in abstract_methods:
            with pytest.raises(NotImplementedError) as err:
                method()

    def test_instantiate_dummy_service_without_rewrite_methods(self):
        with pytest.raises(TypeError) as err:
            service = DummyServiceWithoutMethods()

    def test_instantiate_dummy_service_with_methods(self):
        service = DummyServiceWithMethods()

        assert isinstance(service, ServiceInterface)

    def test_method_base_url_built_from_abstract_methods(self):
        service = DummyServiceWithMethods()

        assert service.base_url() == "https://service.imd.ufrn.br:80"

    @mock.patch.dict(
        os.environ,
        {
            "ACCOUNT_SERVICE_URL": "http://localhost:8181",
        }
    )
    def test_method_base_url_built_from_env_var(self):
        service = DummyServiceWithMethods()

        assert service.base_url() == "http://localhost:8181"