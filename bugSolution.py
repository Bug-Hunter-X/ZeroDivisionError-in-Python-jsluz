def function_with_error_handling(a, b):
    try:
        if a == 0:
            return 1 / a
        else:
            return a + b
    except ZeroDivisionError:
        return float('inf')  # Or another appropriate handling
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None