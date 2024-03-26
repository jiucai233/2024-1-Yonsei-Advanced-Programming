num_hits=11
tree_hitpoints=10
for trial in range(num_hits):
    if tree_hitpoints!=0:
        print(f'---u have been hit tree fo {trial} times---\n---seems u should hit {num_hits-1} more times to take it down!---')
        num_hits-=1
        tree_hitpoints-=1
        print('------')
        continue
    if tree_hitpoints==0:
        print('---u have been hit tree for 10 times---\n---tree is down---\n---no more trees to hit---')
        break