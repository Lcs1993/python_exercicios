cid = str(input('Em que cidade você nasceu? ')).strip()
print('A sua cidade começa com santo? \033[97m {}'.format(cid[:5].upper() == 'SANTO'))

