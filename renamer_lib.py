import os
from difflib import SequenceMatcher
import shutil

def _is_basic(letter):
    #97-122  -> a-z
    #65 - 90  -> A-Z
    #48 - 57  -> 0-9
    #32  -> SPACE  -> higher
    val = ord(letter)
    if 97 <= val <= 122 or 65 <= val <= 90 or 48 <= val <= 57 or val == 32:
        return True
    return False

def _get_stripped_str(word):
    stripped_str = ''
    for l in word:
        if _is_basic(l):
            stripped_str += l

    return stripped_str

# USABLE
def fix_names(problem_dir, correct_dir, needed_length=7, needed_percentage=0.9):
    problem_list = os.listdir(problem_dir)
    correct_list = os.listdir(correct_dir)

    for problem_name in problem_list:
        bad_stripped_str = _get_stripped_str(problem_name)

        for correct_name in correct_list:
            correct_stripped_str = _get_stripped_str(correct_name)

            similarity = SequenceMatcher(None, bad_stripped_str, correct_stripped_str).ratio()
            if similarity > needed_percentage and len(bad_stripped_str) > needed_length:
                os.rename(problem_dir + "/" + problem_name, problem_dir + "/" + correct_name)
                break

# USABLE
def check_names(problem_dir, correct_dir):
    names_to_check = os.listdir(problem_dir)
    name_list = os.listdir(correct_dir)

    for i in range(len(names_to_check)):
        if names_to_check[i] in name_list:
            names_to_check[i] = None
    
    unfixed = []
    for name in names_to_check:
        if name:
            unfixed.append(name)
    
    if unfixed:
        print("---------------")
        print("|UNFIXED NAMES|")
        print("---------------")
        for name in unfixed:
            print(name)
        print("---------------")
    else:
        print("---------------")
        print("|---SUCCESS---|")
        print("---------------")


def _get_last_dir(path):
    name = ""
    for l in path[::-1]:
        if l != "/":
            name += l
        else:
            break
    return name[::-1]

# USABLE
def sort_into_dir(to_sort, destinations, new_folder_dir):
    for destination in destinations:
        try:
            os.mkdir(new_folder_dir + "/" + _get_last_dir(destination[1]))
        except:
            pass

    for name in to_sort[0]:
        for destination in destinations:
            if name in destination[0]:
                shutil.copy(to_sort[1] + "/" + name, new_folder_dir + "/" + _get_last_dir(destination[1]))
