"""
Write a function to find the common free time for all employees from a list called schedule. Each employee's schedule is represented by a list of non-overlapping intervals sorted by start times. The function should return a list of finite, non-zero length intervals where all employees are free, also sorted in order.

Input:

schedule = [[[2,4],[7,10]],[[1,5]],[[6,9]]]
Output:

[(5,6)]
Explanation: The three employees collectively have only one common free time interval, which is from 5 to 6.
"""

class Solution:
    def employeeFreeTime1(self, schedule: list[list[list[int]]]) -> list[list[int]]:
        start, end = float('inf'), float('-inf')
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                start = min(start, schedule[i][j][0])
                end = max(end, schedule[i][j][1])

        free_times = []
        for i in range(len(schedule)):
            free_time = []
            for j in range(len(schedule[i])):
                if not free_time and schedule[i][j][0] > start:
                    free_time.append([start, schedule[i][j][0]])
                elif schedule[i][j][0] > schedule[i][j-1][0]:
                    free_time.append([schedule[i][j-1][1], schedule[i][j][0]])
            else:
                if end > schedule[i][j][1]:
                    free_time.append([schedule[i][j][1], end])

            free_times.append(free_time)
        print(free_times)

    def employeeFreeTime(self, schedule: list[list[list[int]]]) -> list[list[int]]:

        # flattened_schedule = []
        # for i in range(len(schedule)):
        #     for j in range(len(schedule[i])):
        #         flattened_schedule.append(schedule[i][j])
        
        flattened_schedule = [i for employee in schedule for i in employee ]
        flattened_schedule.sort(key=lambda x: x[0])

        # merge overlaps
        # merged_schedule = [flattened_schedule[0]]
        # for i in range(1, len(flattened_schedule)):
        #     if merged_schedule[-1][1] >= flattened_schedule[i][0]:
        #         merged_schedule[-1][0] = min(merged_schedule[-1][0], flattened_schedule[i][0])
        #         merged_schedule[-1][1] = max(merged_schedule[-1][1], flattened_schedule[i][1])
        #     else:
        #         merged_schedule.append(flattened_schedule[i])
        # no need of min as it's alredy sorted. 

        merged_schedule = []
        for interval in flattened_schedule:
            if not merged_schedule or merged_schedule[-1][1] < interval[0]:
                merged_schedule.append(interval)
            else:
                merged_schedule[-1][1] = max(merged_schedule[-1][1], interval[1])
        
        free_times = []
        for i in range(1, len(merged_schedule)):
            # if merged_schedule[i][0] > merged_schedule[i-1][1]:
            #     free_times.append([merged_schedule[i-1][1], merged_schedule[i][0]])
            # no need of above, as it's alreday merged

            free_times.append([merged_schedule[i-1][1], merged_schedule[i][0]])
        return free_times

if __name__ == "__main__":
    print(Solution().employeeFreeTime([[[2,4],[7,10]],[[1,5]],[[6,9]]])) # [(5,6)]