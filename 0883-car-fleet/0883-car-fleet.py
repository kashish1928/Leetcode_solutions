class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort(key = lambda x: (x[0],x[1]),reverse = True)
        left = [(lambda x: (target*1.0 - x[0])/x[1])(car) for car in cars]
        stack = []
        print(left)
        for i in left:
            if not stack:
                stack.append(i)
            if i > stack[-1]:
                stack.append(i)
        return len(stack)