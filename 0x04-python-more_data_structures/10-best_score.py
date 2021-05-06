#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        _max = 0
        for v in a_dictionary.values():
            if _max < v:
                _max = v
        for k in a_dictionary.keys():
            if a_dictionary[k] == _max:
                return(k)
    else:
        return (None)
