def remove(ref_list, target):
    # リスト内部からtargetを削除する
    ref_list.remove(target)
    return ref_list[0]


# 友達関係の把握
[N, M] = list(map(int, input().split()))
relations_list = []
for i in range(M):
    relations_list.append(list(map(int, input().split())))
relations_list = list(map(sorted, relations_list))
# グループ分け
remain_list = list(range(1, 1+N))
group_list = []
while remain_list != []:
    # グループ構成員を求める
    group = []
    group.append(remain_list[0])
    search_list = []
    search_list.append(remain_list[0])
    while search_list != []:
        search = search_list.pop(0)
        # searchに関わるrelationの抽出
        candidate_relations = [
            relation for relation in relations_list if search in relation]
        # 今後検索しないため，relations_listからcandidate_relationsを削除
        for candidate_relation in candidate_relations:
            relations_list.remove(candidate_relation)
        candidate_list = [remove(i, search) for i in candidate_relations]
        search_list.extend(candidate_list)
        group.extend(candidate_list)
        # 検索候補とグループ内部の重複をなくす
        search_list = list(set(search_list))
        group = list(set(group))
    for student in group:
        remain_list.remove(student)
    group_list.append(group)

# 最小グループ数の求め
print(max([len(group) for group in group_list]))
