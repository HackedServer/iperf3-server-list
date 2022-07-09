import yaml

from .generate_data_files import generate_csv_file, generate_json_file, generate_yaml_file, generate_toml_file
from .server_tester import test_servers

default_server_values = {"ports": {"start": 5201, "end": 5201}, "protocols": ["tcp"], "ip_versions": ["v4"]}

data = yaml.safe_load(open("data/source.yaml"))

data["servers"] = sorted(
    [default_server_values | i for i in data["servers"] if i["hostname"] != "defaults.example"],
    key=lambda x: x["hostname"],
)


generate_csv_file(data)
generate_json_file(data)
generate_yaml_file(data)
generate_toml_file(data)
