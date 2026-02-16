class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        if(len(set(bulbs)) == 1):
            if(len(bulbs) % 2 == 0):
                return []
            else:
                return [bulbs[0]]
        on_bulbs = set()
        for i in bulbs:
            if(i not in on_bulbs):
                on_bulbs.add(i)
            else:
                on_bulbs.remove(i)
        return sorted(list(on_bulbs))