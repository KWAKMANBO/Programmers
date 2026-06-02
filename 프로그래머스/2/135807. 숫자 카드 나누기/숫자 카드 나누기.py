from math import gcd

def solution(arrayA, arrayB):
    answer = [0]

    # 배열의 최대공약수를 구하는 함수
    def find_gcd(array):
        g = array[0]
        for a in array[1:]:
            g = gcd(g, a)
            if g == 1:  # 중간에 1이 되면 더 볼 필요 없음
                break
        return g

    gcd_a = find_gcd(arrayA)
    gcd_b = find_gcd(arrayB)

    # g로 array의 모든 원소가 나누어떨어지지 않는지 체크하는 함수
    def check(array, g):
        for a in array:
            if a % g == 0:
                return 0
        return g

    # [수정] gcd_a가 1이더라도 check 결과가 0이 되므로 굳이 조건문을 걸지 않아도 됩니다.
    # [수정] 교차해서 array와 gcd를 넣어주어야 합니다.
    answer.append(check(arrayB, gcd_a))
    answer.append(check(arrayA, gcd_b))

    return max(answer)