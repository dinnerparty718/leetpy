
##


| 查找方式     | 循环条件      | 左侧更新       | 右侧更新        | 中间点位置             | 返回值     |
| ------------ | ------------- | -------------- | --------------- | ---------------------- | ---------- |
| 标准二分查找 | left <= right | left = mid - 1 | right = mid + 1 | (left + right) / 2     | -1 / mid   |
| 二分找左边界 | left < right  | left = mid - 1 | right = mid     | (left + right) / 2     | -1 / left  |
| 二分找右边界 | left < right  | left = mid     | right = mid - 1 | (left + right) / 2 + 1 | -1 / right |


## template 1

- 循环条件：`left <= right`
- 中间位置计算： `mid = left + ((right -left) >> 1)`
- 左边界更新：`left = mid + 1`
- 右边界更新：`right = mid - 1`
- 返回值： `mid / -1`



## template 2 左边界查找1
> 数组有序,但包含重复元素, 
> 数组部分有序,且不包含重复元素
- 循环条件： `left < right`
- 中间位置计算： `mid = left + ((right -left) >> 1)`
- 左边界更新：`left = mid + 1`
- 右边界更新： `right = mid`
- 返回值： `nums[left] == target ? left : -1`


## template 3 左边界查找2 
> 数组部分有序且包含重复元素的情况 \
> Find Minimum in Rotated Sorted Array II
- 循环条件： `left < right`
- 中间位置计算： `mid = left + ((right -left) >> 1)`
- 左边界更新：`left = mid + 1`
- 右边界更新： `right = mid` or `right -= 1`
- 返回值： `nums[left] == target ? left : -1`



## template 4 右边界查找1

- 循环条件： `left < right`
- 中间位置计算： `mid = left + ((right -left) >> 1) + 1` (无论对于奇数还是偶数,这个中间的位置都是偏右的)
- 左边界更新：`left = mid`
- 右边界更新： `right = mid - 1`
- 返回值： `nums[right] == target ? right : -1`

