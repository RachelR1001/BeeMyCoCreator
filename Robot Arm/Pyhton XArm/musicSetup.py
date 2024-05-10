"""
Music Set Up
"""
testDataList = [{'pitch': 48, 'startTime': 0, 'endTime': 3}, {'pitch': 65, 'startTime': 1, 'endTime': 4}, {'pitch': 76, 'startTime': 2, 'endTime': 5}, {'pitch': 57, 'startTime': 3, 'endTime': 6}, {'pitch': 59, 'startTime': 4, 'endTime': 7}, {'pitch': 81, 'startTime': 5, 'endTime': 8}, {'pitch': 77, 'startTime': 6, 'endTime': 9}, {'pitch': 50, 'startTime': 7, 'endTime': 10}, {'pitch': 72, 'startTime': 8, 'endTime': 11}, {'pitch': 53, 'startTime': 9, 'endTime': 12}, {'pitch': 50, 'startTime': 10, 'endTime': 13}, {'pitch': 83, 'startTime': 11, 'endTime': 14}, {'pitch': 76, 'startTime': 12, 'endTime': 15}]

score_matrix = [[72,74,76,77,79,81,83],
                [60,62,64,65,67,69,71],
                [48,50,52,53,55,57,59]]
music_dict = {}
for line_num, m in enumerate(score_matrix):
    for idx, x in enumerate(m):
        music_dict[x] = (line_num + 1, idx)

print(music_dict)

testlist = [62,74,57,77,50,81,48]
melody = testlist
def get_target_position(num):
    print(music_dict)
    line_num, position = 1, 1
    if num in music_dict:
        line_num, position = music_dict[num]
    elif num < 83:
        line_num, position = music_dict[num+1]
    return line_num, position
