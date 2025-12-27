def sum_numbers(*args):
    return sum(args)

print("Sum Result:", sum_numbers(1, 2, 3))

def display_student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nStudent Info using **kwargs:")
display_student_info(name="Alice", age=30)

def mixed_arguments(*args, **kwargs):
    print("\nPositional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

mixed_arguments(1, 2, 3, name="Alice", age=20)
