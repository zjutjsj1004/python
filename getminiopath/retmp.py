import re

REGEX_PATTERN = r".*/video-onex2/video/.*\.insv"
object_name = "716/383/video-onex2/video/VID_20220311_161702_10_013.insv"

match_result = re.match(REGEX_PATTERN, object_name)

if match_result:
    print("匹配成功")
else:
    print("匹配失败")