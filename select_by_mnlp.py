import sys
import math


# sys.argv[1] 输入文件
# sys.argv[2] 输出文件

class Example:
    def __init__(self, text, raw_score, score):
        self.text = text
        self.raw_score = raw_score
        self.score = score


def main():
    example_list = []
    with open(sys.argv[1], 'r', encoding='utf8') as f:
        for line in f:
            items = line.strip().split("\t")
            score_list = items[-1].split(" ")
            score = 0
            for _score in score_list:
                score += math.log(float(_score))
            example_list.append(Example("\t".join(items[:-1]), items[-1], 1 - score / len(score_list)))
        example_list = sorted(example_list, key=lambda x: x.score, reverse=True)

    with open(sys.argv[2], 'w', encoding='utf8') as fw:
        for example in example_list:
            fw.write(example.text+"\t"+example.raw_score+"\t"+str(example.score)+"\n")


if __name__ == "__main__":
    main()