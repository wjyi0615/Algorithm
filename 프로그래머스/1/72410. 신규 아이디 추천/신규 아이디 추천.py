import re

def solution(new_id):
    # 1단계: 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계: 허용된 문자 외 모두 제거
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    
    # 3단계: 연속된 마침표(.)를 하나로 치환
    new_id = re.sub(r'\.+', '.', new_id)
    
    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id = new_id.strip('.')
    
    # 5단계: 빈 문자열이면 "a"를 대입
    if new_id == '':
        new_id = 'a'
    
    # 6단계: 길이가 16자 이상이면 첫 15개의 문자를 제외한 나머지 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    
    # 7단계: 길이가 2자 이하라면 마지막 문자를 길이 3이 될 때까지 반복
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
