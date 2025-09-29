"""
On forums like reddit, comments can reply to each other and be nested.
See https://old.reddit.com/r/math/comments/4lbxlf/a_geometric_haircut/ for example

Given a list of comments (with id, parent id and message), print all comments in a threaded manner.

eg. For the following input (assume parent id of 0 means no parent):

```
id,message,parent
1,first comment,0
2,second comment,0
3,first reply,1
4,second reply,3
5,another reply,1
```

The output should be (spaces are important!):

```
1 first comment
    3 first reply
        4 second reply
    5 another reply

2 second comment
```

GUIDELINES:
* Please write the code in a maintainable way like you'd write in a production environment.
* Do NOT treat this as merely a competitive programming problem, code quality matters
* Your input will be a single string, you must output to standard out
* You may use Google for basic questions on syntax etc but naturally not how to solve the problem!


"""

message_input = """id,message,parent
1,first comment,0
2,second comment,0
5,another reply,1
30,first reply,1
4,second reply,30
10,second reply,4
11,second reply,4
12,second reply,2
13,second reply,5
14,top level,0"""
message_list = message_input.split("\n")

from collections import defaultdict

adj_map = defaultdict(list)

for message_coll in message_list[1:]:
    child_id, message, parent = message_coll.split(",")

    # u -> v
    adj_map[int(parent)].append((int(child_id), message))

adj_list = dict(adj_map)

ans_str = ""


def str_builder(parent_id, message, level):
    result = " " * 4 * level + f"{str(parent_id)} {message}\n"
    return result


def dfs(parent_id, level):
    global ans_str
    if parent_id not in adj_list:
        return

    for child in adj_list.get(parent_id):
        child_id, message = child
        ans = str_builder(child_id, message, level)
        ans_str += ans
        dfs(child_id, level + 1)
        if level == 0:
            ans_str += "\n"

dfs(0, 0)
print(ans_str)