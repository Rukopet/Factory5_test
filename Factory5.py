import random
from typing import List, Union

# list in second param because when K == 0 we need returned empty list
AnswerList = List[int]


def choices_with_weight(choice_list: List[int], k: int, weight_list: List[float]) -> AnswerList:
    # I prefer use random() but according to the condition of the problem, we can only use randint()

    answer, first_index_for_randint, len_choice_list = [], 0, len(choice_list)
    for _ in range(k):
        probability = rand_index = -1
        while not random.randint(0, 100) <= probability * 100:
            rand_index = random.randint(first_index_for_randint, len_choice_list - 1)
            probability = weight_list[rand_index]
        answer.append(choice_list[rand_index])
        choice_list.insert(0, choice_list.pop(rand_index))
        weight_list.insert(0, weight_list.pop(rand_index))
        first_index_for_randint += 1
    return answer


def wrapper_for_cycle(cp_choice_list: List[int], len_choice_list: int, first_index_for_randint: int) -> int:
    rand_index = random.randint(first_index_for_randint, len_choice_list)
    answer = cp_choice_list[rand_index]
    # Move this random element which we take for answer in 0 index, because we can`t take it more
    cp_choice_list.insert(0, cp_choice_list.pop(rand_index))
    # Increment our variable for randint. So as not to take element one more time
    first_index_for_randint += 1
    return answer


def my_choices(choice_list: List[int], k: int, weight_list: List[float] = None) -> AnswerList:
    """
    choices function without weight_list -> algorithm complex O(k)
    choices function with weight_list -> algorithm complex O(10k)
    does not change data


    :param choice_list: data for randomize elements ex -> [1, 3, 4, 3, 3, 9]
    :param k: len returned list -> 3
    :param weight_list: list of weights ex -> [.7, .4, .5, .9, .1, .2] or None
    :return: list of random elements. ex -> [3, 1, 4]
    :raises ValueError: raise if K > len(choice_list)
    """

    # I copy the input data so as not to change them if it is important
    cp_choice_list = choice_list.copy()
    len_choice_list = len(cp_choice_list)
    if k == len_choice_list:
        return cp_choice_list
    elif k > len_choice_list:
        raise ValueError("k bigger than length choice list")
    elif k == 0:
        return []
    if weight_list is not None:
        return choices_with_weight(cp_choice_list, k, weight_list.copy())

    # first cycle variant readable but slow ----------------------------------------------------------------------------
    answer, first_index_for_randint = [], 0
    for _ in range(k):
        rand_index = random.randint(first_index_for_randint, len_choice_list - 1)
        answer.append(cp_choice_list[rand_index])
        # Move this random element which we take for answer in 0 index, because we can`t take it more
        cp_choice_list.insert(0, cp_choice_list.pop(rand_index))
        # Increment our variable for randint. So as not to take element one more time
        first_index_for_randint += 1
    # ------------------------------------------------------------------------------------------------------------------

    # second cycle variant faster but not readable, I prefer first variant ---------------------------------------------
    """
    first_index_for_randint = 0
    return [
        wrapper_for_cycle(cp_choice_list, len_choice_list, first_index_for_randint)
        for _ in range(k)
    ]
    """
    # ------------------------------------------------------------------------------------------------------------------
    return answer


if __name__ == "__main__":
    print(my_choices([1, 3, 4, 3, 3, 9], 4, [.7, .4, .5, .9, .1, .2]))
