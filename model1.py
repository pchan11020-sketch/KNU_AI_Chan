"""
연애 상담 에이전트의 데이터 모델
"""

from pydantic import BaseModel, Field

#from enum import Enum

class UserProfile(BaseModel):
    age : int = Field(description="사용자의 나이")
    gender : str = Field(description="사용자의 성별")
    mbti : str = Field(description="사용자의 MBTI")
    age_gap : int = Field(description="사용자와의 나이 차이")

class Question(BaseModel):
    question_type : str = Field(description="사용자가 설정한 연애 걱정 유형 (예: 짝사랑, 사랑 싸움)")
    target_relation : str = Field(description="사용자가 원하는 관계 해결 방식(예: 연락 빈도 늘리기, 고백, 충분한 대화 시간 갖기)")

class Solution(BaseModel):
    solution_type : str = Field(description="솔루션의 유형")
    solution_content : str = Field(description="솔루션의 구체적인 내용")