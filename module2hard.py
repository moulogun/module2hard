final_result = []
n = int(input('Enter the number: '))
for i in range(1,20):
    for m in range(1,20):
        if m > i:
            if i == m:
                continue
            else:
                kratnost = n % (i + m)
                if kratnost == 0:
                    final_result.append(i)
                    final_result.append(m)
                else:
                    continue
        else:
            continue
print(*final_result, sep='')