"""
연애 상담 에이전트 도구
"""
from langchain_core.tools import tool
from model1 import UserProfile, Question, Solution
from mock_db1 import get_store

def couple_metrics(
        age : int,
        gender: str,
        mbti: str,
        age_gap: int
) -> UserProfile:
    """"상대방 정보를 저장하고 프로필을 반환합니다.
    
    Args:
        age : 나이
        gender : 성별 ("male | female")
        mbti : MPTI
        age_gap : 나이 차이

    Returns:
        UserProfile : 상대방 정보 모델
    """
    profile = UserProfile(
        age=age,
        gender=gender,
        mbti=mbti,
        age_gap=age_gap
    )
    store1 = get_store()
    store1["profile"].append(profile)

    return profile

@tool
def save_question(
    question_type: str,
    target_relation: str
) -> Question:
    """모델이 설계한 목표 해결 방식을 저장합니다.
    
    Args:
        question_type: 사용자가 설정한 연애 걱정 유형(예: 짝사랑, 사랑 싸움)
        target_relation: 사용자가 원하는 관계 해결 방식(예: 연락 빈도 늘리기, 고백, 충분한 대화 시간 갖기)

    Returns:
        Question: 사용자의 고민
    """

    question = Question(
        question_type=question_type,
        target_relatation=target_relation
    )

    store=get_store()
    store["question"].append(question)

    return question

@tool
def save_solution(solution_type: str, solution_content: str) -> Solution:
    """모델이 생성한 솔루션을 저장합니다.
    
    Args:
        solution_type: 저장할 솔루션의 유형
        solution_content: 저장할 솔루션의 내용

    Returns:
        Solution: 저장된 솔루션 정보
    """

    solution = Solution(
        solution_type=solution_type,
        solution_content=solution_content
    )

    store = get_store()
    store["save_solution"].append(solution)

    return solution

@tool
def get_user_info() -> str:
    """저장된 사용자의 프로필, 솔루션을 한번에 조회합니다.
    모델이 맞춤형 계획을 수립하기 이전에 호출하여 사용자의 현황을 파악합니다.

    Returns:
        사용자의 프로필 및 솔루션 정보
    """

    store = get_store()

    profile = store.get("profile", [])
    question = store.get("question", [])
    solution = store.get("solution", [])

    if not profile:
        return "등록된 사용자 정보가 없습니다. 사용자에게 정보를 먼저 등록하라고 하세요."
    
    result = f"""
    사용자 정보
    - 나이: {profile[-1].age}
    - 성별: {profile[-1].gender}
    - MBTI: {profile[-1].mbti}
    - 나이 차이:{profile[-1].age_gap}
    """

    if question:
        question = question[-1]
        result += f"""
        최근 질문
        - 고민 유형: {question.question_type}
        - 목표 관계: {question.target_relation}"""

    if solution:
        solution = list(solution.key())
        result += f"""
        최근 솔루션:
        - 솔루션 유형: {', '.join(solution)}
        """

    return result