# LRU 알고리즘 구현 (Least Recently Used)
# 최근 가장 오랫동안 참조되지 않은 페이지 교체
def solution(cacheSize, cities):
    answer = 0
    cities = [i.lower() for i in cities]
    cache = []

    if cacheSize == 0: #사이즈가 0일 때, miss(5) 곱한 값 리턴
        return len(cities)*5
    else:
        for city in cities:
            if city in cache: #cache에 있을 때, 기존 값 삭제 후 맨 뒤에 다시 추가 = hit
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                if len(cache) >= cacheSize: #cache에 없을 때, 맨 앞의 값 삭제 후 새로운 값 맨 뒤에 추가 = miss
                    cache.pop(0)
                cache.append(city)
                answer += 5

    return answer