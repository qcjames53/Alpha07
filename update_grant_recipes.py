RECIPES_PARENT_FOLDER = "a07/data/a07/recipes"
GRANT_RECIPES_FUNCTION = "a07/data/a07/functions/grant_recipes.mcfunction"
REPLACE_FLAG = "# SCRIPT OUTPUT BELOW"

import os

if __name__ == "__main__":
    # Get names
    filenames = next(os.walk(RECIPES_PARENT_FOLDER), (None, None, []))[2]
    filenames.remove('.DS_Store') # Mac OS sucks
    filenames.sort()
    filenames = ['recipe give @s a07:' + string[:-5] + '\n' for string in filenames]
    
    # Append to function file
    with open(GRANT_RECIPES_FUNCTION, "r+") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            flag_index = None
            if REPLACE_FLAG in line:
                flag_index = i
                break
        if flag_index is not None:
            del lines[flag_index + 1:]
            lines.extend(filenames)
            file.seek(0)
            file.writelines(lines)
            print(f"File '{GRANT_RECIPES_FUNCTION}' modified successfully.")
        else:
            print(f"Replace flag '{REPLACE_FLAG}' not found in the file.")
                