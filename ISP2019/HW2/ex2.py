import asyncio
import websockets
import os
import binascii
import hashlib

async def hello():
    async with websockets.connect('ws://com402.epfl.ch/hw2/ws') as websocket:
        N="EEAF0AB9ADB38DD69C33F80AFA8FC5E86072618775FF3C0B9EA2314C9C256576D674DF7496EA81D3383B4813D692C6E0E0D5D8E250B98BE48E495C1D6089DAD15DC7D7B46154D6B6CE8EF4AD69B15D4982559B297BCF1885C529F566660E57EC68EDBC3C05726CC02FD4CBF4976EAA9AFD5138FE8376435B9FC61D2FC0EB06E3"
        N = int(N, 16)
        g=2
        await websocket.send("zeineb.sahnoun@epfl.ch")
        
        Random = await websocket.recv()
        a=int.from_bytes(os.urandom(32),"big")
        A = pow(g,a,N)
        buff = A.to_bytes((A.bit_length() + 7) //8,'big')
        strToSend = binascii.hexlify(buff).decode()
        await websocket.send(strToSend)

        salt = int(Random, 16)
        salt = salt.to_bytes((salt.bit_length() + 7) //8,'big')

        RecvB = await websocket.recv()
        B = binascii.unhexlify(RecvB)
        hexx = hashlib.sha256(salt + binascii.unhexlify(hashlib.sha256(b'zeineb.sahnoun@epfl.ch:NAAfCxdCXRYPDE4OVQY1CBEITFoMSA==').hexdigest())).hexdigest()
        hexx= int(hexx,16)
        p = pow(int.from_bytes(B, 'big') - pow(g,hexx,N),pow((a + int(hashlib.sha256(buff + B).hexdigest(),16)*hexx),1,N),N)
        await websocket.send(hashlib.sha256(buff + B + p.to_bytes((p.bit_length() + 7) //8,'big')).hexdigest())
        
        token = await websocket.recv()
        print(str(token))

                             
                             
asyncio.get_event_loop().run_until_complete(hello())
