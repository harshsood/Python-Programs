alpha_dict = {"g": 14, "q": 16, "h": 19}

new_value = max(alpha_dict, key=alpha_dict.get)
print("Highest value from dictionary:",new_value)
