from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            name, domain = email.split('@')

            local = name.split('+')[0].replace('.', '')

            unique.add(local + '@' + domain)

        return len(unique)
