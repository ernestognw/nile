"""nile common module."""
from nile.common import DEPLOYMENTS_FILENAME


def register(address, abi, network, alias):
    """Register a new deployment."""
    file = f"{network}.{DEPLOYMENTS_FILENAME}"

    if alias is not None:
        if exists(alias, network):
            raise Exception(f"Alias {alias} already exists in {file}")

    with open(file, "a") as fp:
        if alias is not None:
            print(f"📦 Registering deployment as {alias} in {file}")
        else:
            print(f"📦 Registering {address} in {file}")

        fp.write(f"{address}:{abi}")
        if alias is not None:
            fp.write(f":{alias}")
        fp.write("\n")


def exists(identifier, network):
    """Return whether a deployment exists or not."""
    foo = next(load(identifier, network), None)
    print(network, identifier, foo)
    return foo is not None


def load(identifier, network):
    """Load deployments that matches an identifier (address or alias)."""
    with open(f"{network}.{DEPLOYMENTS_FILENAME}") as fp:
        for line in fp:
            [address, abi, *alias] = line.split(":")
            identifiers = [x.strip() for x in [address] + alias]
            if identifier in identifiers:
                yield address, abi
