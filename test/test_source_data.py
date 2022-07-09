import yaml
import validators

data = yaml.safe_load(open("data/source.yaml"))
servers = data["servers"]

assert len(servers) > 0
assert len(data) == 1

# assert hostnames are unique
assert len(set(server["hostname"] for server in servers)) == len(servers)


for server in servers:
    # assert hostname is valid
    assert server["hostname"], "hostname is required"
    assert (
        validators.domain(server["hostname"])
        or validators.ipv4(server["hostname"])
        or validators.ipv6(server["hostname"])
    ), ("Invalid hostname: " + server["hostname"])

    # assert port is valid
    if server.get("ports"):
        assert isinstance(server["ports"], dict), "ports must be a dict"
        assert server["ports"]["start"] <= server["ports"]["end"], "start port must be less than or equal to end port"
        assert validators.between(server["ports"]["start"], 1, 65535), "start port must be between 1 and 65535"
        assert validators.between(server["ports"]["end"], 1, 65535), "end port must be between 1 and 65535"

    # assert protocol list is valid
    if server.get("protocols"):
        assert isinstance(server["protocols"], list), "protocols must be a list"
        assert all(
            protocol in ["tcp", "udp"] for protocol in server["protocols"]
        ), "protocols must be either tcp or udp"
        assert len(set(server["protocols"])) == len(server["protocols"])

    # assert ip_version is valid
    if server.get("ip_versions"):
        assert isinstance(server["ip_versions"], list), "ip_versions must be a list"
        assert all(
            ip_version in ["v4", "v6"] for ip_version in server["ip_versions"]
        ), "ip_versions must be either v4 or v6"
        assert len(set(server["ip_versions"])) == len(server["ip_versions"]), "duplicate ip_version"
