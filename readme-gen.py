import os
import requests
from progress.bar import Bar

fout = open("README.md", "w")

problems = {}

dir = [f for f in os.listdir("python/") if os.path.isfile("python/" + f)]
for file in dir:
    file = file.partition("_")
    num = int(file[0])
    problems[num] = file[2]

fout.write("# Leetcode Solved\n\n")
fout.write("| #   | Problem | Difficulty | Solutions |\n")
fout.write("| --: | ------- | ---------- | --------- |\n")

easy = medium = hard = 0

bar = Bar('Processing', max=len(problems))
for i in sorted(problems):
    id = problems[i][:-3]

    data = {"operationName": "questionData", "variables": {"titleSlug": id},
            "query": "query questionData($titleSlug: String!) {question(titleSlug: $titleSlug) {title difficulty}}"}
    leetcode = requests.post('https://leetcode.com/graphql', json=data).json()

    name = leetcode['data']['question']['title']
    difficulty = leetcode['data']['question']['difficulty']
    url = "https://leetcode.com/problems/" + id
    path = "./python/" + str(i) + "_" + problems[i]

    fout.write(
        f"| ``{i}`` | [{name}]({url}) | {difficulty} | [python]({path}) |\n")

    match difficulty:
        case 'Easy':
            easy += 1
        case 'Medium':
            medium += 1
        case 'hard':
            hard += 1

    bar.next()

fout.write("""
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://leetcode-stats-six.vercel.app/?username=kutaycinar&theme=dark">
    <source media="(prefers-color-scheme: light)" srcset="https://leetcode-stats-six.vercel.app/?username=kutaycinar">
    <img width=655px>
</picture>
""")

bar.finish()
