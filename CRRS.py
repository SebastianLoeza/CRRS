from tkinter import * 
import tkinter as tk
import requests
import json
import pandas as pd
from PIL import ImageTk, Image
from io import BytesIO


URL_TOURNAMENTS = 'https://api.clashroyale.com/v1/tournaments'
URL_BATTLELOG = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC/battlelog'
URL_PLAYER = 'https://api.clashroyale.com/v1/players/%2382UUGL0YC'

cards_map = {
'Knight':'https://api-assets.clashroyale.com/cards/300/jAj1Q5rclXxU9kVImGqSJxa4wEMfEhvwNQ_4jiGUuqg.png',
'Archers':'https://api-assets.clashroyale.com/cards/300/W4Hmp8MTSdXANN8KdblbtHwtsbt0o749BbxNqmJYfA8.png',
'Goblins':'https://api-assets.clashroyale.com/cards/300/X_DQUye_OaS3QN6VC9CPw05Fit7wvSm3XegXIXKP--0.png',
'Giant':'https://api-assets.clashroyale.com/cards/300/Axr4ox5_b7edmLsoHxBX3vmgijAIibuF6RImTbqLlXE.png',
'P.E.K.K.A':'https://api-assets.clashroyale.com/cards/300/MlArURKhn_zWAZY-Xj1qIRKLVKquarG25BXDjUQajNs.png',
'Minions':'https://api-assets.clashroyale.com/cards/300/yHGpoEnmUWPGV_hBbhn-Kk-Bs838OjGzWzJJlQpQKQA.png',
'Balloon':'https://api-assets.clashroyale.com/cards/300/qBipxLo-3hhCnPrApp2Nn3b2NgrSrvwzWytvREev0CY.png',
'Witch':'https://api-assets.clashroyale.com/cards/300/cfwk1vzehVyHC-uloEIH6NOI0hOdofCutR5PyhIgO6w.png',
'Barbarians':'https://api-assets.clashroyale.com/cards/300/TvJsuu2S4yhyk1jVYUAQwdKOnW4U77KuWWOTPOWnwfI.png',
'Golem':'https://api-assets.clashroyale.com/cards/300/npdmCnET7jmVjJvjJQkFnNSNnDxYHDBigbvIAloFMds.png',
'Skeletons':'https://api-assets.clashroyale.com/cards/300/oO7iKMU5m0cdxhYPZA3nWQiAUh2yoGgdThLWB1rVSec.png',
'Valkyrie':'https://api-assets.clashroyale.com/cards/300/0lIoYf3Y_plFTzo95zZL93JVxpfb3MMgFDDhgSDGU9A.png',
'Skeleton Army':'https://api-assets.clashroyale.com/cards/300/fAOToOi1pRy7svN2xQS6mDkhQw2pj9m_17FauaNqyl4.png',
'Bomber':'https://api-assets.clashroyale.com/cards/300/12n1CesxKIcqVYntjxcF36EFA-ONw7Z-DoL0_rQrbdo.png',
'Musketeer':'https://api-assets.clashroyale.com/cards/300/Tex1C48UTq9FKtAX-3tzG0FJmc9jzncUZG3bb5Vf-Ds.png',
'Baby Dragon':'https://api-assets.clashroyale.com/cards/300/cjC9n4AvEZJ3urkVh-rwBkJ-aRSsydIMqSAV48hAih0.png',
'Prince':'https://api-assets.clashroyale.com/cards/300/3JntJV62aY0G1Qh6LIs-ek-0ayeYFY3VItpG7cb9I60.png',
'Wizard':'https://api-assets.clashroyale.com/cards/300/Mej7vnv4H_3p_8qPs_N6_GKahy6HDr7pU7i9eTHS84U.png',
'Mini P.E.K.K.A':'https://api-assets.clashroyale.com/cards/300/Fmltc4j3Ve9vO_xhHHPEO3PRP3SmU2oKp2zkZQHRZT4.png',
'Spear Goblins':'https://api-assets.clashroyale.com/cards/300/FSDFotjaXidI4ku_WFpVCTWS1hKGnFh1sxX0lxM43_E.png',
'Giant Skeleton':'https://api-assets.clashroyale.com/cards/300/0p0gd0XaVRu1Hb1iSG1hTYbz2AN6aEiZnhaAib5O8Z8.png',
'Hog Rider':'https://api-assets.clashroyale.com/cards/300/Ubu0oUl8tZkusnkZf8Xv9Vno5IO29Y-jbZ4fhoNJ5oc.png',
'Minion Horde':'https://api-assets.clashroyale.com/cards/300/Wyjq5l0IXHTkX9Rmpap6HaH08MvjbxFp1xBO9a47YSI.png',
'Ice Wizard':'https://api-assets.clashroyale.com/cards/300/W3dkw0HTw9n1jB-zbknY2w3wHuyuLxSRIAV5fUT1SEY.png',
'Royal Giant':'https://api-assets.clashroyale.com/cards/300/mnlRaNtmfpQx2e6mp70sLd0ND-pKPF70Cf87_agEKg4.png',
'Guards':'https://api-assets.clashroyale.com/cards/300/1ArKfLJxYo6_NU_S9cAeIrfbXqWH0oULVJXedxBXQlU.png',
'Princess':'https://api-assets.clashroyale.com/cards/300/bAwMcqp9EKVIKH3ZLm_m0MqZFSG72zG-vKxpx8aKoVs.png',
'Dark Prince':'https://api-assets.clashroyale.com/cards/300/M7fXlrKXHu2IvpSGpk36kXVstslbR08Bbxcy0jQcln8.png',
'Three Musketeers':'https://api-assets.clashroyale.com/cards/300/_J2GhbkX3vswaFk1wG-dopwiHyNc_YiPhwroiKF3Mek.png',
'Lava Hound':'https://api-assets.clashroyale.com/cards/300/unicRQ975sBY2oLtfgZbAI56ZvaWz7azj-vXTLxc0r8.png',
'Ice Spirit':'https://api-assets.clashroyale.com/cards/300/lv1budiafU9XmSdrDkk0NYyqASAFYyZ06CPysXKZXlA.png',
'Fire Spirit':'https://api-assets.clashroyale.com/cards/300/16-BqusVvynIgYI8_Jci3LDC-r8AI_xaIYLgXqtlmS8.png',
'Miner':'https://api-assets.clashroyale.com/cards/300/Y4yWvdwBCg2FpAZgs8T09Gy34WOwpLZW-ttL52Ae8NE.png',
'Sparky':'https://api-assets.clashroyale.com/cards/300/2GKMkBrArZXgQxf2ygFjDs4VvGYPbx8F6Lj_68iVhIM.png',
'Bowler':'https://api-assets.clashroyale.com/cards/300/SU4qFXmbQXWjvASxVI6z9IJuTYolx4A0MKK90sTIE88.png',
'Lumberjack':'https://api-assets.clashroyale.com/cards/300/E6RWrnCuk13xMX5OE1EQtLEKTZQV6B78d00y8PlXt6Q.png',
'Battle Ram':'https://api-assets.clashroyale.com/cards/300/dyc50V2cplKi4H7pq1B3I36pl_sEH5DQrNHboS_dbbM.png',
'Inferno Dragon':'https://api-assets.clashroyale.com/cards/300/y5HDbKtTbWG6En6TGWU0xoVIGs1-iQpIP4HC-VM7u8A.png',
'Ice Golem':'https://api-assets.clashroyale.com/cards/300/r05cmpwV1o7i7FHodtZwW3fmjbXCW34IJCsDEV5cZC4.png',
'Mega Minion':'https://api-assets.clashroyale.com/cards/300/-T_e4YLbuhPBKbYnBwQfXgynNpp5eOIN_0RracYwL9c.png',
'Dart Goblin':'https://api-assets.clashroyale.com/cards/300/BmpK3bqEAviflqHCdxxnfm-_l3pRPJw3qxHkwS55nCY.png',
'Goblin Gang':'https://api-assets.clashroyale.com/cards/300/NHflxzVAQT4oAz7eDfdueqpictb5vrWezn1nuqFhE4w.png',
'Electro Wizard':'https://api-assets.clashroyale.com/cards/300/RsFaHgB3w6vXsTjXdPr3x8l_GbV9TbOUCvIx07prbrQ.png',
'Elite Barbarians':'https://api-assets.clashroyale.com/cards/300/C88C5JH_F3lLZj6K-tLcMo5DPjrFmvzIb1R2M6xCfTE.png',
'Hunter':'https://api-assets.clashroyale.com/cards/300/VNabB1WKnYtYRSG7X_FZfnZjQDHTBs9A96OGMFmecrA.png',
'Executioner':'https://api-assets.clashroyale.com/cards/300/9XL5BP2mqzV8kza6KF8rOxrpCZTyuGLp2l413DTjEoM.png',
'Bandit':'https://api-assets.clashroyale.com/cards/300/QWDdXMKJNpv0go-HYaWQWP6p8uIOHjqn-zX7G0p3DyM.png',
'Royal Recruits':'https://api-assets.clashroyale.com/cards/300/jcNyYGUiXXNz3kuz8NBkHNKNREQKraXlb_Ts7rhCIdM.png',
'Night Witch':'https://api-assets.clashroyale.com/cards/300/NpCrXDEDBBJgNv9QrBAcJmmMFbS7pe3KCY8xJ5VB18A.png',
'Bats':'https://api-assets.clashroyale.com/cards/300/EnIcvO21hxiNpoI-zO6MDjLmzwPbq8Z4JPo2OKoVUjU.png',
'Royal Ghost':'https://api-assets.clashroyale.com/cards/300/3En2cz0ISQAaMTHY3hj3rTveFN2kJYq-H4VxvdJNvCM.png',
'Ram Rider':'https://api-assets.clashroyale.com/cards/300/QaJyerT7f7oMyZ3Fv1glKymtLSvx7YUXisAulxl7zRI.png',
'Zappies':'https://api-assets.clashroyale.com/cards/300/QZfHRpLRmutZbCr5fpLnTpIp89vLI6NrAwzGZ8tHEc4.png',
'Rascals':'https://api-assets.clashroyale.com/cards/300/KV48DfwVHKx9XCjzBdk3daT_Eb52Me4VgjVO7WctRc4.png',
'Cannon Cart':'https://api-assets.clashroyale.com/cards/300/aqwxRz8HXzqlMCO4WMXNA1txynjXTsLinknqsgZLbok.png',
'Mega Knight':'https://api-assets.clashroyale.com/cards/300/O2NycChSNhn_UK9nqBXUhhC_lILkiANzPuJjtjoz0CE.png',
'Skeleton Barrel':'https://api-assets.clashroyale.com/cards/300/vCB4DWCcrGbTkarjcOiVz4aNDx6GWLm0yUepg9E1MGo.png',
'Flying Machine':'https://api-assets.clashroyale.com/cards/300/hzKNE3QwFcrSrDDRuVW3QY_OnrDPijSiIp-PsWgFevE.png',
'Wall Breakers':'https://api-assets.clashroyale.com/cards/300/_xPphEfC8eEwFNrfU3cMQG9-f5JaLQ31ARCA7l3XtW4.png',
'Royal Hogs':'https://api-assets.clashroyale.com/cards/300/ASSQJG_MoVq9e81HZzo4bynMnyLNpNJMfSLb3hqydOw.png',
'Goblin Giant':'https://api-assets.clashroyale.com/cards/300/SoW16cY3jXBwaTDvb39DkqiVsoFVaDWbzf5QBYphJrY.png',
'Fisherman':'https://api-assets.clashroyale.com/cards/300/U2KZ3g0wyufcuA5P2Xrn3Z3lr1WiJmc5S0IWOZHgizQ.png',
'Magic Archer':'https://api-assets.clashroyale.com/cards/300/Avli3W7BxU9HQ2SoLiXnBgGx25FoNXUSFm7OcAk68ek.png',
'Electro Dragon':'https://api-assets.clashroyale.com/cards/300/tN9h6lnMNPCNsx0LMFmvpHgznbDZ1fBRkx-C7UfNmfY.png',
'Firecracker':'https://api-assets.clashroyale.com/cards/300/c1rL3LO1U2D9-TkeFfAC18gP3AO8ztSwrcHMZplwL2Q.png',
'Mighty Miner':'https://api-assets.clashroyale.com/cards/300/Cd9R56yraxTvJiD8xJ2qT2OdsHyh94FqOAarXpbyelo.png',
'Elixir Golem':'https://api-assets.clashroyale.com/cards/300/puhMsZjCIqy21HW3hYxjrk_xt8NIPyFqjRy-BeLKZwo.png',
'Battle Healer':'https://api-assets.clashroyale.com/cards/300/KdwXcoigS2Kg-cgA7BJJIANbUJG6SNgjetRQ-MegZ08.png',
'Skeleton King':'https://api-assets.clashroyale.com/cards/300/dCd69_wN9f8DxwuqOGtR4QgWhHIPIaTNxZ1e23RzAAc.png',
'Archer Queen':'https://api-assets.clashroyale.com/cards/300/p7OQmOAFTery7zCzlpDdm-LOD1kINTm42AwIHchZfWk.png',
'Golden Knight':'https://api-assets.clashroyale.com/cards/300/WJd207D0O1sN-l1FTb8P9KhYL2oF5jY26vRUfTUW3FQ.png',
'Monk':'https://api-assets.clashroyale.com/cards/300/2onG4t4-CxqwFVZAn6zpWxFz3_mG2ksSj4Q7zldo1SM.png',
'Skeleton Dragons':'https://api-assets.clashroyale.com/cards/300/qPOtg9uONh47_NLxGhhFc_ww9PlZ6z3Ry507q1NZUXs.png',
'Mother Witch':'https://api-assets.clashroyale.com/cards/300/fO-Xah8XZkYKaSK9SCp3wnzwxtvIhun9NVY-zzte1Ng.png',
'Electro Spirit':'https://api-assets.clashroyale.com/cards/300/WKd4-IAFsgPpMo7dDi9sujmYjRhOMEWiE07OUJpvD9g.png',
'Electro Giant':'https://api-assets.clashroyale.com/cards/300/_uChZkNHAMq6tPb3v6A49xinOe3CnhjstOhG6OZbPYc.png',
'Phoenix':'https://api-assets.clashroyale.com/cards/300/i0RoY1fs6ay7VAxyFEfZGIPnD002nAKcne9FtJsWBHM.png',
'Cannon':'https://api-assets.clashroyale.com/cards/300/nZK1y-beLxO5vnlyUhK6-2zH2NzXJwqykcosqQ1cmZ8.png',
'Goblin Hut':'https://api-assets.clashroyale.com/cards/300/l8ZdzzNLcwB4u7ihGgxNFQOjCT_njFuAhZr7D6PRF7E.png',
'Mortar':'https://api-assets.clashroyale.com/cards/300/lPOSw6H7YOHq2miSCrf7ZDL3ANjhJdPPDYOTujdNrVE.png',
'Inferno Tower':'https://api-assets.clashroyale.com/cards/300/GSHY_wrooMMLET6bG_WJB8redtwx66c4i80ipi4gYOM.png',
'Bomb Tower':'https://api-assets.clashroyale.com/cards/300/rirYRyHPc97emRjoH-c1O8uZCBzPVnToaGuNGusF3TQ.png',
'Barbarian Hut':'https://api-assets.clashroyale.com/cards/300/ho0nOG2y3Ch86elHHcocQs8Fv_QNe0cFJ2CijsxABZA.png',
'Tesla':'https://api-assets.clashroyale.com/cards/300/OiwnGrxFMNiHetYEerE-UZt0L_uYNzFY7qV_CA_OxR4.png',
'Elixir Collector':'https://api-assets.clashroyale.com/cards/300/BGLo3Grsp81c72EpxLLk-Sofk3VY56zahnUNOv3JcT0.png',
'X-Bow':'https://api-assets.clashroyale.com/cards/300/zVQ9Hme1hlj9Dc6e1ORl9xWwglcSrP7ejow5mAhLUJc.png',
'Tombstone':'https://api-assets.clashroyale.com/cards/300/LjSfSbwQfkZuRJY4pVxKspZ-a0iM5KAhU8w-a_N5Z7Y.png',
'Furnace':'https://api-assets.clashroyale.com/cards/300/iqbDiG7yYRIzvCPXdt9zPb3IvMt7F7Gi4wIPnh2x4aI.png',
'Goblin Cage':'https://api-assets.clashroyale.com/cards/300/vD24bBgK4rSq7wx5QEbuqChtPMRFviL_ep76GwQw1yA.png',
'Goblin Drill':'https://api-assets.clashroyale.com/cards/300/eN2TKUYbih-26yBi0xy5LVFOA0zDftgDqxxnVfdIg1o.png',
'Fireball':'https://api-assets.clashroyale.com/cards/300/lZD9MILQv7O-P3XBr_xOLS5idwuz3_7Ws9G60U36yhc.png',
'Arrows':'https://api-assets.clashroyale.com/cards/300/Flsoci-Y6y8ZFVi5uRFTmgkPnCmMyMVrU7YmmuPvSBo.png',
'Rage':'https://api-assets.clashroyale.com/cards/300/bGP21OOmcpHMJ5ZA79bHVV2D-NzPtDkvBskCNJb7pg0.png',
'Rocket':'https://api-assets.clashroyale.com/cards/300/Ie07nQNK9CjhKOa4-arFAewi4EroqaA-86Xo7r5tx94.png',
'Goblin Barrel':'https://api-assets.clashroyale.com/cards/300/CoZdp5PpsTH858l212lAMeJxVJ0zxv9V-f5xC8Bvj5g.png',
'Freeze':'https://api-assets.clashroyale.com/cards/300/I1M20_Zs_p_BS1NaNIVQjuMJkYI_1-ePtwYZahn0JXQ.png',
'Mirror':'https://api-assets.clashroyale.com/cards/300/wC6Cm9rKLEOk72zTsukVwxewKIoO4ZcMJun54zCPWvA.png',
'Lightning':'https://api-assets.clashroyale.com/cards/300/fpnESbYqe5GyZmaVVYe-SEu7tE0Kxh_HZyVigzvLjks.png',
'Zap':'https://api-assets.clashroyale.com/cards/300/7dxh2-yCBy1x44GrBaL29vjqnEEeJXHEAlsi5g6D1eY.png',
'Poison':'https://api-assets.clashroyale.com/cards/300/98HDkG2189yOULcVG9jz2QbJKtfuhH21DIrIjkOjxI8.png',
'Graveyard':'https://api-assets.clashroyale.com/cards/300/Icp8BIyyfBTj1ncCJS7mb82SY7TPV-MAE-J2L2R48DI.png',
'The Log':'https://api-assets.clashroyale.com/cards/300/_iDwuDLexHPFZ_x4_a0eP-rxCS6vwWgTs6DLauwwoaY.png',
'Tornado':'https://api-assets.clashroyale.com/cards/300/QJB-QK1QJHdw4hjpAwVSyZBozc2ZWAR9pQ-SMUyKaT0.png',
'Clone':'https://api-assets.clashroyale.com/cards/300/mHVCet-1TkwWq-pxVIU2ZWY9_2z7Z7wtP25ArEUsP_g.png',
'Earthquake':'https://api-assets.clashroyale.com/cards/300/XeQXcrUu59C52DslyZVwCnbi4yamID-WxfVZLShgZmE.png',
'Barbarian Barrel':'https://api-assets.clashroyale.com/cards/300/Gb0G1yNy0i5cIGUHin8uoFWxqntNtRPhY_jeMXg7HnA.png',
'Heal Spirit':'https://api-assets.clashroyale.com/cards/300/GITl06sa2nGRLPvboyXbGEv5E3I-wAwn1Eqa5esggbc.png',
'Giant Snowball':'https://api-assets.clashroyale.com/cards/300/7MaJLa6hK9WN2_VIshuh5DIDfGwm0wEv98gXtAxLDPs.png',
'Royal Delivery':'https://api-assets.clashroyale.com/cards/300/LPg7AGjGI3_xmi7gLLgGC50yKM1jJ2teWkZfoHJcIZo.png'
}

