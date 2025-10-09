
def is_anagram(s1, s2):
    # Normalize: remove spaces and lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Quick length check
    if len(s1) != len(s2):
        return False

    # Count characters in s1
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
        print(count)

    # Subtract counts using s2
    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    # If dict is empty → all counts matched
    return not count

def main():
    print(is_anagram("cinema", "iceman"))   

if __name__ == '__main__':
    main()