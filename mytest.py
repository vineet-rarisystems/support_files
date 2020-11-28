from pycrate_mobile.NAS             import *
from pycrate_core.elt               import _with_json
#from pycrate_mobile.TS24501_FGMM import *
#from pycrate_mobile.TS24501_FGSM import *

# 5G NAS pdu
nas_5g_pdu = tuple(map(unhexlify, (
    '7e004179000d0100f1100000000022222222222e02e0e0', # 5GMM Reg Req
    '7e0056000200002198a600000000000098a600000000000020105c717acfe29180001fb3117a0f18c3ab', # 5GMM Auth Req
    '7e00572d1034f95b9d3826fc095c9d9232f4d182c5', # 5GMM Auth Resp
    '7e038f2b564d007e005d010002e0e0', # 5GMM Sec Mode Cmd
    '7e0300000000007e005d000602f0f0e1360102', # 5GMM Sec Mode Cmd, more beefy
    '7e04fd5a6e42007e005e', # 5GMM Encrypted message
    '7e005e', # 5GMM Sec Mode Compl inner
    '7e005e7700091530014100002100f07100217e004169000d010302460fff000000000000f11001072e02f0f02f05040aabcdef', # 5GMM Sec Mode Compl inner, more beefy
    '7e004407', # 5GMM Reg Rej
    '7e0100000000037e004561000bf2030246010041c0e00010', # 5GMM Integ prot MO Dereg Req
    '7e0046', # 5GMM MO Dereg Accept
    '7e0042010177000bf2030246010041c0e000105407200302460000641505040aabcdef2101005e016516012c', # 5GMM Reg Accept
    '7e0043', # 5GMM Reg Compl
    '7e0054d0430989cef73a1d2696db6f450989cef73a1d2696db6f46694791501391446069490101', # 5GMM Config Upd Cmd
    '2e0501c1ffff91a1', # 5GSM PDU Sess Estab Req
    '2e0501c211000901000631310101ff0506060001060001290501ac115f012506056461746131', # 5GSM PDU Sess Estab Accept
    '7e00670100072e0602c1000091120681220401000001250706766973696f6e', # 5GMM UL Trans, 5GSM PDU Sess Estab Req
    '7e0100000000067e006801002d2e0602c2110009ff000631310101ff050603f42403f4242905010b000033220401000001250706766973696f6e1206', # 5GMM DL Trans, 5GSM PDU Sess Estab Accept
    '7e00670500020002', # UE policy complete
    )))

def decode_nas_5g(nas_pdu):
    for pdu in nas_pdu:
        m, e = parse_NAS5G(pdu)
        print(e)
        assert( e == 0 )
        v = m.get_val()
        show(m)
        print(' Rari systems --------------------------------------------')
        m.reautomate()
        assert( m.get_val() == v )
        m.set_val(v)
        assert( m.to_bytes() == pdu )
        #
        if _with_json:
            t = m.to_json()
            m.from_json(t)
            assert( m.get_val() == v )


def test_my_code():
    #pdu_mas = unhexify('0123456789')
    
    #msg = FGMMRegistrationAccept() #Encoding a default message
    
    
    IEs = {}
    IEs['CKSN']= 4
    IEs['LocUpdateType'] = {'Type': 1}
    IEs['LAI'] = (u'20820', 0x4321)
    IEs['ID'] = {'type': 1, 'ident': u'208209876543210'}
    IEs['AddUpdateParams'] = {'CSMO': 1, 'CSMT': 1}

    msg = MMLocationUpdatingRequest(val=IEs)
    show(msg)

    test_msg = tuple(map(unhexlify, (
    '7e004179000d0100f1100000000022222222222e02e0e0', # 5GMM Reg Req
    )))
    print("/n/n  encode message  /n/n")
    print(msg.to_bytes())
    
    print("/n/n  decode the messages  /n/n")
    
    #decode_nas_5g(nas_5g_pdu)
    decode_nas_5g(test_msg)
    #show(M)


if __name__ == '__main__':
    test_my_code()

