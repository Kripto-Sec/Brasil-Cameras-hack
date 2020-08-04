import requests, re, os
import time
import sys
import emoji

print('\033[;1m'+'\033[37m'+"[X] FEITO POR JEAN(KRIPTO-SEC) [X]")
print("\n")

print ('\033[37m'+'\033[;1m'+"[+] INSTALANDO POR FAVOR AGUARDE [+]"+'\033[1;30m')
def progress_bar(done):
    print("\rCarregando: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')

def test():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(0.1)


test()      



#cmd = 'pip3 install emoji'
#os.system(cmd)


print('\033[37m'+"""                       .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ## hello world     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'
"""+'\033[37m')
print("\n")


try:

    while True:

        resp = str(input('\033[;1m'+"Gostaria de ver cameras IP expostas ? (S/N/c): "))
    
        if resp == 'S' or resp == 's' :
            print("Procurando...")
            print("\n")		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}       
                for page in range (0,23):
                
                    url = ("https://www.insecam.org/en/bycountry/BR/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                        hasil = findip[count]

                        print ('\033[1;34m'+"Camera Encontrada: ""\033[1;32m"+hasil)
                    
                        count += 1
            except:
                print (" ")
        
        elif resp == 'N' or resp == 'n':
            print(emoji.emojize('\033[1;31m'+"Obrigado por usar adeus"+'\033[1;31m' ":red_heart:"))
            break

        elif resp == 'c' or resp == 'C':
            print("\n")
            print('\033[37m'+'\033[;1m'+"[X] CREDITOS: "+'\033[;1m'+'\033[37m')
            print('\033[37m'+'\033[;1m'+"[X] FEITO POR JEAN(KRIPTO-SEC)"+'\033[;1m'+'\033[37m')
            print('\033[37m'+'\033[;1m'+"[X] github:https://github.com/Kripto-Sec "+'\033[;1m'+'\033[37m')
            print("\n")

        else:
            print("\n")
            print("Por favor use apenas S para sim N para nao e C para creditos")
            print("\n")
            

except KeyboardInterrupt:
    print (" ")


                