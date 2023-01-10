## template 1

- 循环条件：`left <= right`
- 中间位置计算： `mid = left + ((right -left) >> 1)`
- 左边界更新：`left = mid + 1`
- 右边界更新：`right = mid - 1`
- 返回值： `mid / -1`



## template 2 左边界查找1
> 数组有序，但包含重复元素, 
> 数组部分有序，且不包含重复元素
- 循环条件： `left < right`
- 中间位置计算： `mid = left + ((right -left) >> 1)`
- 左边界更新：`left = mid + 1`
- 右边界更新： `right = mid`
- 返回值： `nums[left] == target ? left : -1`


## template 3 左边界查找2 
> 数组部分有序且包含重复元素的情况
- 循环条件： `left < right`
- 中间位置计算： `mid = left + ((right -left) >> 1)`
- 左边界更新：`left = mid + 1`
- 右边界更新： `right = mid` or `right -= right`
- 返回值： `nums[left] == target ? left : -1`
