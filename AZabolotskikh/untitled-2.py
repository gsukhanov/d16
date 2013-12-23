m=[0,1];
i = 2;
while len(m)<102: #i>=0, a_{i+2} = a_{i+1} + 2 a_{i}.
    n = m[i-1] + 2*(m[i-2]);
    m.append(n);
    i += 1;
print (m[100]);
print (m[101]/m[100]);
