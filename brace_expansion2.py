class Solution(object):
    def braceExpansionII(self,expression):
        stack = [[{""}]]
        i, n = 0, len(expression)

        while i < n:
            c = expression[i]
            if c == '{':
                stack.append([{""}])
                i += 1
            elif c == '}':
                top = stack.pop()
                union_set = set()
                for g in top:
                    union_set |= g
                last_group = stack[-1].pop()
                stack[-1].append({a + b for a in last_group for b in union_set})
                i += 1
            elif c == ',':
                stack[-1].append({""})
                i += 1
            else:
                j = i
                while j < n and expression[j].isalpha():
                    j += 1
                word = expression[i:j]
                last_group = stack[-1].pop()
                stack[-1].append({a + word for a in last_group})
                i = j

        top = stack.pop()
        result = set()
        for g in top:
            result |= g
        return sorted(result)
