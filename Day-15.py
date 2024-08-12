def marsExploration(s):
    count = 0
    sos = "SOS"
    for i in range(len(s)):
        if s[i] != sos[i % 3]:
            count += 1
    return count
