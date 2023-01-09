# DP解体模板1 Search + DP 101

Search 当一个大问题是由多个子问题构成是， 我们可以通过不断分解问题来最终构建我们想求的大问题，这个过程称为搜索

搜索空间(search space)可以用tree的形式展现出来， 便于理解
时间复杂试取决于这棵树的深度和每个node的children个数
**Search最重要的就是定义好状态，保证每个子问题都能用一个状态来描述**

如果search space有重复子问题，可以记录这些子问题的答案来保证不会重复计算多次，所以DP也被称为Search + Memoiration

**所有DP都可以写成bottom up DFS 的形式**


## Topdown DFS (tablulation)

1. Define STATE of subproblems
2. Initialize inital state
3. Call dfs(init_state)


dfs(state):
1. Base case check
2. For each subproblem x
   1. a update state = next_state_x
   2. branch down -> call dfs(next_state_x)
   3. **Restore State**


## Bottom Up DFS (memoization)

1. Define STATE of subproblems
2. initialize memo to record calculated subproblem
3. return dfs(top_level_anwer_state)


dfs(state)
1. Base case check
2. if current problem is calculated, return its answer
3. For each Subproblem X
   1. Ask subproblem for their answers -> call dfs(subproblem_state)
   2. build up current state problem answer base on subproblem answer
4. Sotre current problem answer


### for string and array 一般只有2种状态定义
1. i = index or problem_lenght -> dp[i] 代表[0,) 的答案
2. i,j = indexes -> dp[i][j] 代表array[i]-array[j]这段subarray的答案
   