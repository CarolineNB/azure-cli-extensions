# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import ProviderhubConfiguration
from .operations import CustomRolloutsOperations
from .operations import DefaultRolloutsOperations
from .operations import ProviderhubOperationsMixin
from .operations import NotificationRegistrationsOperations
from .operations import Operations
from .operations import ProviderRegistrationsOperations
from .operations import ResourceTypeRegistrationsOperations
from .operations import ResourceTypeRegistrationOperations
from .operations import SkusOperations
from .. import models


class Providerhub(ProviderhubOperationsMixin):
    """Microsoft Provider Hub.

    :ivar custom_rollouts: CustomRolloutsOperations operations
    :vartype custom_rollouts: providerhub.aio.operations.CustomRolloutsOperations
    :ivar default_rollouts: DefaultRolloutsOperations operations
    :vartype default_rollouts: providerhub.aio.operations.DefaultRolloutsOperations
    :ivar notification_registrations: NotificationRegistrationsOperations operations
    :vartype notification_registrations: providerhub.aio.operations.NotificationRegistrationsOperations
    :ivar operations: Operations operations
    :vartype operations: providerhub.aio.operations.Operations
    :ivar provider_registrations: ProviderRegistrationsOperations operations
    :vartype provider_registrations: providerhub.aio.operations.ProviderRegistrationsOperations
    :ivar resource_type_registrations: ResourceTypeRegistrationsOperations operations
    :vartype resource_type_registrations: providerhub.aio.operations.ResourceTypeRegistrationsOperations
    :ivar resource_type_registration: ResourceTypeRegistrationOperations operations
    :vartype resource_type_registration: providerhub.aio.operations.ResourceTypeRegistrationOperations
    :ivar skus: SkusOperations operations
    :vartype skus: providerhub.aio.operations.SkusOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ProviderhubConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.custom_rollouts = CustomRolloutsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.default_rollouts = DefaultRolloutsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.notification_registrations = NotificationRegistrationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.provider_registrations = ProviderRegistrationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_type_registrations = ResourceTypeRegistrationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_type_registration = ResourceTypeRegistrationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "Providerhub":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)