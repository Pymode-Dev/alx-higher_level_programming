#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as error:
        print(f"Exception: {error}")
        return None
    else:
        return result
