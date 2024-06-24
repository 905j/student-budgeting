def get_user_input():
    user_data = {}
    user_data['name'] = input("Enter your name: ")
    user_data['checkings'] = float(input("Enter your checkings amount: "))
    user_data['savings'] = float(input("Enter your savings amount: "))
    user_data['earnings'] = float(input("Enter your monthly earnings: "))
    user_data['needs'] = input("Enter your current needs (separate it with commas): ").split(',')
    user_data['wants'] = input("Enter your current wants (separate it with commas): ").split(',')
    return user_data
