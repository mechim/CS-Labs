import hashlib
import random
import math

msg = "it ran with almost unbelievable efficiency. the bags of mail for deliverythat morning to the embassies in vienna were brought to the blackchamber each day at 7 a.m. there the letters were opened by meltingtheir seals with a candle. the order of the letters in an envelope wasnoted and the letters given to a subdirector. he read them and orderedthe important parts copied. all the employees could write rapidly, andsome knew shorthand. long letters were dictated to save time,sometimes using four stenographers to a single letter. if a letter was in alanguage that he did not know, the subdirector gave it to a cabinetemployee familiar with it. two translators were always on hand. alleuropean languages could be read, and when a new one was needed, anofficial learned it. armenian, for example, took one cabinet polyglot onlya few months to learn, and he was paid the usual 500 florins for his newknowledge. after copying, the letters were replaced in their envelopes intheir original order and the envelopes re-sealed, using forged seals toimpress the original wax. the letters were returned to the post office by9:30 a.m.at 10 a.m., the mail that was passing through this crossroads of thecontinent arrived and was handled in the same way, though with lesshurry because it was in transit. usually it would be back in the post by 2p.m., though sometimes it was kept as late as 7 p.m. at 11 a.m.,interceptions made by the police for purposes of political surveillancearrived. and at 4 p.m., the couriers brought the letters that theembassies were sending out that day. these were back in the stream ofcommunications by 6:30 p.m. copied material was handed to thedirector of the cabinet, who excerpted information of special interest androuted it to the proper agencies, as police, army, or railwayadministration, and sent the mass of diplomatic material to the court. all told, the ten-man cabinet handled an average ofbetween 80 and 100 letters a day.astonishingly, their nimble fingers hardly ever stuffed letters into thewrong packet, despite the speed with which they worked. in one of thefew recorded blunders, an intercepted letter to the duke of modena waserroneously re-sealed with the closely similar signet of parma. when theduke noticed the substitution, he sent it to parma with the wry note, 'notjust me—you too.' both states protested, but the viennese greeted themwith a blank stare, a shrug, and a bland profession of ignorance. despitethis, the existence of the black chamber was well known to the variousdelegates to the austrian court, and was even tacitly acknowledged bythe austrians. when the british'ambassador complained humorously that he was getting copiesinstead of his original correspondence, the chancellor replied coolly,'how clumsy these people are!'enciphered correspondence was subjected to the usual cryptanalyticsweating process. the viennese enjoyed remarkable success in this work.the french ambassador, who was apprised of its successes from paperssold him by a masked man on a bridge, remarked in astonishment that'our ciphers of 1200 [groups] hold out only a little while against theability of the austrian decipherers.' he added that though he suggestednew ways of ciphering and continual changes of ciphers, 'i still findmyself without secure means for the secrets i have to transmit toconstantinople, stockholm, and st. petersburg.'"

hash_object = hashlib.sha3_224()
hash_object.update(msg.encode())
hashed_message = int.from_bytes(hash_object.digest(), byteorder='big')

hash_size = 224
hashed_message = hashed_message << (hash_size - hashed_message.bit_length())
print("Hashed message:", hashed_message)

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2

a = random.randint(1, p - 2)

b = pow(g, a, p)

while True:
    k = random.randint(1, p - 2)
    gcd_value = math.gcd(k, p - 1)

    if gcd_value == 1:
        r = pow(g, k, p)
        s = (pow(k, -1, p - 1) * (hashed_message - a * r)) % (p - 1)
        signature = (r, s)
        print("Signature:", signature)

        received_signature = signature
        r_received, s_received = received_signature

        v1 = (pow(b, r_received, p) * pow(r_received, s_received, p)) % p
        v2 = pow(g, hashed_message, p)
        verification = (v1 == v2)

        print("Signature Verification:", verification)
        break  