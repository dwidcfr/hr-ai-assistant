import requests
from config import API_URL, HEADERS, MODEL


def match_resume(resume_text: str, job_description: str) -> str:
    system_prompt = "Ты — эксперт по подбору персонала. Оцени, насколько кандидат подходит под вакансию."
    user_prompt = f"""
Оцени соответствие по следующим критериям:
1. Процент соответствия (0–100%)
2. Совпадения
3. Несоответствия
4. Советы по улучшению резюме
5. Финальный вывод — подходит или нет

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
        "temperature": 0.4,
        "max_tokens": 1024,
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Groq API Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    with open("../data/job.txt", "r", encoding="utf-8") as f:
        job_desc = f.read()
    with open("../data/resume.txt", "r", encoding="utf-8") as f:
        resume = f.read()

    print("🔍 Анализ соответствия резюме...")
    result = match_resume(resume, job_desc)
    print("\n📄 Результат:\n")
    print(result)
