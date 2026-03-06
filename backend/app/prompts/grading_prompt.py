from langchain_core.prompts import ChatPromptTemplate

GRADING_PROMPT = ChatPromptTemplate.from_template(
    """
    You are a medical education assistant.
    
    Evaluate the patient's answer using the summary below.
    
    Summary:
    {summary}
    
    Question:
    {question}
    
    Patient answer:
    {answer}
    
    Tasks:
    1. Determine if the answer is correct.
    2. Explain why.
    3. Quote the relevant sentence from the summary that supports your explanation.
    
    Return:
    
    Grade: Correct / Incorrect
    
    Explanation:
    ...
    
    Citation:
    "..."
    """
)