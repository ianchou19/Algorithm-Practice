import copy


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # [Line Sweep]
        if not A or not B:
            return []

        sweepLine = []

        for start, end in A:
            sweepLine.append((start, 1))
            sweepLine.append((end, -1))

        for start, end in B:
            sweepLine.append((start, 1))
            sweepLine.append((end, -1))

        sweepLine.sort()
        count = 0
        result = []
        tmp = []

        for idx, (pos, val) in enumerate(sweepLine):
            count += val
            # print count

            if count == 2:
                tmp = [pos, None]

            if count == 1 and tmp:
                tmp[1] = pos
                result.append(copy.deepcopy(tmp))
                tmp = []

            # 遇到一個 interval 的開始點等於另個 interval 的結束點時
            if idx > 0 and sweepLine[idx][0] == sweepLine[idx - 1][0] and sweepLine[idx][1] != sweepLine[idx - 1][1]:
                result.append([sweepLine[idx - 1][0], sweepLine[idx][0]])

        return result
