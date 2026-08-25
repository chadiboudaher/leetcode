class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = ""

        for c in address:
            if c != ".":
                new_address += c
            else:
                new_address += "[.]"

        return new_address