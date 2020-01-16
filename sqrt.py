def w_sqrt(a):
    if a <= 0:
        print("input must b a positive number")
        return
    start = 0
    end = a
    count = 0
    while ((end - start) > 1e-5):
        if ((end + start) / 2) ** 2 == a:
            return (end + start) / 2
        elif ((end + start) / 2) ** 2 > a:
            end = (end + start) / 2
        else:
            start = (end + start) / 2
        count += 1
        print(count, start, end, (end + start) / 2)
    return (end + start) / 2
def newton_sqrt(a):
    start = 1
    end = a
    count = 0
    while(abs(end - start) > 1e-5):
        count += 1
        start = end
        end = (start + a / start) / 2
        print(count, start, end)
if __name__ == '__main__':
    w_sqrt(11)
    newton_sqrt(11)