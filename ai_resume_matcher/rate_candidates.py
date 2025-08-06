import requests
import os
from config import API_URL, HEADERS, MODEL


def rate_candidates(resumes: list[str], job_description: str) -> str:
    system_prompt = "Ты — эксперт по подбору персонала. Оценивай и ранжируй список кандидатов по вакансии."

    formatted_resumes = "\n\n".join(
        [f"Кандидат {i + 1}:\n{resume}" for i, resume in enumerate(resumes)]
    )

    user_prompt = f"""
Вакансия:
{job_description}

Резюме:
{formatted_resumes}

Задача:
- Оцени каждого кандидата по соответствию вакансии
- Дай краткий комментарий
- Отсортируй по убыванию пригодности
- Выведи рейтинг в формате:

1. Кандидат X — 87%
Комментарий...

2. Кандидат Y — 75%
Комментарий...

и так далее.
"""

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.3,
        "max_tokens": 1800,
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Groq API Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    resumes_dir = "resumes/"
    job_file = "../data/job.txt"

    if not os.path.exists(job_file):
        print("❌ Файл job.txt не найден.")
        exit()

    resumes = []
    for filename in sorted(os.listdir(resumes_dir)):
        if filename.endswith(".txt"):
            with open(os.path.join(resumes_dir, filename), "r", encoding="utf-8") as f:
                resumes.append(f.read())

    if not resumes:
        print("❌ В папке 'resumes/' нет .txt файлов с резюме.")
        exit()

    with open(job_file, "r", encoding="utf-8") as f:
        job_description = f.read()

    result = rate_candidates(resumes, job_description)
    print("\n🏆 Ранжирование кандидатов:\n")
    print(result)
