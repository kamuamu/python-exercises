def remove_duplicates(my_list):
    my_set = set()
    for num in my_list:
        my_set.add(num)

    print(my_set)

def main():
    remove_duplicates([1,2,3,1,2])

if __name__ == '__main__':
    main()



