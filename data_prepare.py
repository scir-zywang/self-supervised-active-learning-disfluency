import sys
import os


# sys.argv[1]: 当前训练使用语料句数
# sys.argv[2]: x: 挑选出x句假如训练集
# sys.argv[3]: 当前的训练是第x个run
# sys.argv[4]: 当前的选择策略

def main():
    total_select = list()
    total_unselect = list()
    with open(sys.argv[3] + "/" + sys.argv[1] + "_predict/"+ sys.argv[4] +".txt", 'r', encoding='utf8') as f:
        t = f.readlines()
        for index, line in enumerate(t[:int(sys.argv[2])]):
            items = line.strip().split("\t")
            total_select.append("\t".join(items[:5]))
        for line in t[int(sys.argv[2]):]:
            items = line.strip().split("\t")
            total_unselect.append("\t".join(items[:5]))

    with open("/users5/zywang/disfluency/ac_learning_data/" + sys.argv[3] + "/" + str(int(sys.argv[1])) + "/train.tsv",
              'r', encoding='utf8') as f:
        for line in f:
            total_select.append(line.strip())

    os.makedirs(
        "/users5/zywang/disfluency/ac_learning_data/" + sys.argv[3] + "/" + str(int(sys.argv[1]) + int(sys.argv[2])),
        exist_ok=True)
    # print("/users5/zywang/disfluency/ac_learning_data/" + sys.argv[3] + "/" + str(int(sys.argv[1]) + int(sys.argv[2])))
    with open("/users5/zywang/disfluency/ac_learning_data/" + sys.argv[3] + "/" + str(
            int(sys.argv[1]) + int(sys.argv[2])) + "/train.tsv", "w", encoding='utf8') as fw:
        for line in total_select:
            fw.write(line+"\n")

    with open("/users5/zywang/disfluency/ac_learning_data/" + sys.argv[3] + "/" + str(
            int(sys.argv[1]) + int(sys.argv[2])) + "/unused.tsv", "w", encoding='utf8') as fw:
        for line in total_unselect:
            fw.write(line+"\n")


if __name__ == "__main__":
    main()