#Bearer is only to use in school
headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRmODEyOGIwLTY3ZDQtNDg1MS1hYzIzLWMyMjVhZTVhZWJhMiIsImlhdCI6MTY5MjgzODQyNiwic3ViIjoiZGV2ZWxvcGVyLzA0NGExZjVjLTQwYWItOTYyYS1lNzBhLTI3ZWU5Yjk2YjZhMiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNDguMjA0LjU2LjI0MSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.2eTJrX9FXwHJx-UGpViUHy910mQPyfGVC78Q3JDeuhXSTZB42G7uVckZ3RfDxVes5p4jO0Bwu9NFi48MXluDVQ'

}


root = Tk()
root.title("Clash Royale Recommendation System")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def get_all_tournaments():
    response = requests.get(url=URL_TOURNAMENTS + '?name=' + e.get(), headers=headers)
    print("Tournament status code: " + str(response.status_code))

    if response.status_code == 200:
        items_obj = json.loads(response.text)
        items_list = items_obj.get('items')

        result_window = Toplevel(root)
        result_window.title("Results")

        text_widget = Text(result_window, width=100, height=100)
        text_widget.pack()

        for item in items_list:
            result = (
                'Nombre: ' + item['name'] +
                '\nEstado: ' + item['status'] +
                '\nTag: ' + item['tag'] +
                '\nCapacidad Máxima: ' + str(item['maxCapacity']) +
                '\nCapacidad Actual: ' + str(item['capacity']) +
                '\n======================\n'
            )
            text_widget.insert(END, result)

