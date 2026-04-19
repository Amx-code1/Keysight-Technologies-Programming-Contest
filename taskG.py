mod = 998244353

n, state, m, f = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

mask = (1 << 31) - 1
p = [-1] * n
for i in range(2, n+1):
    if i <= m:
        p[i-1] = q[i-2]-1
    else:
        p[i-1] = state % (i-1)
        state = (state * 1103515245 + 12345) & mask
c = [-1] * n
for i in range(1, n+1):
    if i <= m:
        c[i-1] = d[i-1]-1
    else:
        c[i-1] = state % f
        state = (state * 1103515245 + 12345) & mask

e = [[] for i in range(n)]
for i in range(1, n):
    e[p[i]].append(i)

s = [1] * n
heavy = [-1] * n
for i in reversed(range(1, n)):
    pi = p[i]
    s[pi] += s[i]
    if heavy[pi] == -1 or s[i] > s[heavy[pi]]:
        heavy[pi] = i 

in_t, out_t, vs = [0] * n, [0] * n, [0] * n
ti = 0
st = [0]
while st:
    u = st.pop()
    if u >= 0:
        vs[ti] = u
        in_t[u] = ti
        ti += 1
        for v in e[u]:
            st.append(~v)
            st.append(v) 
    else:
        out_t[~u] = ti

cnt = [0] * n
freq = [0] * (n + 1)
ma_fr = 0
ans = 0

st = [(~0, 1), (0, 1)]
while st:
    u, f = st.pop()
    if u >= 0:
        if heavy[u] != -1:
            st.append((~heavy[u], 1))
            st.append((heavy[u], 1))
        for v in e[u]:
            if v != heavy[u]:
                st.append((~v, 0))
                st.append((v, 0))
    else:
        u = ~u
        cu = c[u]
        fu = cnt[cu]
        freq[fu] -= 1
        cnt[cu] = fu+1
        freq[fu+1] += 1
        if fu+1 > ma_fr:
            ma_fr = fu+1
            
        for v in e[u]:
            if v != heavy[u]:
                for i in range(in_t[v], out_t[v]):
                    w = vs[i]
                    cw = c[w]
                    fw = cnt[cw]
                    freq[fw] -= 1
                    cnt[cw] = fw+1
                    freq[fw+1] += 1
                    if fw+1 > ma_fr:
                        ma_fr = fw+1
        ans = (ans + (freq[ma_fr]^(u+1)) * (ma_fr^(u+1))) % mod
        
        if not f:
            for i in range(in_t[u], out_t[u]):
                w = vs[i]
                cw = c[w]
                fw = cnt[cw]
                freq[fw] -= 1
                cnt[cw] = fw-1
                freq[fw-1] += 1
                if fw == ma_fr and freq[fw] == 0:
                    ma_fr = fw-1

print(ans)