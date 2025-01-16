import re


def solution(new_id):
    answer = ''
    # 대문자를 소문자로 변경
    new_id = new_id.lower()
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub('[^a-z0-9\-_.]', "", new_id)
    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    # 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id= new_id.strip('.')
    # 빈 문자열이라면, new_id에 "a"를 대입
    if not new_id:
        new_id += 'a'
    # new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id.rstrip('.')
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙
    if len(new_id) < 3:
        new_id += new_id[-1] * (3 - len(new_id))

    return new_id
