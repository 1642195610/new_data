from randomList import randomList
import copy


def count_sort(list_list):
    dic = {}
    nums = []
    result1 = []
    for i in range(len(list_list)):
        if list_list[i] not in nums:
            nums.append(list_list[i])
        if list_list[i] not in dic:
            dic[list_list[i]] = 1
        else:
            dic[list_list[i]] += 1
    print(dic)
    print(f"去重后: {nums}")
    nums_copy = copy.deepcopy(nums)
    for i in range(len(nums)):
        m = min(nums_copy)
        for j in range(dic[m]):
            m = min(nums_copy)
            result1.append(m)
        nums_copy.remove(m)
    return result1


if __name__ == '__main__':
    list1 = randomList.randomList(10)
    # list = [9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9 ,7,9]
    result = count_sort(list1)
    print(f"未排序: {list1}")
    print(f"排序后: {result}")
