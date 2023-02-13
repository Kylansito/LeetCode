# Given a string s, return the number of segments in the string.
class Solution:
    def countSegments(self, s: str) -> int:
        grouped = s.split(" ")
        countW = 0
        for i in range(0, len(grouped)):
            if grouped[i] != "" and grouped[i] != " ":
                countW += 1
        return countW