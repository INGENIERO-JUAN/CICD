from feature_flags import is_feature_enabled


def test_feature_flag_defaults_false_without_sdk_key(monkeypatch):
    monkeypatch.delenv("CONFIGCAT_SDK_KEY", raising=False)
    from feature_flags import _configcat_client

    _configcat_client.cache_clear()
    assert is_feature_enabled("feature-resta", False) is False
