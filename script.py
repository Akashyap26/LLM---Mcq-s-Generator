import PyPDF2
import openai


openai.api_key = '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' #this Api key expires on 10-06-2023 please generate a new api key from this link https://platform.openai.com/account/api-keys and paste it here

def mcqs(paragraph, num_questions):
    
    max_paragraph_length = 4096
    if len(paragraph) > max_paragraph_length:
        paragraph = paragraph[:max_paragraph_length]

    
    prompt = f"Generate {num_questions} multiple-choice questions based on the following paragraph which answers at the end:\n\n{paragraph}\n\n---\n\nQuestion:"

    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=256,
        n=num_questions,
        stop=None,
        temperature=0.7,
        top_p=1.0
    )

    #
    choices = response.choices
    questions = [choice.text.strip() for choice in choices]
    answers = [choice.text.strip() for choice in choices]

    
    for i in range(num_questions):
        print(f"Question {i+1}: {questions[i]}")
        print(f"Answer {i+1}: {answers[i]}\n")


def pdftotext(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# List of PDF files to process
pdf_files = ['G:/Proj Curreent/Akaike Tech/NLP assignment/internship-assignment-nlp-main/Dataset/chapter-2.pdf','G:/Proj Curreent/Akaike Tech/NLP assignment/internship-assignment-nlp-main/Dataset/chapter-3.pdf','G:/Proj Curreent/Akaike Tech/NLP assignment/internship-assignment-nlp-main/Dataset/chapter-4.pdf']

# Read text from each PDF file
for file in pdf_files:
    text = pdftotext(file)
    print(text)


mcqs(text,10)