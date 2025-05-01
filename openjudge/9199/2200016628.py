from collections import deque

def count_dict_lookups(M, N, words):
    memory = set()
    queue = deque()
    lookup_count = 0

    for word in words:
        if word in memory:
            continue 
        else:
            lookup_count += 1 
            if len(memory) >= M:
                old_word = queue.popleft()
                memory.remove(old_word)
            # 添加新单词
            memory.add(word)
            queue.append(word)

    return lookup_count


if __name__ == "__main__":
    M, N = map(int, input().split())
    words = list(map(int, input().split()))
    print(count_dict_lookups(M, N, words))