import iperf3
import json
import yaml
import toml
import csv


data = yaml.safe_load(open("data/source.yaml"))

data["servers"] = sorted(
    [i for i in data["servers"] if i["hostname"] != "defaults.example"],
    key=lambda x: x["hostname"],
)

yaml.dump(data, open("data/servers.yaml", "w"))
json.dump(data, open("data/servers.json", "w"), indent=2)
toml.dump(data, open("data/servers.toml", "w"))
csv.writer(open("data/servers.csv", "w")).writerows(data["servers"])

"""
client = iperf3.Client()
client.duration = 2
client.server_hostname = "la.speedtest.clouvider.net"
client.port = 5201
client.zerocopy = True
client.protocol = "tcp"
client.verbose = True
results: iperf3.TestResult = client.run()
print(results)
"""
