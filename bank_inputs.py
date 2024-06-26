def get_user_input():
    name = input("Enter your name: ")
    savings_amount = float(input("Enter your savings account amount: "))
    monthly_earnings = float(input("Enter your monthly earnings: "))
    
    needs = []
    wants = []
    
    num_needs = int(input("Enter the number of needs: "))
    for i in range(num_needs):
        need = input(f"Enter need # {i+1}: ")
        needs.append(need)
        
    num_wants = int(input("Enter the number of wants: "))
    for i in range(num_wants):
        want = input(f"Enter want # {i+1}: ")
        wants.append(want)
    
    return {
        "name": name,
        "savings_amount": savings_amount,
        "monthly_earnings": monthly_earnings,
        "needs": needs,
        "wants": wants
    }
