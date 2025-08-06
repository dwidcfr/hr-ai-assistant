import requests
from config import API_URL, HEADERS, MODEL


def improve_resume(resume_text: str, job_description: str) -> str:
    system_prompt = (
        "Ты — опытный карьерный консультант и AI-специалист по составлению резюме."
    )
    user_prompt = f"""
Улучшите данное резюме под следующую вакансию. Сконцентрируйся на ключевых навыках, терминологии и релевантности.
Выведи улучшенное резюме как текст, готовый для использования.
ПРИМЕЧАНИЕ: ТВОЯ ЗАДАЧА МАКСИМАЛЬНО ПРИБЛИЗИТЬ РЕЗЮМЕ К ВАКАНСИИ ИСХОДЯ ИЗ НАВЫКОВ КОТОРЫЕ ОТМЕЧЕННЫ В САМОМ РЕЗЮМЕ. НЕ ДОБАВЛЯЙ ТО ЧЕГО НЕТ!

Вакансия:
{job_description}

Резюме:
{resume_text}
"""

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.5,
        "max_tokens": 1500,
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Groq API Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    with open("../data/resume.txt", "r", encoding="utf-8") as f:
        resume = f.read()
    with open("../data/job.txt", "r", encoding="utf-8") as f:
        job = f.read()

    improved = improve_resume(resume, job)
    print("📄 Улучшенное резюме:\n")
    print(improved)
