import openai
import bank_inputs

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_budget_advice(student_info):
    name = student_info["name"]
    monthly_earnings = student_info["monthly_earnings"]
    needs = student_info["needs"]
    wants = student_info["wants"]
    
    system_instruction = """
    You are a college student financial advisor and I will give you a student's NAME, their monthly EARNINGS, 
    a list of their NEEDS, and WANTS. You are to give me, in json (integers for the amounts), how much of their monthly earnings should go to savings, 
    each of their needs, each of their wants, and one sentence of constructive feedback to better their spending habits. 
    The priority should be needs, savings, and then wants. Make sure wants do not exceed 10% of the student's earnings feel free to give 0 to wants 
    if the student does not make. Consider the real-world average costs in the United States for the given wants and need and generate the budget accordingly.
    The format of the json should be
    {
    "savings": integer,
    "need1": integer,
    "need2": integer,
    "want1": integer,
    "want2": integer,
    "feedback": string
    }
    """

    needs_str = ", ".join(needs)
    wants_str = ", ".join(wants)

    user_instruction = f"""
    Name: {name}
    Monthly Earnings: {monthly_earnings}
    Needs: {needs_str}
    Wants: {wants_str}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_instruction}
        ]
    )
    
    return response.choices[0].message['content']
