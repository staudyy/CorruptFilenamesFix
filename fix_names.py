import argparse
import renamer_lib

def run(problem_dir, correct_dir, min_len):
    if min_len:
        renamer_lib.fix_names(problem_dir, correct_dir, min_len)
    else:
        renamer_lib.fix_names(problem_dir, correct_dir)
    renamer_lib.check_names(problem_dir, correct_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script that fixes corrupted filenames from similarities to not corrupted filenames"
    )
    parser.add_argument("corrupt", metavar="path_corrupted", type=str, help="The path to the folder containing files with corrupted filenames")
    parser.add_argument("correct", metavar="path_correct", type=str, help="The path to the folder containing files with correct filenames")

    parser.add_argument("-m", "--match", metavar="N", type=int, help="The number of characters that have to be identical including the file extension (default is 7)")
    args = parser.parse_args()

    run(args.corrupt, args.correct, args.match)