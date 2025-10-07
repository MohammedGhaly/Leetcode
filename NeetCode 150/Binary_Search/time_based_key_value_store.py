class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.time_map.get(key, None) is None:
            self.time_map[key] = [(timestamp, value)]
        else:
            self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if self.time_map.get(key, None) is None:
            return ""

        entries = self.time_map[key]
        l = 0
        r = len(entries) - 1

        while l <= r:
            mid = (l + r) // 2

            if entries[mid][0] == timestamp:
                return entries[mid][1]
            if entries[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        # Not found
        if r > -1:
            return entries[r][1]
        return ""

        # dic = {1: 3, 2: 6, 3: 9}
        # x = dic.copy()
        # print(dic)
        # print(x)
        # x[4] = 7
        # print(dic)
        # print(x)
time_map = TimeMap()
time_map.set("key1",  "apple", 1)
time_map.set("key1",  "apple2", 2)
time_map.set("key1",  "apple3", 3)
time_map.set("key2",  "app4", 4)
time_map.set("key2",  "app5", 5)
time_map.set("key3",  "ap6", 6)
time_map.set("key4",  "ap7", 7)


print(time_map.get("key1", 1))
print(time_map.get("key2", 4.5))
print(time_map.get("key3", 7))
print(time_map.get("key4", 7))
# print(time_map.get("key4", 3))
