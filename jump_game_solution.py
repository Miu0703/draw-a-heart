"""
跳跃游戏 II - 最小跳跃次数
问题描述：给定一个长度为 n 的 0 索引整数数组 nums，返回到达 nums[n-1] 的最小跳跃次数。

解法思路：贪心算法
核心思想：在每一步中，我们都选择能跳到最远位置的跳跃方式。
"""

def jump(nums):
    """
    使用贪心算法求解最小跳跃次数
    
    参数:
        nums: 整数数组，nums[i] 表示从位置 i 最多能跳跃的步数
    
    返回:
        到达最后一个位置的最小跳跃次数
    """
    n = len(nums)
    if n <= 1:
        return 0
    
    # 跳跃次数
    jumps = 0
    # 当前跳跃能到达的最远位置
    current_end = 0
    # 在当前跳跃范围内，下一跳能到达的最远位置
    farthest = 0
    
    # 遍历数组（不需要遍历最后一个元素，因为我们的目标就是到达它）
    for i in range(n - 1):
        # 更新在当前跳跃范围内，下一跳能到达的最远位置
        farthest = max(farthest, i + nums[i])
        
        # 如果已经到达了当前跳跃的边界
        if i == current_end:
            # 必须进行下一跳
            jumps += 1
            # 更新当前跳跃能到达的最远位置
            current_end = farthest
    
    return jumps


def jump_with_path(nums):
    """
    返回最小跳跃次数和跳跃路径
    
    参数:
        nums: 整数数组
    
    返回:
        (最小跳跃次数, 跳跃路径)
    """
    n = len(nums)
    if n <= 1:
        return 0, [0] if n == 1 else []
    
    jumps = 0
    current_end = 0
    farthest = 0
    path = [0]  # 记录跳跃路径
    
    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            # 找到下一跳的最佳位置
            next_pos = i + 1
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                if j + nums[j] >= next_pos + nums[next_pos]:
                    next_pos = j
            if next_pos < n - 1:
                path.append(next_pos)
    
    if path[-1] != n - 1:
        path.append(n - 1)
    
    return jumps, path


# 测试用例
def test_jump_game():
    """测试函数"""
    test_cases = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([1, 1, 1, 1], 3),
        ([1, 2, 3], 2),
        ([0], 0),
        ([1], 0),
        ([2, 1], 1)
    ]
    
    print("=== 跳跃游戏测试结果 ===")
    for i, (nums, expected) in enumerate(test_cases):
        result = jump(nums)
        jumps, path = jump_with_path(nums)
        
        print(f"\n测试用例 {i+1}:")
        print(f"输入: {nums}")
        print(f"预期结果: {expected}")
        print(f"实际结果: {result}")
        print(f"跳跃路径: {path}")
        print(f"状态: {'✓ 通过' if result == expected else '✗ 失败'}")


if __name__ == "__main__":
    test_jump_game()
    
    # 详细解释示例
    print("\n" + "="*50)
    print("详细解释示例 1: nums = [2,3,1,1,4]")
    print("="*50)
    
    nums = [2, 3, 1, 1, 4]
    n = len(nums)
    
    print(f"数组: {nums}")
    print(f"目标: 从索引 0 跳到索引 {n-1}")
    print()
    
    # 模拟执行过程
    jumps = 0
    current_end = 0
    farthest = 0
    
    print("执行过程:")
    for i in range(n - 1):
        old_farthest = farthest
        farthest = max(farthest, i + nums[i])
        
        print(f"i={i}: nums[{i}]={nums[i]}, 从位置{i}最远可到达{i + nums[i]}")
        print(f"      更新farthest: {old_farthest} -> {farthest}")
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            print(f"      到达跳跃边界! 跳跃次数: {jumps}, 新的边界: {current_end}")
        
        print()
    
    print(f"最终结果: {jumps} 次跳跃")
    
    # 贪心算法原理解释
    print("\n" + "="*50)
    print("贪心算法原理解释")
    print("="*50)
    print("""
1. 核心思想：在每次跳跃中，选择能到达最远位置的策略

2. 关键变量：
   - jumps: 当前跳跃次数
   - current_end: 当前跳跃能到达的最远位置
   - farthest: 在当前跳跃范围内，下一跳能到达的最远位置

3. 算法流程：
   - 遍历数组的每个位置
   - 不断更新下一跳能到达的最远位置
   - 当到达当前跳跃的边界时，必须进行下一跳
   - 更新跳跃次数和新的边界

4. 时间复杂度：O(n)
   空间复杂度：O(1)

5. 为什么这个贪心策略是正确的？
   - 在每个跳跃范围内，我们选择能让下一跳到达最远的位置
   - 这样能保证用最少的跳跃次数到达目标
   - 因为题目保证一定能到达终点，所以贪心策略是最优的
""")