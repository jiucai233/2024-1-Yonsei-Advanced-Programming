import os

dnamecwd=os.getcwd()
dname='emails'
fname_email=os.listdir(dname)
print(fname_email)
for fname in fname_email:
    fname_joined=os.path.join(dnamecwd,dname,fname)
    print(fname_joined)
    print(os.path.splitext(fname_joined))