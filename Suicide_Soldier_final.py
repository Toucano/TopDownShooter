from math import *
import math,pygame
from sys import *
from random import *
#creer par mbelafdal
pygame.init() # initialisation du module "pygame"
displayx=1331
displayy=700
actualx=displayx-(76*2)
actualy=displayy-(103*2)
fenetre = pygame.display.set_mode((displayx,displayy))#,pygame.FULLSCREEN)
pygame.display.set_caption("suicide soldier") # DÃƒÂ©finit le titre de la fenÃƒÂªtre
fullscreen=False
######Entity values
#bullets=[0]=position(x,y)[1]=argx/argy[2]=bullet_speed[3]bullet_team[4]=damage
#entity=[0]=position(x,y)[1]=sprite[2]entity_team[3]=weapon_selected
#weapon_selected=[0]=Melee[1]=Glock[2]=Rifle[3]=Shotgun
#weapon_selected[x]=[0]=Name[1]=bullet_speed[2]=weapon_reloading_speed[3]=weapon_shot_sound[4]=magazine_capacity[5]=bullets_total[6]=weapon_cadence[7]=weapon_damage[8]=bullet_clip
the_game=True
i=0
reset1=0
reset2=0
reset3=0
reset4=0
reset5=0
reset6=0
reset7=0
reset8=0
reset9=0
reset10=0
reset11=0
time=[]
bullet_reset=0
shooting=0
score=0
cycle=0
weapon_selected=1
instant_direction=1
weapon_names=["Rifle","Glock","Shotgun"]
bullets_ally_speed=40
player_speed=32
playerAlive=True
player_health=100
player_position = (100,displayy/2)
arial32=pygame.font.SysFont("arial",32)
moving=False
bullets_ally=[]
bullet_enemy=[]
entity=[]
main_menu=True
death_menu=False
gaming=False
endmenu=False
######Image files
bullet=pygame.image.load("./imagefiles/sprites/bullet.png")
rifle_sprite_original=pygame.image.load("./imagefiles/sprites/ak47.png")
shotgun_sprite_original=pygame.image.load("./imagefiles/sprites/shotgun_sprite.png")
pistol_sprite_original=pygame.image.load("./imagefiles/sprites/pistol.png")
background=pygame.image.load("./imagefiles/sprites/background lvl1.png")
background2=pygame.image.load("./imagefiles/sprites/background lvl2.png")
background3=pygame.image.load("./imagefiles/sprites/background lvl3.png")
background_full=pygame.image.load("./imagefiles/sprites/background full (1).png")
background_full2=pygame.image.load("./imagefiles/sprites/background full (2).png")
player_sprite=pygame.image.load("./imagefiles/player/player.png")
player_back_sprite=pygame.image.load("./imagefiles/player/player_back.png")
player_not_moving=pygame.image.load("./imagefiles/player/player_not_moving.png")
player_moving2_left=pygame.image.load("./imagefiles/player/player_moving2_left.png")
player_moving_left=pygame.image.load("./imagefiles/player/player_moving_left.png")
player_moving2_right=pygame.image.load("./imagefiles/player/player_moving2_right.png")
player_moving_right=pygame.image.load("./imagefiles/player/player_moving_right.png")
enemie=pygame.image.load("./imagefiles/train_doll/enemies.png")
enemie_dead=pygame.image.load("./imagefiles/train_doll/enemies_dead.png")
enemie_dead2=pygame.image.load("./imagefiles/train_doll/enemies_dead2.png")
start_menu=pygame.image.load("./imagefiles/menu/Start_screen.png")
soldier_ally_sprite=pygame.image.load("./imagefiles/soldier_ally/soldier_ally.png")
soldier_enemy_sprite=pygame.image.load("./imagefiles/soldier_enemy/soldier_enemy.png")
soldier_enemy_dead_sprite=pygame.image.load("./imagefiles/soldier_enemy/soldier_enemy_dead.png")
soldier_enemy_dead_sprite2=pygame.image.load("./imagefiles/soldier_enemy/soldier_enemy_dead2.png")
start_menu_selected=pygame.image.load("./imagefiles/menu/Start_screen_selected.png")
door_up_sprite=pygame.image.load("./imagefiles/sprites/door_upper.png")
door_low_sprite=pygame.image.load("./imagefiles/sprites/door_lower.png")
health_pack_sprite=pygame.image.load("./imagefiles/sprites/health_pack.png")
glock_ammunition_sprite=pygame.image.load("./imagefiles/sprites/glock_ammunition.png")
rifle_ammunition_sprite=pygame.image.load("./imagefiles/sprites/rifle_ammunition.png")
blood_sprite=pygame.image.load("./imagefiles/sprites/blood.png")
blood2_sprite=pygame.image.load("./imagefiles/sprites/blood2.png")
main_screen_sprite=pygame.image.load("./imagefiles/menu/main_screen.png")
bullet_enemy_sprite=pygame.image.load("./imagefiles/sprites/bullet_enemy.png")
crossair_sprite=pygame.image.load("./imagefiles/sprites/crossair.png")
boss_zero_suit_standing=pygame.image.load("./imagefiles/boss/boss_zero_suit_standing.png")
boss_zero_suit_walking1=pygame.image.load("./imagefiles/boss/boss_zero_suit_walking1.png")
boss_zero_suit_walking2=pygame.image.load("./imagefiles/boss/boss_zero_suit_walking2.png")
finalboss_sprite=pygame.image.load("./imagefiles/boss/final_boss.png")
finalboss_dead_sprite1=pygame.image.load("./imagefiles/boss/final_bossdead1.png")
finalboss_dead_sprite2=pygame.image.load("./imagefiles/boss/final_bossdead2.png")
machine=pygame.image.load("./imagefiles/boss/machine.png")
scientist_sprite=pygame.image.load("./imagefiles/npc/scientist.png")
scientist_sprite=pygame.transform.scale(scientist_sprite,(50,110))
scientist_dialog_sprite=pygame.image.load("./imagefiles/dialog/scientist dialog.png")
scientist_dialog_sprite=pygame.transform.scale(scientist_dialog_sprite,(400,200))
robot_sprite=pygame.image.load("./imagefiles/dialog/robot.png")
block_sprite=pygame.image.load("./imagefiles/sprites/block.png")
congrats=pygame.image.load("./imagefiles/sprites/congrats.png")
######Sound files
Rifle_shot=pygame.mixer.Sound('./soundfiles/Rifle_shot.ogg')
Glock_shot=pygame.mixer.Sound('./soundfiles/Glock_shot.ogg')
shotgun_shot=pygame.mixer.Sound('./soundfiles/shotgun_shot.ogg')
no_ammos_gun=pygame.mixer.Sound('./soundfiles/no_ammos.ogg')
no_ammos_suit=pygame.mixer.Sound('./soundfiles/ammo_depleted.ogg')
weapon_reloading_sound=pygame.mixer.Sound('./soundfiles/gun_reload_sound.ogg')
intro_music=pygame.mixer.Sound('./soundfiles/intro_sound.ogg')
health_pack_pickedup=pygame.mixer.Sound('./soundfiles/health_pick.ogg')
ammo_pickup=pygame.mixer.Sound('./soundfiles/ammo_pickup.ogg')
######starting values
weapon_selected=1#Rifle
weapon_speed=12
weapon_cadence=100
player_health=20
weapon_reloading_speed=2010
weapon_shot_sound=Rifle_shot
ab=0
ordo=0
reloading=0
bullets_ally.append(((-700,-200),(0,0),(weapon_speed)))
weapons=[("Melee"),("Rifle",120,2019,Rifle_shot,30,120,300,14,30,no_ammos_gun),("Glock",120,1019,Glock_shot,12,60,100,10,12,no_ammos_gun),("Shotgun",120,3000,shotgun_shot,6,60,100,10,4,no_ammos_gun)]
bullet_total=[weapons[1][5],weapons[2][5],weapons[3][5],weapons[2][5]]
weapon_capacity=[weapons[1][4],weapons[2][4],weapons[3][4]]
bullet_clip=[weapons[1][8],weapons[2][8],weapons[3][8]]
zombot=["enemie","zombot",50,5,12]
soldier_enemy=["enemie","soldier_enemy",100,1,40]
soldier_ally=["ally","soldier_ally",100,5]
rifle_ammunition=("rifle_ammunition",(600,350))
glock_ammunition=("glock_ammunition",(600,350))
player_damagibility=True
entity_enemy=[]
entity_ally=[]
blocks=[]
door_down=("door_lower",(76,displayy/2))
door_up=("door_upper",(displayx-146,displayy/2))
health_pack=("health_pack",(600,350))
entity.append(health_pack)
loading_map=False
actual_level=1
def text_objects(text, font, color):
    textSurface = font.render (text, True, color)
    return textSurface, textSurface.get_rect()
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos ( )
    click = pygame.mouse.get_pressed ( )
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect (fenetre, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action ( )
    else:
        pygame.draw.rect (fenetre, ic, (x, y, w, h))
    smallText = pygame.font.SysFont ("arial", 48)
    textSurf, textRect = text_objects (msg, smallText, (255,255,255))
    textRect.center = ((x +
     (w / 2)), (y + (h / 2)))
    fenetre.blit (textSurf, textRect)

def game_init():
    global player_health,player_position,entity_enemy,bullets_ally,weapons,bullet_total,bullet_clip,reset3,reset4,actual_level,blocks,loading_map,i
    reset3=0
    reset4=0
    reset1=0
    reset2=0
    player_position=(160,displayy/2)
    shooting=0
    i=0
    score=0
    weapon_selected=1
    gaming= False
    instant_direction=1
    weapon_names=["Rifle","Glock","Shotgun"]
    bullets_ally_speed=40
    bullet_reset=0
    player_speed=17
    playerAlive=True
    player_health=100
    bullets_ally=[]
    arial32=pygame.font.SysFont("arial",32)
    moving=False
    main_menu=True
    death_menu=False
    actual_level=1
    bullets_ally.append(((-700,-200),(0,0),(weapon_speed)))
    blocks=[]
    loading_map=False
######starting values
##Game Features:
#weapon_selected[x]=[0]=Name[1]=bullet_speed[2]=weapon_reloading_speed[3]=weapon_shot_sound[4]=magazine_capacity[5]=bullets_total[6]=weapon_cadence[7]=weapon_damage[8]=bullet_clip    bullet_total=[weapons[1][5],weapons[2][5]]
    weapon_capacity=[weapons[1][4],weapons[2][4],weapons[3][4]]
    bullet_clip=[weapons[1][8],weapons[2][8],weapons[3][8]]
    zombot=["enemie","zombot",50,5,12]
    entity_enemy=[]
def summon_door_up():
    global entity
    elv_up=("door_upper",(displayx-146,displayy/2))
    entity.append(elv_up)
def summon_door_down():
    global entity
    elv_down=("door_lower",(76,displayy/2))
    entity.append(elv_down)
def summon_health_pack(absice,ordone):
    global entity
    health_pack=("health_pack",(absice,ordone))
    entity.append(health_pack)
def summon_glock_ammunition(absice,ordone):
    global entity
    glock_ammunition=("glock_ammunition",(absice,ordone))
    entity.append(glock_ammunition)
def summon_npc(entityname,absice,ordone):
    global entity
    entity.append((entityname,(absice,ordone)))
def summon_block(absice,ordone):
    global blocks
    blocks.append(("block",(absice,ordone)))
def summon_ceo(absice,ordone):
    entity.append((("CEO"),(absice,ordone),pygame.time.get_ticks(),False))
def summon_machine(absice,ordone):
    entity.append((("machine"),(absice,ordone)))
def summon_boss(absice,ordone):
    entity_enemy.append((("enemie","finalboss",3000,1,1),(absice,ordone)))
def changing_level(actual_lvl):
    global entity_enemy,loading_map,entity_ally,actual_level,player_position,entity,background,background_full,blocks,bullets_ally,bullet_enemy,reset10
    entity_enemy=[]
    entity_ally=[]
    entity=[]
    bullets_ally=[]
    blocks=[]
    bullet_enemy=[]
    bullets_ally.append(((-700,-200),(0,0),(weapon_speed)))
    if actual_lvl==1:
        fichier = open("./maps/lvl1.txt", "r")
        background_full=pygame.image.load("./imagefiles/sprites/background lvl1.png")
        background=pygame.image.load("./imagefiles/sprites/background lvl1.png")
    if actual_lvl==2:
        fichier = open("./maps/lvl2.txt", "r")
        background_full=background_full2
        background=background2
    if actual_lvl==3:
        fichier = open("./maps/lvl3.txt", "r")
        i=0
        background=background3
    if actual_lvl==4:
        fichier = open("./maps/lvl4.txt", "r")
        background=background2
    if actual_lvl==5:
        fichier = open("./maps/lvl5.txt", "r")
        background=background2
    if actual_lvl==6:
        fichier = open("./maps/lvl6.txt", "r")
    if actual_lvl==7:
        fichier = open("./maps/lvl-finalboss.txt", "r")
        background=background2
        reset10=pygame.time.get_ticks()
    ligne = fichier.readlines()
    for x in range(0,len(ligne)//4):
        repere=x*4
        c=str(ligne[repere])
        a=int(ligne[repere+1])
        b=int(ligne[repere+2])
        if c=="zombie\n":
            summon_zombie(a,b)
        if c=="soldier_ally\n":
            summon_soldier_ally(a,b)
        if c=="soldier_enemy\n":
            summon_soldier_enemy(a,b)
        if c=="door_upper\n":
            summon_door_up()
        if c=="door_lower\n":
            summon_door_down()
        if c=="health_pack\n":
            summon_health_pack(a,b)
        if c=="rifle_ammunition\n":
            summon_rifle_ammunition(a,b)
        if c=="glock_ammunition\n":
            summon_glock_ammunition(a,b)
        if c=="npc_scientist\n":
            summon_npc("scientist",a,b)
        if c=="block\n":
            summon_block(a,b)
        if c=="CEO\n":
            summon_ceo(a,b)
        if c=="machine\n":
            summon_machine(a,b)
        if c=="finalboss\n":
            summon_boss(actualx/2-105,b)
    fichier.close()
    loading_map=True
    player_position =(160,displayy/2)
    pygame.mouse.set_visible(False)
def summon_soldier_enemy(x,y):
    global entity_enemy
    entity_enemy.append(((soldier_enemy),(x,y),0,0))
def summon_rifle_ammunition(x,y):
    global entity
    rifle_ammunition_box=("rifle_ammunition",(x,y))
    entity.append(rifle_ammunition_box)
def summon_soldier_ally(x,y):
    global entity_ally
    entity_ally.append((soldier_ally,(x,y),0,0))
def summon_zombie(x,y):
    global zombot,entity_enemy
    zombot=["enemie","zombot",50,5,12]
    entity_enemy.append(((zombot),(x,y)))
def shooting(weapon_selected,position_bullet,ab,ordo):
    global bullets_ally,bullets
    weapon_shot_sound=weapons[weapon_selected][3]
    if weapon_selected!=3:
        ab+=randint(-50,50)
        ordo+=randint(-50,50)
        bullets_ally.append((position_bullet,(ab,ordo),weapon_selected))
    if weapon_selected==3:
        ab=(ab/2)-75
        ordo=(ordo/2)-75
        for x in range(0,5):
            ab=ab+20
            ordo=ordo+20
            bullets_ally.append((position_bullet,(ab,ordo),weapon_selected))
    pygame.mixer.Sound.play(weapon_shot_sound)
def shooting_enemy(weapon_selected,position_bullet,ab,ordo):
    global bullets_ally,bullet_enemy
    weapon_shot_sound=Glock_shot
    ab=ab+randint(-100,100)
    ordo=ordo+randint(-100,100)
    bullet_enemy.append((position_bullet,(ab,ordo),weapon_selected))
    pygame.mixer.Sound.set_volume(weapon_shot_sound,0.4)
    pygame.mixer.Sound.play(weapon_shot_sound)
def reloading(weapon_selected):
    s=weapon_selected-1
    if bullet_total[s]>0 and bullet_total[s]>=(weapon_capacity[s]-bullet_clip[s]) and bullet_clip[s]!=weapon_capacity[s] and weapon_selected!=3:
        bullet_total[s]=bullet_total[s]-(weapon_capacity[s]-bullet_clip[s])
        bullet_clip[s]=bullet_clip[s]+((weapon_capacity[s]-bullet_clip[s]))
        pygame.mixer.Sound.play(weapon_reloading_sound)
    if bullet_total[s]>0 and bullet_total[s]>=(weapon_capacity[s]-bullet_clip[s]) and bullet_clip[s]!=weapon_capacity[s] and weapon_selected==3:
        bullet_total[s]=bullet_total[s]-1
        bullet_clip[s]=bullet_clip[s]+1
        pygame.mixer.Sound.play(weapon_reloading_sound)
    elif bullet_total[s]>0 and bullet_total[s]<=(weapon_capacity[s]-bullet_clip[s]) and weapon_selected!=3:
        bullet_clip[s]=bullet_clip[s]+bullet_total[s]
        bullet_total[s]=0
    if bullet_total[s]==0:
        pygame.mixer.Sound.play(no_ammos_suit)
def moving_entity_enemy():
    global player_position,entity_enemy
    #entity[l]=(entity[l][0],entity[l][1],pygame.time.get_ticks(),entity[l][3])
    for d in range(0,len(entity_enemy)):
            entity_enemy_speed=2
            health_enemy=entity_enemy[d][0][2]
            if entity_enemy[d][0][1]=="zombot":
                entity_enemy_speed=5
            if entity_enemy[d][0][1]=='soldier_enemy':
                entity_enemy_speed=2
            if health_enemy>0:
                if player_position[0]-entity_enemy[d][1][0]>0:
                    entity_enemy[d]=entity_enemy[d][0],(entity_enemy[d][1][0]+entity_enemy_speed,entity_enemy[d][1][1])
                if player_position[0]-entity_enemy[d][1][0]<0:
                    entity_enemy[d]=entity_enemy[d][0],(entity_enemy[d][1][0]-entity_enemy_speed,entity_enemy[d][1][1])
                if player_position[1]-entity_enemy[d][1][1]>0:
                    entity_enemy[d]=entity_enemy[d][0],(entity_enemy[d][1][0],entity_enemy[d][1][1]+entity_enemy_speed)
                if player_position[1]-entity_enemy[d][1][1]<0:
                    entity_enemy[d]=entity_enemy[d][0],(entity_enemy[d][1][0],entity_enemy[d][1][1]-entity_enemy_speed)
            for m in range(0,len(blocks)):
                if abs(entity_enemy[d][1][1]+entity_enemy_speed-blocks[m][1][1])<=30 and abs(entity_enemy[d][1][1]+entity_enemy_speed-blocks[m][1][1])<=30:
                    entity_enemy[d]=entity_enemy[d][0],(entity_enemy[d][1][0],entity_enemy[d][1][1]-entity_enemy_speed)
def logique_collision():
    global player_health,player_position,player_damagibility,reset3,entity_enemy,actual_level,loading_map,time,weapons,bullet_total
    for a in range (0,len(entity_enemy)):
        for b in range(0,len(bullets_ally)):
            if entity_enemy[a][0][1]=="zombot":
                damage_toplayer=damage_toplayer=randint(5,entity_enemy[a][0][4])
            if entity_enemy[a][0][1]=="soldier_enemy":
                damage_toplayer=randint(20,entity_enemy[a][0][4])
            if entity_enemy[a][0][1]=="finalboss":
                damage_toplayer=randint(2,6)
            damage_byplayer=weapons[weapon_selected][7]+randint(weapons[weapon_selected][7]-5,weapons[weapon_selected][7]+5)
            entity_enemy_x=entity_enemy[a][1][0]
            entity_enemy_y=entity_enemy[a][1][1]
            entity_name=entity_enemy[a][0][1]
            if abs(bullets_ally[b][0][0]-entity_enemy_x)<=40 and abs(bullets_ally[b][0][1]-entity_enemy_y)<=64 and entity_enemy[a][0][2]>0 and entity_enemy[a][0][2]-damage_byplayer>0 and entity_name!='finalboss':
                entity_enemy[a]=((entity_enemy[a][0][0],entity_enemy[a][0][1],entity_enemy[a][0][2]-damage_byplayer,entity_enemy[a][0][3],entity_enemy[a][0][4]),entity_enemy[a][1])
                time.append((pygame.time.get_ticks(),(bullets_ally[b][0][0],bullets_ally[b][0][1])))
                bullets_ally[b]=((-700,-400),(0,0),0)
                fenetre.blit(blood_sprite,(entity_enemy_x,entity_enemy_y))
            elif abs(bullets_ally[b][0][0]-entity_enemy_x)<=40 and abs(bullets_ally[b][0][1]-entity_enemy_y)<=64 and entity_enemy[a][0][2]>0 and entity_enemy[a][0][2]-damage_byplayer<=0 and entity_name!='finalboss':
                entity_enemy[a]=((entity_enemy[a][0][0],entity_enemy[a][0][1],entity_enemy[a][0][2]-damage_byplayer,entity_enemy[a][0][3],entity_enemy[a][0][4]),entity_enemy[a][1])
                time.append((pygame.time.get_ticks(),(bullets_ally[b][0][0],bullets_ally[b][0][1])))
                fenetre.blit(blood_sprite,(bullets_ally[b][0][0],bullets_ally[b][0][1]))
            if abs(bullets_ally[b][0][0]-entity_enemy_x)<=40 and abs(bullets_ally[b][0][1]-entity_enemy_y)<=64 and entity_enemy[a][0][2]>0 and entity_enemy[a][0][2]-damage_byplayer<=0 and entity_name!='finalboss':
                entity_enemy[a]=((entity_enemy[a][0][0],entity_enemy[a][0][1],entity_enemy[a][0][2]-damage_byplayer,entity_enemy[a][0][3],entity_enemy[a][0][4]),entity_enemy[a][1])
                fenetre.blit(blood_sprite,(bullets_ally[b][0][0],bullets_ally[b][0][1]))
            if 0<bullets_ally[b][0][0]-entity_enemy_x<=300 and 0<bullets_ally[b][0][1]-entity_enemy_y<=200 and entity_enemy[a][0][2]>0 and entity_name=='finalboss':
                time.append((pygame.time.get_ticks(),(bullets_ally[b][0][0],bullets_ally[b][0][1])))
                bullets_ally[b]=((-700,-400),(0,0),0)
                entity_enemy[a]=((entity_enemy[a][0][0],entity_enemy[a][0][1],entity_enemy[a][0][2]-damage_byplayer,entity_enemy[a][0][3],entity_enemy[a][0][4]),entity_enemy[a][1])
            if entity_enemy[a][0][2]<=0:
                entity_enemy[a]=((entity_enemy[a][0][0],entity_enemy[a][0][1],0,entity_enemy[a][0][3],entity_enemy[a][0][4]),entity_enemy[a][1],randint(0,4))
            if abs(player_position[0]-entity_enemy_x)<=39  and entity_enemy[a][0][2]>0 and abs(player_position[1]-entity_enemy_y)<=82 and player_damagibility==True:
                player_damagibility=False
                player_health=player_health-damage_toplayer
                reset3=pygame.time.get_ticks()
    for p in range(0,len(entity)):
        ab=entity[p][1][0]
        ordo=entity[p][1][1]
        if abs(player_position[0]-ab)<=80 and abs(player_position[1]-ordo)<=80 and entity[p][0]=="health_pack":
            player_health=player_health+50
            entity[p]=entity[p][0],(-700,0)
            pygame.mixer.Sound.play(health_pack_pickedup)
        if abs(player_position[0]-ab)<=80 and abs(player_position[1]-ordo)<=80 and entity[p][0]=="door_upper":
            actual_level+=1
            loading_map=False
            player_position = (100,displayy/2)
        if abs(player_position[0]-ab)<=80 and abs(player_position[1]-ordo)<=80 and entity[p][0]=="door_lower":
            actual_level-=1
            loading_map=False
            player_position = (800,displayy/2)
        if abs(player_position[0]-ab)<=80 and abs(player_position[1]-ordo)<=80 and entity[p][0]=="rifle_ammunition":
            bullet_total=[bullet_total[0]+60,bullet_total[1],bullet_total[2]]
            entity[p]=entity[p][0],(-700,0)
            pygame.mixer.Sound.play(ammo_pickup)
        if abs(player_position[0]-ab)<=80 and abs(player_position[1]-ordo)<=80 and entity[p][0]=="glock_ammunition":
            bullet_total=[bullet_total[0],bullet_total[1]+60,bullet_total[2]]
            entity[p]=entity[p][0],(-700,0)
            pygame.mixer.Sound.play(ammo_pickup)
    for u in range(0,len(bullet_enemy)):
        bulletx,bullety=bullet_enemy[u][0][0],bullet_enemy[u][0][1]
        playerx,playery=player_position[0],player_position[1]
        if 0<abs(bulletx-playerx)<=50 and 0<abs(bullety-playery)<=88:
            bullet_enemy[u]=[(-600,-700),(0,0)]
            player_health-=10
            player_damagibility=False
            player_health=player_health-damage_toplayer
            reset3=pygame.time.get_ticks()
def moving_entity_ally():
    global entity_ally,i
    for o in range(0,len(entity_ally)):
        speed_ally=entity_ally[o][0][3]
        positionx_ally=entity_ally[o][1][0]
        positiony_ally=entity_ally[o][1][1]
        entity_health_ally=entity_ally[o][0][2]
        speed_enemy=entity_enemy[i][0][3]
        positionx_enemy=entity_enemy[i][1][0]
        positiony_enemy=entity_enemy[i][1][1]
        entity_health_enemy=entity_enemy[i][0][2]
        if entity_health_ally>0 and entity_health_enemy>0:
                if positionx_ally-positionx_enemy> 100:
                    entity_ally[o]=entity_ally[o][0],(entity_ally[o][1][0]-speed_ally,entity_ally[o][1][1]),entity_ally[o][2],entity_ally[o][3]
                if positionx_ally-positionx_enemy< -100:
                    entity_ally[o]=entity_ally[o][0],(entity_ally[o][1][0]+speed_ally,entity_ally[o][1][1]),entity_ally[o][2],entity_ally[o][3]
                if positiony_ally-positiony_enemy>100:
                    entity_ally[o]=entity_ally[o][0],(entity_ally[o][1][0],entity_ally[o][1][1]-speed_ally),entity_ally[o][2],entity_ally[o][3]
                if positiony_ally-positiony_enemy< 100:
                    entity_ally[o]=entity_ally[o][0],(entity_ally[o][1][0],entity_ally[o][1][1]+speed_ally),entity_ally[o][2],entity_ally[o][3]
    for p in range(0,len(entity_ally)):
            for m in range(0,len(entity_ally)):
                positionx_ally=entity_ally[p][1][0]
                positiony_ally=entity_ally[p][1][1]
                positionx_ally_other=entity_ally[m][1][0]
                positiony_ally_other=entity_ally[m][1][1]
                if positionx_ally-positionx_ally_other>0 and positionx_ally-positionx_ally_other<60:
                    entity_ally[p]=entity_ally[p][0],(entity_ally[p][1][0]+6,entity_ally[p][1][1]),entity_ally[p][2],entity_ally[p][3]
def logique_AI():
    global entity_ally,bullets_ally,i,reset8
    for u in range(0,len(entity_ally)):
        for z in range(0,len(entity_enemy)):
            speed_enemy=entity_enemy[i][0][3]
            positionx_enemy=entity_enemy[i][1][0]
            positiony_enemy=entity_enemy[i][1][1]
            entity_health_enemy=entity_enemy[i][0][2]
            speed_ally=entity_ally[u][0][3]
            positionx_ally=entity_ally[u][1][0]
            positiony_ally=entity_ally[u][1][1]
            entity_health_ally=entity_ally[u][0][2]
            name_enemy=entity_enemy[z][0][1]
            ab=positionx_enemy-positionx_ally
            ordo=positiony_enemy-positiony_ally
            reset5=entity_ally[u][0][3]
            if entity_health_ally>0 and entity_health_enemy>0 and pygame.time.get_ticks()-entity_ally[u][3]>=500:
                shooting(2,(positionx_ally,positiony_ally),ab,ordo)
                entity_ally[u]=entity_ally[u][0],(entity_ally[u][1][0],entity_ally[u][1][1]),entity_ally[u][2],pygame.time.get_ticks()
            if entity_health_enemy>0 and pygame.time.get_ticks()-reset8>1000 and name_enemy=='soldier_enemy':
                ab=player_position[0]-positionx_enemy
                ordo=player_position[0]-positiony_enemy
                shooting_enemy(1,(positionx_enemy,positiony_enemy),ab,ordo)
                reset8=pygame.time.get_ticks()
    for p in range(0,len(entity_enemy)):
        name_enemy=entity_enemy[p][0][1]
        positionx_enemy=entity_enemy[p][1][0]
        positiony_enemy=entity_enemy[p][1][1]
        dispersionx=randint(-100,100)
        dispersiony=randint(-100,100)
        anglex=positionx_enemy-player_position[0]
        angley=positiony_enemy-player_position[1]
        if name_enemy=='soldier_enemy' and entity_enemy[p][0][2]>0 and pygame.time.get_ticks()-entity_enemy[p][0][3]>=1000:
            shooting_enemy(1,(positionx_enemy,positiony_enemy),anglex+dispersionx,angley+dispersiony)
            entity_enemy[p]=(entity_enemy[p][0][0],entity_enemy[p][0][1],entity_enemy[p][0][2],pygame.time.get_ticks(),entity_enemy[p][0][4]),(entity_enemy[p][1][0],entity_enemy[p][1][1])
def moving_boss():
    global reset10
    if 0<pygame.time.get_ticks()-reset10<=5000:
        entity_enemy[0]=entity_enemy[0][0],(entity_enemy[0][1][0],entity_enemy[0][1][1]+2)
    if 5000<pygame.time.get_ticks()-reset10<10000:
        entity_enemy[0]=entity_enemy[0][0],(entity_enemy[0][1][0],entity_enemy[0][1][1]-2)
    if 10000<pygame.time.get_ticks()-reset10<=15000:
        entity_enemy[0]=entity_enemy[0][0],(entity_enemy[0][1][0]+2,entity_enemy[0][1][1])
    if 15000<pygame.time.get_ticks()-reset10<20000:
        entity_enemy[0]=entity_enemy[0][0],(entity_enemy[0][1][0]-2,entity_enemy[0][1][1])
    if pygame.time.get_ticks()-reset10>=20000:
        reset10=pygame.time.get_ticks()
def logique_AI_boss():
    if pygame.time.get_ticks()-reset10>=500 and randint(0,100)<=20:
        shooting_enemy(1,(entity_enemy[0][1][0],entity_enemy[0][1][1]+250),0,-500)
        shooting_enemy(1,(entity_enemy[0][1][0]+300,entity_enemy[0][1][1]+250),0,-500)
        shooting_enemy(1,(entity_enemy[0][1][0],entity_enemy[0][1][1]+250),-500,500)
        shooting_enemy(1,(entity_enemy[0][1][0]+300,entity_enemy[0][1][1]+250),500,500)
        shooting_enemy(1,(entity_enemy[0][1][0],entity_enemy[0][1][1]+250),-500,0)
        shooting_enemy(1,(entity_enemy[0][1][0]+300,entity_enemy[0][1][1]+250),500,0)
    #for o in range(0,len(bullet_enemy)):

def logiqueDuJeu():
    global i,player_damagibility,playerAlive,playerlifes,bullets,bullets_ally,bullets_ally_speed,player_position,player_health,death_menu,gaming,playerAlive,main_menu,death_menu,gaming,actual_level,loading_map,endmenu
    if loading_map==False:
        changing_level(actual_level)
    if actual_level!=7:
        moving_entity_enemy()
    logique_collision()
    logique_AI()
    if cycle>=25:
        endmenu=True
        gaming=False
    if actual_level==7 and entity_enemy[0][0][2]>0:
        moving_boss()
        logique_AI_boss()
    if entity_enemy!=[]:
        moving_entity_ally()
    if actual_level==5:
        now=0
        for p in range(0,len(entity_enemy)):
            if entity_enemy[p][0][2]<=0:
                now+=1
        if now==len(entity_enemy):
            actual_level+=1
            loading_map=False
    for a in range(0,len(entity_enemy)):
        if entity_enemy[a][0][2]>0:
            moving_entity_ally()
            i=a
    for f in range(0,len(entity)):
        if entity[f][0]=='CEO' and entity[f][3]==True:
                entity[f]=(entity[f][0],(entity[f][1][0],entity[f][1][1]+7),entity[f][2],entity[f][3])
        if entity[f][1][1]>=450:
            actual_level+=1
            loading_map=False
    for z in range(0,len(bullets_ally)):
        argx=bullets_ally[z][1][0]
        argy=bullets_ally[z][1][1]
        posi_bullet_x=bullets_ally[z][0][0]
        posi_bullet_y=bullets_ally[z][0][1]
        if argx>0 and argy>0:
            bullets_ally[z]=((posi_bullet_x+bullets_ally_speed*atan(argx/argy),posi_bullet_y+bullets_ally_speed*atan(argy/argx)),(argx,argy))
        if argx<0 and argy>0:
            bullets_ally[z]=((posi_bullet_x+bullets_ally_speed*atan(argx/argy),posi_bullet_y-bullets_ally_speed*atan(argy/argx)),(argx,argy))
        if argx>0 and argy<0:
            bullets_ally[z]=((posi_bullet_x-bullets_ally_speed*atan(argx/argy),posi_bullet_y+bullets_ally_speed*atan(argy/argx)),(argx,argy))
        if argx<0 and argy<0:
            bullets_ally[z]=((posi_bullet_x-bullets_ally_speed*atan(argx/argy),posi_bullet_y-bullets_ally_speed*atan(argy/argx)),(argx,argy))
        if argx==0:
            bullets_ally[z]=((posi_bullet_x-bullets_ally_speed*1,posi_bullet_y-bullets_ally_speed*0),(argx,argy))
        if argy==0:
            bullets_ally[z]=((posi_bullet_x-bullets_ally_speed*1,posi_bullet_y-bullets_ally_speed*0),(argx,argy))
    for p in range (0,len(bullet_enemy)):
        arx=bullet_enemy[p][1][0]
        ary=bullet_enemy[p][1][1]
        posibullet_x=bullet_enemy[p][0][0]
        posibullet_y=bullet_enemy[p][0][1]
        if arx==0:
            bullet_enemy[p]=((posibullet_x-bullets_ally_speed*1,posibullet_y-bullets_ally_speed*0),(arx,ary))
        if ary==0:
            bullet_enemy[p]=((posibullet_x-bullets_ally_speed*1,posibullet_y-bullets_ally_speed*0),(arx,ary))
        if arx>0 and ary>0:
            bullet_enemy[p]=((posibullet_x-bullets_ally_speed*atan(arx/ary),posibullet_y-bullets_ally_speed*atan(ary/arx)),(arx,ary))
        if arx<0 and ary>0:
            bullet_enemy[p]=((posibullet_x-bullets_ally_speed*atan(arx/ary),posibullet_y+bullets_ally_speed*atan(ary/arx)),(arx,ary))
        if arx>0 and ary<0:
            bullet_enemy[p]=((posibullet_x+bullets_ally_speed*atan(arx/ary),posibullet_y-bullets_ally_speed*atan(ary/arx)),(arx,ary))
        if arx<0 and ary<0:
            bullet_enemy[p]=((posibullet_x+bullets_ally_speed*atan(arx/ary),posibullet_y+bullets_ally_speed*atan(ary/arx)),(arx,ary))
    if player_health<=0:
        main_menu=True
        gaming=False
        game_init()
        the_game()
    if pygame.time.get_ticks()-reset3>=700:
        player_damagibility=True
def dessiner():
    global blood_sprite,time,entity_ally,reset4,player_health,enemie,reset2,player_moving_left,player_moving2_left,player_moving_right,player_moving2_right,bullet,imageVaisseau, fenetre, projectile,score,player_position,player_sprite,shotgun,background,weapon_names,moving,player_not_moving,reset11,cycle
    fenetre.fill( (0,0,0) )# On remplit complÃƒÂ¨tement notre fenÃƒÂªtre avec la couleur noire: (0,0,0)
    fenetre.blit(background,(0,0))
    if fullscreen==True:
        fenetre.blit(background_full,(0,0))
    if fullscreen==False:
        fenetre.blit(background,(0,0))
    for x in range(0,len(bullets_ally)):#dessine chaque image
            if bullets_ally[x][0][0]>0 and bullets_ally[x][0][0]<pygame.display.list_modes()[3][0] and bullets_ally[x][0][1]>0 and bullets_ally[x][0][1]<pygame.display.list_modes()[3][1]:
                fenetre.blit(bullet,bullets_ally[x][0])
    bullet_total_selected=arial32.render(str(bullet_total[weapon_selected-1]),True,pygame.Color(255,255,255))
    bullet_clip_selected=arial32.render(str(bullet_clip[weapon_selected-1]),True,pygame.Color(255,255,255))
    weapon_name=arial32.render(str(weapon_names[weapon_selected-1]),True,pygame.Color(255,0,0))
    health=arial32.render(str(player_health),True,pygame.Color(255,255,255))
    slash=arial32.render("/",True,pygame.Color(255,255,255))
    fenetre.blit(weapon_name,(0,30))
    fenetre.blit(bullet_clip_selected,(80,30))
    fenetre.blit(bullet_total_selected,(120,30))
    fenetre.blit(slash,(110,30))
    fenetre.blit(health,(300,30))
    if actual_level==1:
        fenetre.blit(robot_sprite,(1109,112))
        fenetre.blit(scientist_sprite,(839,105))
        fenetre.blit(scientist_dialog_sprite,(457,106))
    for h in range(0,len(bullet_enemy)):
        fenetre.blit(bullet_enemy_sprite,(bullet_enemy[h][0]))
    for l in range(0,len(entity)):
        if entity[l][0]=="health_pack":
            fenetre.blit(health_pack_sprite,entity[l][1])
        if entity[l][0]=="door_lower":
            fenetre.blit(door_low_sprite,entity[l][1])
        if entity[l][0]=="door_upper":
            fenetre.blit(door_up_sprite,entity[l][1])
        if entity[l][0]=="rifle_ammunition":
            fenetre.blit(rifle_ammunition_sprite,entity[l][1])
        if entity[l][0]=="glock_ammunition":
            fenetre.blit(glock_ammunition_sprite,entity[l][1])
        if entity[l][0]=="scientist":
            fenetre.blit(scientist_sprite,entity[l][1])
        if entity[l][0]=="CEO" and entity[l][3]==False:
            fenetre.blit(boss_zero_suit_standing,entity[l][1])
        if entity[l][0]=="CEO" and entity[l][3]==False and pygame.time.get_ticks()-entity[l][2]>=2000:
            entity[l]=(entity[l][0],entity[l][1],pygame.time.get_ticks(),True)
        if entity[l][0]=="CEO" and pygame.time.get_ticks()-entity[l][2]<=200 and entity[l][3]==True:
            fenetre.blit(boss_zero_suit_walking1,entity[l][1])
        if entity[l][0]=="CEO" and 200<pygame.time.get_ticks()-entity[l][2]<=400 and entity[l][3]==True:
            fenetre.blit(boss_zero_suit_walking2,entity[l][1])
            entity[l]=(entity[l][0],entity[l][1],pygame.time.get_ticks(),entity[l][3])
        if entity[l][0]=="machine":
            fenetre.blit(machine,entity[l][1])
    for j in range(0,len(blocks)):
            fenetre.blit(block_sprite,blocks[j][1])
    for z in range(0,len(entity_enemy)):
        if entity_enemy[z][0][2]>0 and entity_enemy[z][0][1]=="zombot":
            fenetre.blit(enemie,entity_enemy[z][1])
        if entity_enemy[z][0][2]<=0 and  entity_enemy[z][0][1]=="zombot" and int(z%2)==0:
            fenetre.blit(enemie_dead,entity_enemy[z][1])
        if entity_enemy[z][0][2]<=0 and  entity_enemy[z][0][1]=="zombot" and int(z%2)!=0:
            fenetre.blit(enemie_dead2,entity_enemy[z][1])
        if entity_enemy[z][0][2]>0 and entity_enemy[z][0][1]=="soldier_enemy":
            fenetre.blit(soldier_enemy_sprite,entity_enemy[z][1])
        if entity_enemy[z][0][2]<=0 and entity_enemy[z][0][1]=="soldier_enemy" and int(z%2)==0:
            fenetre.blit(soldier_enemy_dead_sprite,entity_enemy[z][1])
        if entity_enemy[z][0][2]<=0 and entity_enemy[z][0][1]=="soldier_enemy" and int(z%2)!=0:
            fenetre.blit(soldier_enemy_dead_sprite2,entity_enemy[z][1])
        if entity_enemy[z][0][1]=="finalboss" and entity_enemy[z][0][2]>0:
            fenetre.blit(finalboss_sprite,entity_enemy[z][1])
        if entity_enemy[z][0][1]=="finalboss" and entity_enemy[z][0][2]<=0 and pygame.time.get_ticks()-reset11<=250:
            fenetre.blit(finalboss_dead_sprite1,entity_enemy[z][1])
        if entity_enemy[z][0][1]=="finalboss" and entity_enemy[z][0][2]<=0 and 250<=pygame.time.get_ticks()-reset11:
            fenetre.blit(finalboss_dead_sprite2,entity_enemy[z][1])
        if pygame.time.get_ticks()-reset11>=500 and entity_enemy[z][0][1]=="finalboss" and entity_enemy[z][0][2]<=0:
            reset11=pygame.time.get_ticks()
            cycle+=1
    for l in range(0,len(entity_ally)):
        if entity_ally[l][0][2]>0:
            fenetre.blit(soldier_ally_sprite,entity_ally[l][1])
    if player_damagibility==True:
        blit_player()
    if player_damagibility==False :
        if pygame.time.get_ticks()-reset4<=100:
            blit_player()
        if pygame.time.get_ticks()-reset4>=200:
            reset4=pygame.time.get_ticks()
    for p in range(0,len(time)):
        if pygame.time.get_ticks()-time[p][0]<=300:
            fenetre.blit(blood_sprite,(time[p][1][0],time[p][1][1]))
        if pygame.time.get_ticks()-time[p][0]>=300 and pygame.time.get_ticks()-time[p][0]<=500:
            fenetre.blit(blood2_sprite,(time[p][1][0],time[p][1][1]))
    fenetre.blit(crossair_sprite,(pygame.mouse.get_pos()[0]-7,pygame.mouse.get_pos()[1]-7))
    pygame.display.flip()
def findAngle(pos):
    sX = player_position[0]
    sY = player_position[1]
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2
    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi*2) - angle
    return angle
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
def blit_player():
    global reset2
    positionx,positiony=player_position[0]-10,player_position[1]
    if weapon_selected==1:
        weapon_sprite=rifle_sprite_original
        positionx-=15
        positiony-=10
    if weapon_selected==2:
        weapon_sprite=pistol_sprite_original
    if weapon_selected==3:
        weapon_sprite=shotgun_sprite_original
    pos =pygame.mouse.get_pos()
    angle = int((math.degrees(findAngle(pos)))/math.pi)
    if angle==28:
        angle=30
    if angle==86:
        angle=87
    if angle==29:
        angle=26
    if 0<=angle<30 or 88<=angle<144:
        weapon_sprite=rot_center(weapon_sprite,angle*math.pi)
    else:
        weapon_sprite=pygame.transform.flip(weapon_sprite,0,1)
        weapon_sprite=rot_center(weapon_sprite,angle*math.pi)
    if 0<=angle<57:
        fenetre.blit(weapon_sprite,(positionx,positiony))
    pygame.draw.line(fenetre,(255,255,255),(player_position[0]+30,player_position[1]+30),pygame.mouse.get_pos())
    if 0<=angle<60:
        fenetre.blit(player_back_sprite,(player_position[0]-5,player_position[1]-5))
    if 60<=angle<=114:
        fenetre.blit(player_sprite,(player_position[0]-5,player_position[1]-5))
    if moving==False:
        fenetre.blit(player_not_moving,(player_position[0],player_position[1]+41))
    if moving==True and pygame.time.get_ticks()-reset2>=300 and instant_direction==1:
        if pygame.time.get_ticks()-reset2>=600:
            reset2=pygame.time.get_ticks()
        fenetre.blit(player_moving_left,(player_position[0],player_position[1]+41))
    if moving==True and pygame.time.get_ticks()-reset2<=300 and instant_direction==1:
        fenetre.blit(player_moving2_left,(player_position[0]-10,player_position[1]+41))
    if moving==True and pygame.time.get_ticks()-reset2>=300 and instant_direction==2:
        if pygame.time.get_ticks()-reset2>=600:
            reset2=pygame.time.get_ticks()
        fenetre.blit(player_moving_right,(player_position[0],player_position[1]+41))
    if moving==True and pygame.time.get_ticks()-reset2<=300 and instant_direction==2:
        fenetre.blit(player_moving2_right,(player_position[0]-10,player_position[1]+41))
    if 58<=angle<114:
        fenetre.blit(weapon_sprite,(positionx,positiony))
def gererClavierEtSouris():
    global reset7,fullscreen,actualy,actualx,reset6,moving,instant_direction,reset1,weapon_shot_sound,weapon_cadence,weapon_reloading_speed,gaming,reloading, player_position, projectile,shooting,bullets,laserSound,shotgun,bullet_reset,bullet_glock_clip,bullet_glock_total,player_speed,weapon_selected,bullet_clip
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gÃƒÂ©rer un clic sur le bouton de fermeture de la fenÃƒÂªtre
            gaming = False
    argx=bullets_ally[-1][1][0]
    argy=bullets_ally[-1][1][1]
    touchesPressees = pygame.key.get_pressed()
    if pygame.mouse.get_pressed()[0]==1 and pygame.time.get_ticks()-bullet_reset>=weapon_cadence and bullet_clip[weapon_selected-1]>0 and actual_level!=1 and actual_level!=6:#left click
        bullet_clip[weapon_selected-1]=bullet_clip[weapon_selected-1]-1
        ab=pygame.mouse.get_pos()[0]-player_position[0]
        ordo=pygame.mouse.get_pos()[1]-player_position[1]
        position=[player_position[0]+30,player_position[1]+30]
        shooting(weapon_selected,position,ab,ordo)
        bullet_reset=pygame.time.get_ticks()
    if pygame.mouse.get_pressed()[0]==1 and pygame.time.get_ticks()-bullet_reset>=weapon_cadence and bullet_clip[weapon_selected-1]==0:
        pygame.mixer.Sound.play(no_ammos_gun)
        bullet_reset=pygame.time.get_ticks()
    if pygame.mouse.get_pressed()[2]==1 and pygame.time.get_ticks()-reset6>=300:
        reset6=pygame.time.get_ticks()
        summon_soldier_enemy(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    if touchesPressees[pygame.K_d] == True:
            instant_direction=2
            moving=True
            if player_position[0]<=actualx:
                player_position = ( player_position[0] + player_speed , player_position[1] )
    if touchesPressees[pygame.K_a] == True:
            instant_direction=1
            moving=True
            if player_position[0]>=76:
                player_position = ( player_position[0] - player_speed , player_position[1] )
    if touchesPressees[pygame.K_s] == True:
            moving=True
            if player_position[1]<=560:
                player_position = ( player_position[0], player_position[1] +player_speed )
    if touchesPressees[pygame.K_w] == True:
            moving=True
            if player_position[1]>=110:
                player_position = ( player_position[0], player_position[1] -player_speed )
    if touchesPressees[pygame.K_f] == True:
        if pygame.time.get_ticks()-reset7>=500 and fullscreen==False:
            pygame.display.toggle_fullscreen()
            pygame.display.set_mode(pygame.display.list_modes()[0],pygame.FULLSCREEN)
            displayx=pygame.display.list_modes()[0][0]
            displayy=pygame.display.list_modes()[0][1]
            start_menu_postion=((displayx-140)/2,displayy/2-100)
            actualx=displayx-(76*2)
            actualy=displayy-(103*2)
            reset7=pygame.time.get_ticks()
            fullscreen=True
        else:
            fullscreen==False
    if touchesPressees[pygame.K_s] == False and touchesPressees[pygame.K_w] == False and touchesPressees[pygame.K_a] == False and touchesPressees[pygame.K_d] == False:
         moving=False
    if touchesPressees[pygame.K_ESCAPE] == True:
        pygame.QUIT # Permet de gÃƒÂ©rer un clic sur le bouton de fermeture de la fenÃƒÂªtre
        gaming =False
    if touchesPressees[pygame.K_r] == True and pygame.time.get_ticks()-reset1>=weapon_reloading_speed and pygame.mouse.get_pressed()[0]!=1:
        reset1=pygame.time.get_ticks()
        reloading(weapon_selected)
    if touchesPressees[pygame.K_1] == True:
        weapon_selected=1#rifle
        weapon_speed=12
        weapon_cadence=100
        weapon_reloading_speed=400
        weapon_shot_sound=Rifle_shot
    if touchesPressees[pygame.K_2] == True:
        weapon_selected=2#glock
        weapon_speed=10
        weapon_cadence=350
        weapon_reloading_speed=200
        weapon_shot_sound=Glock_shot
    if touchesPressees[pygame.K_3] == True:
        weapon_selected=3#shotgun
        weapon_speed=10
        weapon_cadence=1000
        weapon_reloading_speed=700
        weapon_shot_sound=Glock_shot
def start_game():
    global gaming,death_menu,main_menu
    gaming=True
    death_menu=False
    main_menu=False
    game_init()
    pygame.mixer.pause()
    the_game()
def quit_game():
    global gaming,death_menu,main_menu
    gaming=False
    death_menu=False
    main_menu=False
def pause_game():
    global gaming,death_menu,main_menu
    death_menu=True
    gaming=False
    main_menu=False
def menu_dessin():
    global main_menu,gaming,start_menu_postion
    positionx=pygame.mouse.get_pos()[0]
    postiony=pygame.mouse.get_pos()[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gÃƒÂ©rer un clic sur le bouton de fermeture de la fenÃƒÂªtre
            gaming = False
            main_menu=False
            death_menu=False
    fenetre.fill( (0,0,0) )
    width=200
    heigh=100
    fenetre.blit(main_screen_sprite,(0,0))
    button("Start",(actualx)/2,actualy/2+50,width,heigh,(100,100,100),(255,0,0),start_game)
    button("credits",(actualx)/2,actualy/2+50+heigh,width,heigh,(100,100,100),(255,0,0),pause_game)
    button("Quit",(actualx)/2,actualy/2+50+heigh+100,width,heigh,(100,100,100),(255,0,0),quit_game)
    pygame.mouse.set_visible(True)
    pygame.display.flip()
def menu_interaction():
    global gaming,main_menu,displayx,displayy,start_menu_postion,death_menu,the_game,reset7,reset9
    positionx=pygame.mouse.get_pos()[0]
    postiony=pygame.mouse.get_pos()[1]
    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_ESCAPE] == True:
        pygame.QUIT # Permet de gÃƒÂ©rer un clic sur le bouton de fermeture de la fenÃƒÂªtre
        gaming =False
        main_menu=False
        death_menu=False
        the_game=False
    if touchesPressees[pygame.K_f] == True:
        if pygame.time.get_ticks()-reset7>=300:
            pygame.display.toggle_fullscreen()
            pygame.display.set_mode(pygame.display.list_modes()[0],pygame.FULLSCREEN)
            displayx=pygame.display.list_modes()[0][0]
            displayy=pygame.display.list_modes()[0][1]
            actualx=displayx-(76*2)
            actualy=displayy-(103*2)
            reset7=pygame.time.get_ticks()
        else:
            pygame.display.set_mode(pygame.display.list_modes()[0],pygame.FULLSCREEN)
            displayx=pygame.display.list_modes()[1][0]
            displayy=pygame.display.list_modes()[1][1]
            actualx=displayx-(76*2)
            actualy=displayy-(103*2)
            reset7=pygame.time.get_ticks()
    if pygame.mixer.get_busy()==0:
        pygame.mixer.Sound.play(intro_music)
def death_menu_dessin():
    global main_menu,gaming,start_menu_postion,death_menu
    positionx=pygame.mouse.get_pos()[0]
    postiony=pygame.mouse.get_pos()[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
            main_menu=False
            death_menu=False
    fenetre.fill( (0,0,0) )
    width=200
    heigh=100
    button("Start",actualx/2+100,actualy/2+50,width,heigh,(100,100,100),(255,0,255),start_game)
    button("credits",actualx/2+100,actualy/2,width,heigh,(100,100,100),(255,0,255),pause_game)
    button("Quit",actualx/2+100,actualy/2+200,width,heigh,(100,100,100),(255,0,255),quit_game)
    pygame.mouse.set_visible(True)
def death_menu_interaction():
    global gaming,main_menu,displayx,displayy,start_menu_postion,death_menu,the_game,player_health,entity_enemy,actualx,actualy,actual_level
    positionx=pygame.mouse.get_pos()[0]
    postiony=pygame.mouse.get_pos()[1]
    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_ESCAPE] == True:
        quit_game()
    if touchesPressees[pygame.K_f] == True:
        if pygame.time.get_ticks()-reset7>=300 and fullscreen==False:
            pygame.display.toggle_fullscreen()
            pygame.display.set_mode(pygame.display.list_modes()[0],pygame.FULLSCREEN)
            displayx=pygame.display.list_modes()[0][0]
            displayy=pygame.display.list_modes()[0][1]
            start_menu_postion=((displayx-140)/2,displayy/2-100)
            actualx=displayx-(76*2)
            actualy=displayy-(103*2)
            reset7=pygame.time.get_ticks()
    pygame.mouse.set_visible(True)
def endgame():
    fenetre.fill((255,255,255))
    fenetre.blit(congrats,(500,200))
    pygame.display.flip()
    width=200
    heigh=100
    button("Start",actualx/2+100,actualy/2+50,width,heigh,(100,100,100),(255,0,255),start_game)
    button("credits",actualx/2+100,actualy/2,width,heigh,(100,100,100),(255,0,255),pause_game)
    button("Quit",actualx/2+100,actualy/2+200,width,heigh,(100,100,100),(255,0,255),quit_game)
clock = pygame.time.Clock()
latence=pygame.time.Clock()
def the_game():
    clock.tick(70)
    while main_menu==True:
        menu_dessin()
        menu_interaction()
    while gaming==True:
        logiqueDuJeu()
        gererClavierEtSouris()
        dessiner()
    while death_menu==True:
        menu_interaction()
        menu_dessin()
    while endmenu==True:
        endgame()
the_game()
## A la fin, lorsque l'on sortira de la boucle, on demandera ÃƒÂ  Pygame de quitter proprement
pygame.quit()
