# Pytherife Teen Code Reply Challenge

import sys
MOD = 100003

# Analizar los datos del input 
def parse_testcases(io):
    # Leer el número de casos
    T = int(io.readline())
    tc = []

    # Para cada test case
    for _ in range(T):
        # Leer los datos del input
        
        x,y = map(int, io.readline().strip().split())
        s,w = map(int, io.readline().strip().split())
        n = int(io.readline())
        p = []
        out = []
       
        for i in range(0,n):
            a = list(map(int, io.readline().strip().split())) # x_in y_in x_out y_out
            p.append(a[0])
            out.append(a[2])
          
        # Añadir a la lista de casos
        tc.append((x,s,n,p,out))

    # Retornar todos los casos analizados
    return tc

# Función para resolver un caso
def solve_testcase(t):
    # Obtener los datos del caso
    (x,s,n,p,out) = t
    cnt = 0
    a = s
    b = 0
    while len(p) > 0:
        minimum = get_min(s,n,p)
        a = p[minimum]
        b = minimum
        cnt += abs(s-a)
        s = out[b]
        del p[b]
        del out[b]
       
    return cnt%MOD
    
def get_min(s, n, p):
    a = s
    if len(p) == 1:
        return 0
        
    for i in range(0,len(p)):
        if abs(s-p[i] < a):
            a = i

    return a

# Resolución 
def solve(input, output):
    # Enumerar todos los casos
    for i, t in enumerate(parse_testcases(input)):
        # Imprimir la solución del caso
        print(f"Case #{i+1}:", solve_testcase(t), file=output)
        
if __name__ == "__main__":
    fin = open(r'C:\Users\Andrey\Documents\python_projects\demos\Competitive programming\Code Reply\input.txt', "r")
    fout = open(r"C:\Users\Andrey\Documents\python_projects\demos\Competitive programming\Code Reply\output.txt", "w")
    solve(fin, fout)