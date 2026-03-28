from agent1 import get_solution_agent

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model = "openai/gpt-oss-20b"
)

solution_agent = get_solution_agent(model)

result = solution_agent.invoke({
    "messages" : [
        {
            "role": "user",
            "content": "현재 연애 중이지는 않지만 해당 시점 전 여자친구가 23살이고 저랑 동갑이었습니다. 서로 멀리 떨어져야 하는 상황이 생겼는데, 바로 직전에 다툼을 하였습니다. 다툼 내용은 친구들과 장난으로 했던 내용을 전 여자친구가 보고 제가 한 짓이 아님에도 헤어지게 되었습니다."
        }
    ]
})


print(result)
print(result['messages'][-1].content)