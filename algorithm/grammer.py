
def get_diff_between_list(listA: list, listB: list) -> set:
    """2つのリストの差分を返す。
    
    
    """
    diff_set: set = set(listA) ^ set(listB)
    return diff_set
    
    
    