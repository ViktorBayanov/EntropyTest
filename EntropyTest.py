
class RKN:
    class node:
        def __init__(self):
            self.is_end = False
            self.next = dict()

    def __init__(self, banned_subnerworks_list):
        self.root = self.node()
        for subnetrwork in banned_subnerworks_list:
            subnetrwork = subnetrwork.split('/')
            mask = subnetrwork[-1]
            network_ip = subnetrwork[0].split('.')[:(int(mask) // 8)]
            walk = self.root
            for bit in network_ip:
                if not walk.next.get(bit):
                    walk.next[bit] = self.node()
                walk = walk.next[bit]
            walk.is_end = True

    def is_banned(self, subnetwork):
        subnetwork = subnetwork.split('.')
        walk = self.root
        for bit in subnetwork:
            if not walk.next.get(bit):
                return False
            walk = walk.next[bit]
            if walk.is_end:
                return True
        return walk.is_end

if __name__ == "__main__":
    r = RKN(['10.0.0.0/8', '8.8.8.8/32'])
    assert(r.is_banned('10.1.2.3') is True)  # True
    assert(r.is_banned('127.0.0.1') is False)  # False
    assert(r.is_banned('8.8.8.8') is True)  # True
    assert(r.is_banned('8.8.8.7') is False)  # False


    print("The test cases from the example was passed!")

    r2 = RKN(['198.168.0.1/8', '172.16.0.0/16', '85.89.127.36/24', '209.185.108.134/32'])

    assert(r2.is_banned('198.168.0.1') is True)
    assert (r2.is_banned('198.168.0.2') is True)
    assert (r2.is_banned('198.168.3.2') is True)
    assert (r2.is_banned('198.167.0.2') is True)
    assert (r2.is_banned('193.165.0.2') is False)

    assert (r2.is_banned('172.16.0.0') is True)
    assert (r2.is_banned('172.16.0.1') is True)
    assert (r2.is_banned('172.16.5.2') is True)
    assert (r2.is_banned('172.167.0.1') is False)
    assert (r2.is_banned('170.16.0.1') is False)

    assert (r2.is_banned('85.89.127.36') is True)
    assert (r2.is_banned('85.89.127.5') is True)
    assert (r2.is_banned('85.89.120.33') is False)
    assert (r2.is_banned('85.90.127.35') is False)
    assert (r2.is_banned('84.89.127.36') is False)

    assert (r2.is_banned('209.185.108.134') is True)
    assert (r2.is_banned('209.185.108.130') is False)
    assert (r2.is_banned('209.185.125.33') is False)
    assert (r2.is_banned('209.9.127.35') is False)
    assert (r2.is_banned('8.89.127.36') is False)

    print("My tests was passed!")