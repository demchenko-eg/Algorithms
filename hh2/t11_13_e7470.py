def solve():
    n, m = map(int, input().split())
    salaries = list(map(int, input().split()))
    banknotes = list(map(int, input().split()))
    if sum(banknotes) < sum(salaries):
        print("NO")
        return
    salaries.sort(reverse=True)
    banknotes.sort(reverse=True)
    used = [False] * m
    def backtrack(person_index):
        if person_index == n:
            return True
        if sum(banknotes[i] for i in range(m) if not used[i]) < salaries[person_index]:
            return False
        def search_for_person(start, current_sum):
            if current_sum == salaries[person_index]:
                if backtrack(person_index + 1):
                    return True
                return False
            if current_sum > salaries[person_index]:
                return False
            prev = -1
            for j in range(start, m):
                if not used[j] and banknotes[j] != prev:
                    if current_sum + banknotes[j] > salaries[person_index]:
                        prev = banknotes[j]
                        continue
                    used[j] = True
                    if search_for_person(j + 1, current_sum + banknotes[j]):
                        return True
                    used[j] = False
                    prev = banknotes[j]
            return False
        return search_for_person(0, 0)
    print("YES" if backtrack(0) else "NO")

if __name__ == '__main__':
    solve()
