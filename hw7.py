passwd = open("/etc/passwd", "r")
group = open("/etc/group", "r")
output = open("output.txt", "w")


console_count = {}
groups = {}
gid_to_gname = {}
uname_to_uid = {}

for line in group.readlines():
    name, passw, gid, users_str = line.strip().split(":")
    gid_to_gname[int(gid)] = name
    groups[name] = users_str.split(",") if users_str != "" else []

for line in passwd.readlines():
    name, passw, uid, gid, data, home, console = line.strip().split(":")
    uname_to_uid[name] = uid
    gid = int(gid)
    console_count[console] = console_count.get(console, 0) + 1

    # может такое быть что в /etc/passwd указана группа а в /etc/group - нет
    already_added_users = groups.get(gid_to_gname[gid], [])
    if name not in already_added_users:
        groups[gid_to_gname[gid]] = groups.get(gid_to_gname[gid], []) + [name]

output.write("Task #1\n\n")
for cons in console_count:
    output.write(f"{cons} - {console_count[cons]}\n")

output.write("\nTask #2\n\n")
for gr in groups:
    for i in range(len(groups[gr])): groups[gr][i] = uname_to_uid[groups[gr][i]] # write uids not names
    output.write(f"{gr} : {' , '.join(groups[gr])}\n")

passwd.close()
group.close()
output.close()

# vagrant@ubuntu-bionic:~$ grep rasul /etc/group
# rasul:x:1016:ubuntu
# vagrant@ubuntu-bionic:~$ grep ubuntu output.txt 
# ubuntu : 1001
# vagrant@ubuntu-bionic:~$ grep rasul output.txt 
# rasul : 1001 , 1011
# vagrant@ubuntu-bionic:~$ grep rasul /etc/passwd
# rasul:x:1011:1016:Best User:/home/rasul:/bin/bash
# vagrant@ubuntu-bionic:~$