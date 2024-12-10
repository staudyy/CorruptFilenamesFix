# CorruptFilenamesFix
Fix corrupted filenames with the help of another directory containing files with correct names

## Possible usecase:
You copied music files from Android to Windows, made a lot of changes and edits and realised the filenames are wrong. You copy them again now correctly and want to batch rename the edited files

## Requirements
A directory full of files that had ASCII characters used in filenames and their filenames have corrupted due to wrong encoding being used (for example extracting an archive made on linux badly on windows) and you need to rename them back to the original
A directory with files that have the same names but encoded properly
For example:
- Correct filename:   My_file_Abčďé_👍
- Corrupted filename: My_file_AbÄÄÃ©_ðŸ‘
WARNING: Works only on filenames that contain some normal non special characters as well (characters that didn't change even after the corruption) - Default is 7 including the file extension - You can change this value but the results may be less accurate

## Usage
1. Clone the repo
2. Run the file "fix_names.py" in terminal with 2 arguments
   The paths have to lead to a folder that contains ONLY files and NO OTHER folders
```
python fix_names.py <PATH_TO_CORRUPTED_FILES> <PATH_TO_CORRECT_FILES>
```

##
Optionally you can change the minimum non special character limit for the script to rename a file
```
python fix_names.py <PATH_TO_CORRUPTED_FILES> <PATH_TO_CORRECT_FILES> -m <NUMBER_OF_CHARACTERS>
```
