import os
from functools import lru_cache
from typing import Any


@lru_cache(maxsize=1)
def _configcat_client() -> Any | None:
    sdk_key = os.environ.get("CONFIGCAT_SDK_KEY")
    if not sdk_key:
        return None
    import configcatclient
    from configcatclient import ConfigCatOptions, PollingMode

    return configcatclient.get(
        sdk_key,
        ConfigCatOptions(polling_mode=PollingMode.LAZY_LOAD),
    )


def is_feature_enabled(key: str, default: bool = False) -> bool:
    client = _configcat_client()
    if client is None:
        return default
    return bool(client.get_value(key, default))
