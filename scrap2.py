t='''DVYCNZVJIHNVMNBDFTRRSNNXPIRMFMZZOYUFXGBEHKEVDDFVMTURWDAXMDGKMZBIOJZFOZLZOHLGVMFVBIQEPOUZOBCRSOVTVGNIUJVEUZEVT
OZVPIFYPMRZUCBLHCGZXJHCENNZMVOFVONCJOGCFVAUTZRKIZJRUZEPQVEKPAGYFRBIMYVKJNNNBTVYBQRFGYEZWDAXPASKIZFGMZREBIQIFBHCBOV
EHOUVDDETVGNKJJANIZAVWZEZGDAUNTFVMATIPRVEHBEZNVOFVOGYFHBLUCJYFIRMFMVKJNNUBHCUSDMQMTAFWZZSFMVENTFFVGJYFIRMFMVWJIQDZ
NRCGDAMPGHEUVEZMTCRVNVEHWRWPMRTPASZORNIFCBLTZFROYOIJITZOBHGUCRIFVEFGZIVSTSLOZERMDZVFONEEZFGFXVRMGLNIZAVWZEDZCLGPNT
VUNHTIVALQKRIIVAUPAZVUCNKJOEVRPVIFNNJUMBEHHBIBGCIJIPZQGRKPKEVWZAKNZSIPHQVMDOVSVGVMTFKFKCZOBVEUJGYFNGIFZGROYZVUCBUJ
XNCMTXEPXXZOBCVPKYVTCNKTJSWUCREJVPTPPAKJOUZHCGZNZGFHZGKPNRRBNFFPINJJXNEUCVJJNZPTPOJUDGLUZSFSKVJUJYROYORMGJZUCNGIDY
FTJCYJXNCGGBLSDFYDVGFUCEFXNUZNNRCGPCFOCVJTRBIEDDLJZGCZONBFOBKIZFYJKGYFMRZTIBKIDAXTPEGSDFZOBVEUCVJJAGYFTOLUFAVXDGRM
HBJUVYCNZAZOOUVJMQVHMRVTJZVUDZVPMBKIZETIZEZTCIVSTAVBMYPUCRJBHRWFZYZOBFKPRNIENGYFJPVBIJZUCZVUCRIFIBNJNLFVMVETPYRSXV
KZJSKIZZROCNKUJRJCZYKFYEFVIQSZRURSQRJBNVEEDNEJNYVTWLTPMNCSZRWTXBDNZETFNHISJHEENVKXDGYIZEJVMSIJBUKBIQCFAGKIZFKSZRKT
ONBFTBLXVGVSRNIEDGJFSGIFHRUPRAKPRAZTOUVCVGKFMLNIZEVUCNKOJOCFHBCFDFNBNUVEWLNBQRJBIQTPJYVEWLSSZRQFNJYJXURGZJYPPEJQMR
MJJHJXZEVPPGFGNVXIOBWMVAUMJBBBOGYFXEFXYFFGRNKFMTRAZEJUCRIF'''

s=t.replace('\n','')

d={}
for i in range(len(s)):
    if i%4==2:
        if s[i] in d:
            d[s[i]]+=1
        else:
            d[s[i]]=1
for i in d:
    print(i+': '+str(d[i]))