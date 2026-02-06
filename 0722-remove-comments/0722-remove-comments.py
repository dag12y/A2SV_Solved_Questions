class Solution(object):
    def removeComments(self, source):
        res = []
        in_block = False
        buffer = ""

        for line in source:
            i = 0
            if not in_block:
                buffer = ""

            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    break
                elif not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 1
                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 1
                elif not in_block:
                    buffer += line[i]
                i += 1

            if buffer and not in_block:
                res.append(buffer)

        return res
