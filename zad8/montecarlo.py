import random

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    circle_points = 0
    square_points = 0
    interval = 0
    while(interval < n):
        x = random.random()
        y = random.random()
        d = x*x + y*y
        if(d <= 1):
            circle_points += 1
        square_points += 1
        interval += 1
    
    pi = 4 * (circle_points / square_points)
    print(pi)


n = 100
while n <= 1000000:
    print('Intervals: ', n)
    calc_pi(n)
    n *= 10
