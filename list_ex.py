'''pokedex_list_seen = [15, 16, 18, 19, 32]
pokedex_list_caught = ["Ho-oh", "Charizard", "Lugia"]
pokedex_list_unk = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,...]

pc = pokedex_list_caught

poke_in_pockets = ["Alakazam", "Rayquaza", "Rhyperior", "Tyranitar", "Chikorita"
, "Mankey"]

#personaje entra en combate.

print("Go " + poke_in_pockets[0] + "!" )

Alakazam_basic = [32]
#stats = [atk, atk sp, def, defsp, speed]
Alakazam_01 = ["Pyschic", "Future Sight", "Flash", "Recover"]
Alakazam_01_stats = [200, 315, 216, 122, 185]

Vaporeon_enemy1 = ["Water gun", "Acid Armor", "Substitute", "Surf"]
Vaporeon_enemy1_stats = [150, 100, 280, 260, 200]

water_gun = [32]

vap_damage = Vaporeon_enemy1_stats[1] + water_gun[0]


total_damge = vap_damage - Alakazam_01_stats[3]
print("What will you do?")
options = ["Fight", "Object", "Pokémon", "Run"]


print("Vaporeon used water gun!")
print("Alakazam received " + str(total_damge) + " hp damage from foe!")


#print(poke_in_pockets)
#print(pokedex_list_caught)
'''
'''
moved_pokemon = poke_in_pockets.pop(5)

print(poke_in_pockets)
print(moved_pokemon)


print(pokedex_list_caught)

poke_box01 = []

poke_box01.append("Seviper")
poke_box01.append("Torterra")
poke_box01.append("Swellow")
poke_box01.append("Talonflame")
poke_box01.append("Gliscor")

print(poke_box01)

poke_box01.insert(1, "Cyndaquil")

print(poke_box01)

print(poke_in_pockets)

poke_box01.append(moved_pokemon)
print(poke_box01)


poke_box01.remove('Torterra')

print(poke_box01)

Fran 1st Answer 2.0

guests = ["Reddmar", "Yosthon", "Ricardo"]
invitation_01 = "Dear " + guests[0] + ", I'll order some pizza, so come over, mamawebo!"
invitation_02 = "Dear " + guests[1] + ", I'll order some pizza, so come over, mamawebo!"
invitation_03 = "Dear " + guests[2] + ", I'll order some pizza, so come over, mamawebo!"
print(invitation_01)
print(invitation_02)
print(invitation_03)



guests = ["Reddmar", "Yosthon", "Ricardo", "Aaron", "Quinn", "Zim", "Keyla"]


print("Dear " + guests[0] + ", I'll order some pizza, so come over, mamawebo!")
print("Dear " + guests[1] + ", I'll order some pizza, so come over, mamawebo!")
print("Dear " + guests[2] + ", I'll order some pizza, so come over, mamawebo!")


print(sorted(guests))
print(guests)


guests.sort()
print(guests)

guests.sort(reverse=True)
print(guests)

guests.reverse()
print(guests)

print(len(guests))

'''
guests = ["Reddmar", "Yosthon", "Ricardo", "Aaron", "Quinn", "Zim", "Keyla"]

print(guests[-1])