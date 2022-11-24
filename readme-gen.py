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

fout.write("# leetcode\n\n")
fout.write("| #   | Problem | Difficulty | Solutions |\n")
fout.write("| --: | ------- | ---------- | --------- |\n")

easy = medium = hard = 0

bar = Bar('Processing', max=len(problems))
for i in sorted(problems):
    id = problems[i][:-3]

    data = {"operationName": "questionData", "variables": {"titleSlug": id}, "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}
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

fout.write(f"\n")
fout.write(f"# {len(problems)} solved\n")
fout.write(f"### easy: ``{easy}``\n")
fout.write(f"### medium: ``{medium}``\n")
fout.write(f"### hard: ``{hard}``\n")

bar.finish()
