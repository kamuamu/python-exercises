class DictionaryWithFrequency:
    def dic_with_freq(self, sent):
        empty_dict = {}
        words = sent.lower().split()
        for word in words:
            if word in empty_dict:
                empty_dict[word] += 1
            else:
                empty_dict[word] = 1
        print(empty_dict)

def main():
    df = DictionaryWithFrequency()
    df.dic_with_freq("hello world hello world hello india")

if __name__ == '__main__':
    main()

