import os
def find_file_recursive(suffix, path, output_list=None):
    dir_files = os.listdir(path)
    for filename in dir_files:
        filename = os.path.join(path,filename)
        if os.path.isfile(filename):
            if filename.endswith(suffix):
                output_list.append(filename)
        elif os.path.isdir(filename):
            find_file_recursive(suffix,filename,output_list=output_list)
    return

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    import os
    os.path.isdir()
    os.path.isfile()
    os.lsdir()
    os.path.join()
    """
    returnList = []
    find_file_recursive(suffix, path, returnList)
    return returnList

#print(find_files('py','.'))