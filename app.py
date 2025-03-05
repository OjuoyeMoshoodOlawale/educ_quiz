import json
from docx import Document

# Re-extracting and structuring the full set of questions and answers
full_questions_data = {
    "course": "EDUC 309: Fundamentals of Counselling",
    "questions": []
}

# Extracting the content from the uploaded document
doc_path = "EDUC 309 2018 CBT DEPARTMENT OF EDUCATIONAL PSYCHOLOGY AND COUNSELLING NEW.docx"

# Parsing the document text to extract questions and answers
doc = Document(doc_path)
content = [p.text for p in doc.paragraphs]

current_question = None
options = []
correct_answer = None

for line in content:
    line = line.strip()
    if line.startswith("^^"):  # Identifies the start of a question
        if current_question:
            full_questions_data["questions"].append({
                "question": current_question,
                "options": options,
                "answer": correct_answer
            })
        current_question = line[2:].strip()
        options = []
        correct_answer = None
    elif line.startswith("@@"):  # Identifies an answer option
        option_text = line[2:].strip().rstrip("~")
        options.append(option_text)
        if line.endswith("~"):  # Correct answer is marked with "~"
            correct_answer = option_text

# Append the last question
if current_question:
    full_questions_data["questions"].append({
        "question": current_question,
        "options": options,
        "answer": correct_answer
    })

# Save the extracted questions into JSON format
json_file_path = "./educ_309_full_questions.json"
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(full_questions_data, json_file, indent=4)

# Provide the file for download
json_file_path