def get_player_battle_log():
    BATTLELOG = URL_BATTLELOG.replace('82UUGL0YC', e.get())
    response = requests.get(url=BATTLELOG, headers=headers)
    print("Player Battle Log Status code: " + str(response.status_code))

    if response.status_code == 200:
        battle_logs = response.json()
        cards_vec = []
        cards_malos_vec=[]

        for log in battle_logs:
            team = log['team']
            for card in team[0]['cards']:
                cards_vec.append(card['name'])

        cartas_vec = pd.Series(cards_vec)

        max_card = cartas_vec.value_counts().idxmax()
        #min_card = cartas_vec.value_counts().idxmin()




        #result = (
        #    "En los últimos 25 juegos la carta más repetida es: " + max_card +
         #   "\nEn los últimos 25 juegos la carta menos repetida es: " + min_card +
         #   "\n\nRecomendaciones de mazo:"
       # )
        #text_widget.insert(END, result)

        recommendation_count = 0

        for log in battle_logs:
            team = log['team']
            crowns = team[0]['crowns']
            opponent = log['opponent']
            crowns_opponent = opponent[0]['crowns']

            player_cards = [card['name'] for card in team[0]['cards']]

            if max_card in player_cards and crowns_opponent > crowns:
                for cardop in opponent[0]['cards']:
                    cards_malos_vec.append(cardop['name'])
     
                recommendation_count += 1

                if recommendation_count == 3:
                    break

    else:
        print("No se pudo obtener el registro de batallas del jugador.")
    #print(cards_malos_vec)

    image_window = tk.Toplevel(root)

    # Configure the grid geometry manager
    image_window.grid()

    # Variable to track the column count
    column_count = 1
    row_count = 1

    # Iterate over the card names in the card_name vector
    for card_name in cards_malos_vec:
        # Check if the maximum number of rows has been reached
        if row_count == 4:
            break

        # Get the corresponding image URL from the cards_map
        image_url = cards_map.get(card_name)

        if image_url:
            # Get the image from the URL
            response = requests.get(image_url)
            image_data = response.content

            # Create a PIL image from the downloaded data
            pil_image = Image.open(BytesIO(image_data))

            # Resize the image if necessary
            pil_image = pil_image.resize((100, 100), Image.LANCZOS)

            # Create an instance of ImageTk to display the image in Tkinter
            image = ImageTk.PhotoImage(pil_image)

            # Create a label to display the image
            image_label = tk.Label(image_window, image=image)
            image_label.grid(row=row_count, column=column_count, padx=10, pady=10)

            # Increment the column count
            column_count += 1

            # Reset column count and increment row count if 8 images have been displayed in the row
            if column_count == 9:
                column_count = 1
                row_count += 1

            # Store a reference to the image to prevent it from being garbage collected
            image_label.image = image

    label = tk.Label(image_window, text="Mazo 1:")
    label.grid(row=1, column=0, padx=10, pady=10)
    label2 = tk.Label(image_window, text="Mazo 2:")
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3 = tk.Label(image_window, text="Mazo 3:")
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4 = tk.Label(image_window, text="Recomiendo usar estos mazos:")
    label4.grid(row=0, column=0, padx=10, pady=10)


