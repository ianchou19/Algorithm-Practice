import collections


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # [BFS, Hash Table]
        em_to_name = {}
        graph = collections.defaultdict(set)  # Adjacent table

        for acc in accounts:
            print acc
            name = acc[0]

            for email in acc[1:]:
                # 用每個account的第一個email當作connected component的hub，來連接所有同個帳戶的emails
                graph[acc[1]].add(email)
                graph[email].add(acc[1])  # 兩點相鄰時，彼此都要是彼此的nb
                em_to_name[email] = name

        seen = set()
        ans = []

        for email in graph:
            if email not in seen:
                queue = collections.deque([email])
                seen.add(email)
                component = []

                while queue:
                    node = queue.popleft()
                    component.append(node)

                    for nb in graph[node]:
                        if nb in seen:
                            continue
                        queue.append(nb)
                        seen.add(nb)

                ans.append([em_to_name[email]] + sorted(component))

        return ans
