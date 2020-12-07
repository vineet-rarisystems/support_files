import socket
import sctp
from pycrate_asn1dir.NGAP import *
from pycrate_mobile.NAS             import *
from pycrate_core.elt               import _with_json
from pycrate_mobile.TS24501_FGMM import *
from pycrate_mobile.TS24501_FGSM import *

sk = sctp.sctpsocket_tcp(socket.AF_INET)
sk.connect(("127.0.0.1",38412))

print("creating ngsetup request Message")

PDU = NGAP_PDU_Descriptions.NGAP_PDU

#struct = {'procedureCode': 21, 'criticality': 'reject', 'value': ('NGAPSetupRequest', {'protocolIEs': [{'id': , 'criticality': 'reject', 'value': ('AMF-UE-NGAP-ID', 1)}, {'id': 85, 'criticality': 'reject', 'value': ('RAN-UE-NGAP-ID', 0)}, {'id': 64, 'criticality': 'reject', 'value': ('PDUSessionResourceModifyListModReq', [{'pDUSessionID': 1, 'nAS-PDU': b'~\x02\x00\x00\x00\x00\x04~\x00h\x01\x00\x04.\x01\x01\xcb\x12\x01', 'pDUSessionResourceModifyRequestTransfer': ('PDUSessionResourceModifyRequestTransfer', {'protocolIEs': [{'id': 140, 'criticality': 'reject', 'value': ('UL-NGU-UP-TNLModifyList', [{'uL-NGU-UP-TNLInformation': ('gTPTunnel', {'transportLayerAddress': (32895, 16), 'gTP-TEID': b'\x00\x00\x02\xf0'}), 'dL-NGU-UP-TNLInformation': ('gTPTunnel', {'transportLayerAddress': (0, 1), 'gTP-TEID': b'\x01\xf0\x7f\x00'})}])}]})}])}]})}

#PDU.set_val(struct)


#PDU = NGAP.NGAP_PDU_Descriptions.NGAP_PDU
#([]byte("\x00\x01\x02"), 24, "free5gc")

#gnbId = "\x00\x01\x02"
#gnbID bit length = 24 
#RANNodeName = "free5gc"
PDU.from_aper(unhexlify("00150035000004001b00080002f83910000102005240090300667265653567630066001000000000010002f839000010080102030015400140"))

print(PDU.to_asn1())
#print('to aper')
#print(PDU.to_aper())

#print(len(hexlify(PDU.to_uper())))
#show(PDU)
#PDU.to_aper()

sk.sctp_send(str(PDU.to_aper()),ppid = socket.htonl(60) )


sk.shutdown(0)
sk.close()