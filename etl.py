# %%
def transform(legacy_data):
    legacy_data = {vi: k for k, v in legacy_data.items() for vi in v}
    legacy_data = {k.casefold(): v for k, v in legacy_data.items()}
    return legacy_data


# %%
