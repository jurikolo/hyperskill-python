# def print_book_info(title, author=None, year=None):
#     result = f'"{title}"'
#     if (author is not None) and (year is not None):
#         result += f" was written by {author} in {year}"
#     elif author is not None:
#         result += f" was written by {author}"
#     elif year is not None:
#         result += f" was written in {year}"
#     print(result)

def find_my_list(all_lists, my_list):
    for index, lst in enumerate(all_lists):
        # Change the next line
        if all_lists[index] is my_list:
            return index


all = [[1, 2, 3], [1, 2], [2, 3]]
my = all[0]
print(find_my_list(all, my))
