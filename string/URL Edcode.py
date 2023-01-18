'''
253 · URL Edcode



sorted
query_params_sorted = sorted(query_params, key = lambda d: d[0], reverse=False)


'''

from typing import (
    List,
)


class Solution:
    """
    @param base_url: the string of base_url
    @param query_params_list: sequence of two-element tuples by query_params
    @return: return a url query string
    """

    def urlencode(self, base_url: str, query_params_list: List[List[str]]) -> str:
        # write your code.
        # query_params_list = sorted(query_params_list, key=lambda x: (x[0]))

        if not query_params_list:
            return base_url

        query_params_list.sort()

        return base_url + '?' + '&'.join([key + '=' + val for key, val in query_params_list])


so = Solution()

base_url = "https://translate.google.cn/"
query_params_list = [["sl", "en"], ["tl", "zh-CN"], ["text", "Hello"], ["op", "translate"]]


res = so.urlencode(base_url, query_params_list)
print(res)
