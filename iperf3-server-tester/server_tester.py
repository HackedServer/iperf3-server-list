import iperf3
from typing import List, Dict, Any


def test_servers(server_list: List[Dict]) -> List[Dict]:
    for server in server_list:
        client = iperf3.Client()
        client.duration = 2
        client.server_hostname = server["hostname"]
        client.port = server["ports"]["start"]
        client.zerocopy = True
        client.protocol = "tcp"
        client.verbose = True
        results: iperf3.TestResult = client.run()
        print(results)
