try:
    a=100/50
    b=20/0
except ZeroDivisionError:
    print("ZeroDivisionError")

except ArithmeticError:
    print("Arithmetic Error ")

else:
    print("Success ! else block ")

finally:
    print("always will be excecuted final block")
