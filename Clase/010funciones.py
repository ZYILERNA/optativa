def my_function():
    print("Hola, mundo!")

my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(1.4,5.2)
sum_two_values("5", "7")

def sum_two_values_and_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_and_return(10, 5)
print(my_result)

my_result = sum_two_values_and_return("10", 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Yang", name="Zhen")

def print_upper_text(text):
    print(text.upper())

print_upper_text("Hola, mundo!")