def get_player():
    PLAYER = URL_PLAYER.replace('82UUGL0YC', e.get())

    response = requests.get(url=PLAYER, headers=headers)
    result_window = tk.Toplevel(root)  # Create a new window for the result
    result_window.title("Results")
    
    if response.status_code == 200:
        user_json = response.json()
        result_text = tk.Text(result_window)
        result_text.pack()

        result_text.insert(tk.END, 'Nombre: ' + user_json['name'] + "\n")
        result_text.insert(tk.END, 'Nivel: ' + str(user_json['expLevel']) + "\n")
        result_text.insert(tk.END, 'Trofeos: ' + str(user_json['trophies']) + "\n")
        result_text.insert(tk.END, 'Total de batallas: ' + str(user_json['battleCount']) + "\n")
        result_text.insert(tk.END, "==============================\n")
    else:
        result_text = tk.Text(result_window)
        result_text.pack()
        result_text.insert(tk.END, "Player not found or an error occurred.\n")



button_GetPBattleLog = Button(root, text="Recomendaciones", padx=40, pady=20, command=get_player_battle_log)
button_GetPBattleLog.grid(row=1, column=0, columnspan=3)



button_GetPlayer = Button(root, text="Torneos", padx=40, pady=20, command=get_all_tournaments)
button_GetPlayer.grid(row=2, column=0, columnspan=3)

button_GetPlayerResume=Button(root,text='Resumen Jugador',padx=40,pady=20,command=get_player)
button_GetPlayerResume.grid(row=3,column=0,columnspan=3)

root.mainloop()
