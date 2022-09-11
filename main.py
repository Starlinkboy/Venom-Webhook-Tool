try:
    import httpx, os, sys, threading, time
    from pystyle import *
except Exception as zt:
    print(f'Missing imports | {zt}')


logo2 = '''Venom | github/starlinkboy | Starlinkboy#0159'''
def main():
  System.Size(165, 55)
  logo = """
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⢶⡲⠟⠛⢉⣀⣨⣉⣉⠛⠚⠛⠷⣖⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⣯⠟⠋⣁⣤⣤⡶⡋⠀⢀⡄⠀⠉⠀⠀⠀⠀⠙⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣧⣵⠟⠋⠼⠋⠉⣠⢾⡇⢠⣾⡇⢧⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠤⢴⣄⡀⠀⠀⢠⢋⣭⠏⣠⠊⠀⠀⣴⢃⣦⢷⢸⡇⠻⣆⡓⠦⠤⣤⡄⠀⠀⠀⠀⠀⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣿⣿⣆⢠⣿⡿⠁⠞⠁⠀⠀⣰⠃⣼⣿⡼⢸⡇⠀⠀⠙⠷⣤⣘⠳⣤⣀⠀⣀⠀⠀⠸⡷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣿⣿⡿⡟⠀⠀⠀⠀⠀⢠⡿⢸⣿⣷⡇⠀⢹⡄⠀⠀⠀⠀⠙⠳⠦⣍⡳⣌⠻⣆⠀⠸⣷⠀⠀Github: github.com/starlinkboy⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣿⣿⣿⠟⠀⠀⠀⡀⠀⠐⡿⠁⣾⣿⣿⣽⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⢳⡽⣆⢸⡄⠈⣻⠀⠀ Discord: Starlinkboy#0159⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⠁⠀⠀⡾⢿⠀⢸⢁⣼⣿⣿⣿⣟⡄⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢞⢆⢳⡄⣸⠀⠀⠀Venom Webhook Tool⠀⠀⠀⠀⠀⠀⠀
⣇⠀⢸⣷⣿⠀⠀⠈⠀⡸⠀⡞⣻⣿⣟⣩⣾⣿⡿⣄⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⢸⣟⢾⠀⠀⠀Made with⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣌⣿⠇⠀⠀⠀⡰⠁⢠⣳⣿⠛⣻⣿⣿⣿⢿⣿⣦⠀⢳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠘⡆⢿⣞⠀⠀Love❌ Code✅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡏⠙⠂⠀⠀⠀⡇⠀⠀⢸⣟⣾⣿⣿⣿⣿⣿⣿⣿⢧⣀⠀⠈⠛⠓⠶⠲⠷⠛⠢⡀⢱⠸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⢦⡀⠀⠀⢸⣹⣄⢠⡈⣿⡿⣯⣿⡿⣿⣿⣿⣿⡿⣿⣞⣶⣦⣤⣶⣦⣶⣶⣤⣈⠻⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⠃⠀⠀⠘⢯⡞⡄⢹⣿⣾⣿⣟⣿⣿⣿⣿⣿⣽⢛⠏⣿⠹⡿⢻⠉⡟⣿⠻⣿⢿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣤⣦⢀⡖⠀⠀⠀⠀⠻⣿⡿⡈⢿⣽⣿⣏⣿⣽⣿⣿⣿⡏⠈⡼⡿⢸⠁⣼⢠⡇⢣⠀⡾⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠛⠋⠃⡼⠬⢳⡀⠀⠀⣹⡇⠸⣆⢹⣃⣿⣿⣿⣿⣿⣿⣿⠎⠁⠀⢠⢰⢿⡜⡇⡄⢀⣿⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡀⠀⢸⡃⣠⢖⣿⡇⠀⢿⡞⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠇⠈⢸⣧⢺⢹⣸⢿⡸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣦⣃⢠⣾⠟⠁⣼⣿⣇⠀⠘⣷⢿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡂⠀⠘⡟⢸⢸⡇⠸⠃⠉⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀⠀
⠀⠀⢻⡼⠿⠁⠀⢰⣿⣿⣿⡆⠀⣿⣼⣿⡿⣿⣿⣿⣿⣙⠛⣿⠛⣻⣶⣤⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀
⠀⠀⣼⠁⠀⠀⣠⣿⣻⣿⣿⣆⠀⠸⣿⣷⠿⣿⣿⣿⣿⣾⣤⢨⡙⣳⢼⠑⣻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀
⡶⠋⠁⠀⡠⣴⡿⠟⠉⠉⠉⠻⣦⠀⠘⣿⡿⢽⣿⢿⣿⣿⣿⣾⣿⣿⣤⡙⢮⣻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀
⠀⠀⠀⢨⡿⠃⠀⠀⠀⠀⠀⠀⠘⢧⡀⢸⣿⣿⣒⣯⡿⢿⣿⣿⣿⣿⡽⣿⡅⠙⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀
⠀⠀⢲⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠙⣿⣍⣴⢾⣿⣿⣿⣿⣿⣿⡵⢟⣆⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀
⠀⢀⡨⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠘⢷⣯⠽⣺⢟⢿⣿⣿⣿⣦⣪⡚⢆⠚⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣿⠀
⠈⠏⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠘⣿⣯⡵⢡⣾⢻⣿⣿⣿⣿⣷⡈⣳⡤⠻⡄⠀⠀⠀⠀⠀⠀⣠⣾⣿⠃⠀
⠛⠤⢴⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠘⣿⣷⣯⢃⡏⣸⣿⠻⣿⣿⣿⣇⡹⣌⠨⢷⣄⡀⣀⣠⣾⣿⠟⠁⢀⡀
⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡂⠈⠛⠿⣿⣶⣧⡇⡿⣹⢯⣿⡿⢇⠞⠓⠦⠤⠭⠽⠟⡋⠁⠀⣰⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⣄⡀⠀⠈⠻⢿⣿⣷⣷⣿⣶⡞⠁⠀⠀⠀⠀⠀⠀⣄⢧⠀⣺⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠺⣧⣄⠀⠀⠀⠉⠻⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⡿⣻⢷⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠢⠤⠤⣤⣤⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀
  """
  Anime.Fade(Center.Center(logo), Colors.black_to_white, Colorate.Vertical, interval=0.01, time=6)




  def delete():
    r = httpx.delete(web)
    if r.status_code == 200:
      print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('[!] Webhook Deleted Succesfully!')))
    else:
      print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('[!] Webhook Failed To Delete!')))
  
  
  def spam():
    message = input(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('[?] Message: ')))
    us = input(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('[?] Embed Author: ')))
    ef = input(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('[?] Footer: ')))
    threads = input(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('[?] Threads: ')))

    
    embeds = []
    embed = {
                            "color": 000000,
                            "fields": [
                                {
                                    "name": "**https://github.com/Starlinkboy/Venom-Webhook-Tool**",
                                    "value": f'```Venom Spammer```',
                                    "inline": True
                                },
                            ],
                            "author": {
                                "name": f"{us}",
                                "icon_url": f'https://media.wired.com/photos/5bb69ec50bba6f2d70ffcc11/master/w_2560%2Cc_limit/Venom_TA.jpg'
                            },
                            "footer": {
                            "text": f"{ef}"
                            }
                            
    }
    embeds.append(embed)
      
    os.system('cls')
    os.system('cls')
    
    data = {
                      "content": message,
                      "embeds": embeds,
                      "username": 'Venom Webhook Tool',
                      "avatar_url": 'https://media.wired.com/photos/5bb69ec50bba6f2d70ffcc11/master/w_2560%2Cc_limit/Venom_TA.jpg'
    }
      
    for x in range(int(threads)):
         r = httpx.post(url=web, json=data)
         try:
              r = httpx.post(url=web, json=data)
              if r.status_code == 200 or 204:
                print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('[!] Message Sent!')))
              if r.status_code == 404:
                print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('[!] Invalid Webhook Or Deleted!')))
                print(logo2)
                sys.exit()
              if r.status_code == 429:
                print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(f"[!] Rate Limited: ({r.json()['retry_after']}ms)\n")))
         except KeyboardInterrupt:
                 break
  
  
  txt = """
██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝
                                               
"""
  print(
            Colorate.Vertical(
                Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(txt)
            )
        )

  opt = input(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('[1] Webhook Deleter | [2] Webhook Spammer: ')))
  web = input(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('[?] Webhook: ')))
  if opt == '1':
          delete()
          main()
  elif opt == '2':
          spam()
          main()
  else:
          print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(f'[!] Error invalid choice | {opt}')))
          time.sleep(3)
          main()
  
main()

