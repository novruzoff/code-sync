class Solution:
  def romanToInt(self, s: str) -> int:
    answer = 0
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}

    for i, j in zip(s, s[1:]):
      if numerals[i] < numerals[j]:
        answer -= numerals[i]
      else:
        answer += numerals[i]

    return answer + numerals[s[-1]]