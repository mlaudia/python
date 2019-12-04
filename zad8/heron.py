from math import sqrt

def is_triangle(a, b, c):
    if((a+b) > c and (b+c) > a and (a+c) > b):
        return True

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if(not is_triangle(a, b, c)):
        raise ValueError("Nie spełnia warunku trójkąta")
    s = sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))/4
    print(s)


print(heron(2, 3, 4))