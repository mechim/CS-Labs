import random
import hashlib
from sympy import isprime
import math

def generate_large_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1 
        
        if isprime(num):
            return num


def choose_public_exponent(phi_n):
    e = 65537

    while not (1 < e < phi_n and math.gcd(e, phi_n) == 1):
        e = random.randint(2, phi_n - 1)

    return e

msg = "it ran with almost unbelievable efficiency. the bags of mail for deliverythat morning to the embassies in vienna were brought to the blackchamber each day at 7 a.m. there the letters were opened by meltingtheir seals with a candle. the order of the letters in an envelope wasnoted and the letters given to a subdirector. he read them and orderedthe important parts copied. all the employees could write rapidly, andsome knew shorthand. long letters were dictated to save time,sometimes using four stenographers to a single letter. if a letter was in alanguage that he did not know, the subdirector gave it to a cabinetemployee familiar with it. two translators were always on hand. alleuropean languages could be read, and when a new one was needed, anofficial learned it. armenian, for example, took one cabinet polyglot onlya few months to learn, and he was paid the usual 500 florins for his newknowledge. after copying, the letters were replaced in their envelopes intheir original order and the envelopes re-sealed, using forged seals toimpress the original wax. the letters were returned to the post office by9:30 a.m.at 10 a.m., the mail that was passing through this crossroads of thecontinent arrived and was handled in the same way, though with lesshurry because it was in transit. usually it would be back in the post by 2p.m., though sometimes it was kept as late as 7 p.m. at 11 a.m.,interceptions made by the police for purposes of political surveillancearrived. and at 4 p.m., the couriers brought the letters that theembassies were sending out that day. these were back in the stream ofcommunications by 6:30 p.m. copied material was handed to thedirector of the cabinet, who excerpted information of special interest androuted it to the proper agencies, as police, army, or railwayadministration, and sent the mass of diplomatic material to the court. all told, the ten-man cabinet handled an average ofbetween 80 and 100 letters a day.astonishingly, their nimble fingers hardly ever stuffed letters into thewrong packet, despite the speed with which they worked. in one of thefew recorded blunders, an intercepted letter to the duke of modena waserroneously re-sealed with the closely similar signet of parma. when theduke noticed the substitution, he sent it to parma with the wry note, 'notjust me—you too.' both states protested, but the viennese greeted themwith a blank stare, a shrug, and a bland profession of ignorance. despitethis, the existence of the black chamber was well known to the variousdelegates to the austrian court, and was even tacitly acknowledged bythe austrians. when the british'ambassador complained humorously that he was getting copiesinstead of his original correspondence, the chancellor replied coolly,'how clumsy these people are!'enciphered correspondence was subjected to the usual cryptanalyticsweating process. the viennese enjoyed remarkable success in this work.the french ambassador, who was apprised of its successes from paperssold him by a masked man on a bridge, remarked in astonishment that'our ciphers of 1200 [groups] hold out only a little while against theability of the austrian decipherers.' he added that though he suggestednew ways of ciphering and continual changes of ciphers, 'i still findmyself without secure means for the secrets i have to transmit toconstantinople, stockholm, and st. petersburg.'"

print("Message:", msg)

hash_object = hashlib.sha3_256()
hash_object.update(msg.encode())
hashed_message = int.from_bytes(hash_object.digest(), byteorder='big')

hash_size = 256
hashed_message = hashed_message << (hash_size - hashed_message.bit_length())
print("Hashed message:", hashed_message)


bits = 1554
prime1 = generate_large_prime(bits)
prime2 = generate_large_prime(bits)

n = prime1 * prime2
phi_n = (prime1 - 1) * (prime2 - 1)

e = choose_public_exponent(phi_n)

d = pow(e, -1, phi_n)

signature = pow(hashed_message, d, n)

verification = pow(signature, e, n)

print("Signature is valid:", verification == hashed_message)