"""
Given current directory and change directory path, return final path.

For Example:

Current               Change              Output
/                     /facebook           /facebook
/facebook/anin        ../abc/def          /facebook/abc/def
/facebook/instagram   ../../../../.       /
"""

def change_directory(current_dir: str, change_dir_path: str) -> str:
    """Takes in a current directory and change directory path and returns final path"""
    if not change_dir_path:
        return current_dir
    if change_dir_path[0] == "/":
        return change_dir_path
    
    paths = []

    aggregate_path_list = f"{current_dir}/{change_dir_path}".split("/")

    for segment in aggregate_path_list:
        if segment == "..":
            if len(paths) > 0:
                paths.pop()
        elif segment and segment != ".":
            paths.append(segment)

    final_path = "/" + "/".join(paths)

    return final_path