from randomList import randomList
import copy


def countsort(list):
    dic = {}
    nums = []
    result = []
    for i in range(len(list)):
        if list[i] not in nums:
            nums.append(list[i])
        if list[i] not in dic:
            dic[list[i]] = 1
        else:
            dic[list[i]] += 1
    print(dic)
    print(f"去重后: {nums}")
    nums_copy = copy.deepcopy(nums)
    for i in range(len(nums)):
        m = min(nums_copy)
        for j in range(dic[m]):
            m = min(nums_copy)
            result.append(m)
        nums_copy.remove(m)
    return result


if __name__ == '__main__':
    list = randomList.randomList(10)
    # list = [9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9 ,7,9]
    result = countsort(list)
    print(f"未排序: {list}")
    print(f"排序后: {result}")
