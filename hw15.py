import ipaddress


class Router:
    ''' 
    This class keeps all the information about routes in self.routes_table
    
    Each item in self.routes_table is a dict : 
    {
        'network_destination' : str,
        'netmask' : str,
        'gateway' : str,
        'interface' : str
    }

    '''
    def __init__(self):
        self.routes_table = []

    @staticmethod
    def make_route_info(ip : str, interface : str) -> dict:
        route = {
            'network_destination' : str(ipaddress.ip_network(ip, False).network_address),
            'netmask' : str(ipaddress.ip_network(ip, False).netmask),
            'gateway' : ip.split("/")[0],
            'interface' : interface or ip.split("/")[0]
        }
        return route

    def add_ip_adress(self, ip : str, interface : str = None):
        self.routes_table.append(self.make_route_info(ip, interface))

    def can_access(self, ip : str) -> bool:
        for route in self.routes_table:
            dest_network, mask = route["network_destination"], route["netmask"]
            ip_network = str(ipaddress.ip_network(f"{ip}/{mask}", False).network_address)
            if dest_network == ip_network:
                return True
        return False

    def add_route(self, ip_dest, gateway):
        if self.can_access(gateway):
            route = self.make_route_info(ip_dest, None)
            route["gateway"] = gateway
            route["interface"] = gateway
            self.routes_table.append(route)
        else:
            raise Exception(f"Can't access {gateway}")

    def delete_route(self, condition):
        '''
            condition : it's a function, returns bool : True means delete item;
            this function is being called with 1 parameter - route (dict with route info)
        '''
        new_routes_table = []
        for route in self.routes_table:
            if not condition(route):
                new_routes_table.append(route)
        self.routes_table = new_routes_table

    def print_table(self):
        pattern = "{:^35}{:^35}{:^35}{:^35}"
        print("-" * 140)
        print(pattern.format("Network Destination", "Netmask", "Gateway", "Interface"))
        print("-" * 140)
        for route in self.routes_table:
            net, mask = route["network_destination"], route["netmask"]
            gate, inter = route["gateway"], route["interface"]
            print(pattern.format(net, mask, gate, inter))
        print("-" * 140)
        

if __name__ == "__main__":
    router = Router()
    test_routes = [("172.16.0.0/16", "192.168.5.1"), ("172.24.0.0/16", "192.168.8.1"), ("172.24.0.0/16", "172.16.8.1")]

    print("Adding ip 192.168.5.14/24 on eth1\n")
    router.add_ip_adress("192.168.5.14/24", "eth1")

    for test_ip, test_gateway in test_routes:
        try:
            print(f"Trying to add route to {test_ip} through {test_gateway}")
            router.add_route(test_ip, test_gateway)
        except Exception as ex:
            print("Got exeption : ")
            print(ex)
        else:
            print("Added successfully")

    print("\nTable of routes\n")
    router.print_table()

    print("Deleting first record in table")
    router.delete_route(lambda x : x["gateway"] == "192.168.5.14")

    router.print_table()
    