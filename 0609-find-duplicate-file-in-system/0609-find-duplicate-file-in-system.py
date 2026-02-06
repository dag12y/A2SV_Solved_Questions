class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        content_map = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file in parts[1:]:
                name, content = file.split('(')
                content = content[:-1]
                full_path = directory + "/" + name
                content_map[content].append(full_path)

        return [files for files in content_map.values() if len(files) > 1]