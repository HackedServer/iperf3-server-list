import json
import yaml
import toml
import csv


def generate_csv_file(data):
    with open("data/servers.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["hostname", "port_start", "port_end", "protocols", "ip_versions"])

        for server in data["servers"]:
            writer.writerow(
                [
                    server["hostname"],
                    server["ports"]["start"],
                    server["ports"]["end"],
                    ",".join(server["protocols"]),
                    ",".join(server["ip_versions"]),
                ]
            )


def generate_json_file(data):
    with open("data/servers.json", "w") as f:
        json.dump(data, f, indent=2)


def generate_yaml_file(data):
    yaml.Dumper.ignore_aliases = lambda *args: True
    with open("data/servers.yaml", "w") as f:
        yaml.dump(data, f)


def generate_toml_file(data):
    with open("data/servers.toml", "w") as f:
        toml.dump(data, f)
