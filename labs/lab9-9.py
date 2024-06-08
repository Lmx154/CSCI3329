t = int(input())
k, n, m = [], [], []
s = []

for i in range(t):
    k_i, n_i, m_i = input().split()
    k.append(float(k_i))
    n.append(float(n_i))
    m.append(float(m_i))

for i in range(t):
    s.append(float(k[i] * n[i] - m[i]))
    print(f"{s[i]:.2f}")
