import turtle as t


t.color('green')
for i in range(-200, 200, 40):
    t.goto(i, -200)
    t.dot(10, 'blue')
    t.goto(0, 0)