power, numDragons = list(map(int, input().split()));
dragons = [];
for i in range(numDragons):
    dragons.append(list(map(int, input().split())));
dragons = sorted(dragons, key=lambda x:[0]);
for dragon in dragons: #here be dragons
    if power>dragon[0]:
        power += dragon[1];
    else:
        print ("NO");
        exit(0);
print ("YES");