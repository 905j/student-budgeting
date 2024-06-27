import openai
import bank_inputs
import os

openai.api_key = os.getenv('OPENAI_KEY')

def get_budget_advice(student_info):
    name = student_info["name"]
    monthly_earnings = student_info["monthly_earnings"]
    needs = student_info["needs"]
    wants = student_info["wants"]
    
    system_instruction = """
    You are a college student financial advisor and I will give you a student's NAME, their monthly EARNINGS, 
    a list of their NEEDS, and WANTS. You are to give me, in json (integers for the amounts), how much of their monthly earnings should go to savings, 
    each of their needs, each of their wants, and one sentence of constructive feedback to better their spending habits. 
    The priority should be needs, savings, and then wants. Make sure wants do not exceed 20% of the student's earnings. Consider the amount in the
    student's savings account to inform your advivce and whether they have more freedom to spend. Consider the real-world average costs 
    in the United States for the given wants and needs and generate the budget accordingly. Ensure that 
    monthly earnings = savings + need1 + need2 + want1 + want2 + etc...
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

#student_info = bank_inputs.get_user_input()
#budget_advice = get_budget_advice(student_info)
#print(budget_advice)
