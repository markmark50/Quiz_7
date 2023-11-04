현재_트리_높이 = int(input("크리스마스 트리의 높이를 설정하세요:"))
for 높이 in range(1, 현재_트리_높이 + 1):
    for 공백 in range(현재_트리_높이 - 높이):
        print(" ", end="")
    for 별 in range(2 * 높이 - 1):
        print("*", end="")
    print()
