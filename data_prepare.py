import sys
import os


# sys.argv[1]: num of sentences in training dataset
# sys.argv[2]: num of sentences added to training dataset
# sys.argv[3]: epoch of run
# sys.argv[4]: the selecting strategy

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

    with open("data/" + sys.argv[3] + "/" + str(int(sys.argv[1])) + "/train.tsv",'r', encoding='utf8') as f:
        for line in f:
            total_select.append(line.strip())

    os.makedirs("data/" + sys.argv[3] + "/" + str(int(sys.argv[1]) + int(sys.argv[2])),exist_ok=True)
    with open("data/" + sys.argv[3] + "/" + str(int(sys.argv[1]) + int(sys.argv[2])) + "/train.tsv", "w", encoding='utf8') as fw:
        for line in total_select:
            fw.write(line+"\n")

    with open("data/" + sys.argv[3] + "/" + str(int(sys.argv[1]) + int(sys.argv[2])) + "/unused.tsv", "w", encoding='utf8') as fw:
        for line in total_unselect:
            fw.write(line+"\n")


if __name__ == "__main__":
    main()
