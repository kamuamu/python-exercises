class RemoveDuplicates:
    def remove_duplicate(self,my_list):
        self.my_list = my_list
        new_list = []
        for num in my_list:
            if num not in new_list:
                new_list.append(num)

        print(new_list)

def main():
    rd = RemoveDuplicates()
    rd.remove_duplicate([1,3,2,2,3])

if __name__ == '__main__':
    main()