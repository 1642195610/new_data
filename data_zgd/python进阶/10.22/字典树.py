class TireNode:
    def __init__(self):
        self.data = {}
        self.is_world = False

    def __repr__(self):
        return f"{str(self.data)}"


class Tire:
    def __init__(self):
        self.root = TireNode()

    def insert(self, world):
        node = self.root
        for char in world:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TireNode()
            node = node.data[char]
        node.is_world = True

    def search(self, world): #查找单词是否存在
        node = self.root
        for char in world:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_world

    def prefix(self, prefix): # 查找公共前缀是否存在
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if not node:
                return False
        return True

if __name__ == '__main__':
    t = Tire()
    t.insert('something')
    t.insert('somewhere')
    print(t.root.data)
    world = "something"
    world2 = "somethings"
    print(f"要查找的单词: {world}, 是否存在 {t.search(world)}")
    print(f"要查找的单词: {world2}, 是否存在 {t.search(world2)}")
    prefix = 'so'
    prefix2 = 'sos'
    print(f"要查找的公共前缀: {prefix}, 是否存在 {t.prefix(prefix)}")
    print(f"要查找的公共前缀: {prefix2}, 是否存在 {t.prefix(prefix2)}")
