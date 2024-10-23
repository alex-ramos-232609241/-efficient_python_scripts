def gen_pyramid(N):
    i = 0
    while i < N + 1:
        value = (N-i)*' ' + (2*(i-1)+1)*'*'
        print(f"{value}")
        i += 1
gen_pyramid(10) 