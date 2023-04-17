# python3

def read_input():
    input_type = input().rstrip()

    pattern = input().rstrip()
    text = input().rstrip()

    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    
    
    p = 1000000007
    x = 263
    
    m = len(pattern)
    n = len(text)
    h_pattern = sum([ord(pattern[i]) * pow(x, i, p) for i in range(m)]) % p
    h_text = sum([ord(text[i]) * pow(x, i, p) for i in range(m)]) % p
    
    occurrences = []
    
    for i in range(n - m + 1):
        if h_pattern == h_text:
            if pattern == text[i:i+m]:
                occurrences.append(i)
        
        if i < n - m:
            h_text = ((h_text - ord(text[i]) * pow(x, m-1, p)) * x + ord(text[i+m])) % p
    
    return occurrences



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
