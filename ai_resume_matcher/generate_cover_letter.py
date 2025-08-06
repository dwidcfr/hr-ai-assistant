import requests
from config import GEMINI_API_KEY, GEMINI_URL, GEMINI_HEADERS


def generate_cover_letter(resume: str, job_description: str):
    prompt = f"""
Создай сопроводительное письмо на основе резюме и вакансии.

Требования:
- Деловой стиль
- Акцент на сильные стороны, подходящие под вакансию
- До 300 слов
- Структура: Введение — Основной блок — Заключение

Резюме:
{resume}

Вакансия:
{job_description}
"""

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(
        f"{GEMINI_URL}?key={GEMINI_API_KEY}", headers=GEMINI_HEADERS, json=payload
    )

    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        raise Exception(f"Gemini API error: {response.status_code} {response.text}")


if __name__ == "__main__":
    with open("../data/resume.txt", "r", encoding="utf-8") as f:
        resume = f.read()
    with open("../data/job.txt", "r", encoding="utf-8") as f:
        job = f.read()
    result = generate_cover_letter(resume, job)
    print("📨 Сопроводительное письмо:\n")
    print(result)
