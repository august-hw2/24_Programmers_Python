from collections import deque

# 다리에 올라갈 수 있는 트럭 수, 견딜 수 있는 다리 무게, 트럭별 무게
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length) # 다리
    truck_weights = deque(truck_weights)

    total_weight = 0 # 다리에 올라가있는 트럭 무게

    while len(truck_weights) > 0:

        time += 1
        total_weight -= bridge.popleft()

        if total_weight + truck_weights[0] <= weight:
            total_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else: # 넘으면 0 삽입
            bridge.append(0)

    return time + bridge_length