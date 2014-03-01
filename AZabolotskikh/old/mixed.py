host = list(input());
guest = list(input());
mix = list(input());
try:
    for letter in host:
        mix.remove(letter);
    for letter in guest:
        mix.remove(letter);
except:
    print ("NO");
else:
    if len(mix)==0:
        print("YES");
    else:
        print ("NO");