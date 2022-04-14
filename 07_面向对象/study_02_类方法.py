class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print(cls.count)


fuzi = Tool("斧子")
banShou = Tool("扳手")
Tool.show_tool_count()
