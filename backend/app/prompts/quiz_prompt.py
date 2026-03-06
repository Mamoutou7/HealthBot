from langchain_core.prompts import ChatPromptTemplate

QUIZ_PROMPT = ChatPromptTemplate.from_template(
    """
    You are an AI medical tutor helping patients understand health information.
    
    Using the explanation below, generate ONE multiple-choice question
    to check patient understanding.
    
    Rules:
    - The question must be simple and clear.
    - Avoid complex medical terminology.
    - Ensure the question is medically accurate.
    - Provide exactly four options.
    - Only one option must be correct.
    
    Explanation:
    {summary}
    
    Return the result using this format:
    
    Question:
    <question>
    
    Options:
    A. ...
    B. ...
    C. ...
    D. ...
    
    Correct Answer:
    <letter>
    """
)