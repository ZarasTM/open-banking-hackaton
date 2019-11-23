_C=False
_B=None
_A='utf-8'
import base64,gzip,logging,ssl,uuid
from collections import namedtuple
from datetime import datetime
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request,urlopen
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from enablebanking import eb_core
def _params_to_pairs(params):A=params;return[(B.name,B.value)for B in A]if A else[]
_ApiParam=namedtuple('_ApiParam',('name','value'))
class Platform:
	def makeRequest(Q,request,callback):
		P='%d %r';O='gzip';N='content-encoding';J=callback;A=request;H=A.origin+A.path;K=urlencode(_params_to_pairs(A.query));L=A.body.encode();C=dict(_params_to_pairs(A.headers))
		if K:H+='?'+K
		logging.debug('Request(%r, %r, headers=%r, method=%r',H,L,C,A.method);M=Request(H,data=L,headers=C,method=A.method);E=_B
		if A.tls:E=ssl.create_default_context();E.check_hostname=_C;E.verify_mode=ssl.CERT_NONE;E.load_cert_chain(A.tls.certPath,A.tls.keyPath,lambda:A.tls.keyPassword)
		try:
			with urlopen(M,context=E)as F:
				I=F.info();logging.info('%r',I.items());G=I.get(N,_B)
				if G and G.lower()==O:B=gzip.decompress(F.read()).decode(_A)
				else:B=F.read().decode(_A)
				logging.debug(P,F.status,B);C=[_ApiParam(A,B)for(A,B)in(I.items())];J(eb_core.eb_ApiResponse(F.status,B,C))
		except HTTPError as D:
			G=D.headers[N]
			if G and G.lower()==O:B=gzip.decompress(D.fp.read()).decode(_A)
			else:B=D.fp.read().decode(_A)
			logging.error(P,D.status,B);C=[_ApiParam(A,B)for(A,B)in(D.headers.items())];J(eb_core.eb_ApiResponse(D.status,B,C))
	def genUUID(A):return str(uuid.uuid1())
	def getTimestamp(B,utc=_C):
		if utc:A=datetime.utcnow()
		else:A=datetime.now()
		return int(A.timestamp())
	def getCurrentDateTime(B,format,utc=_C):
		'Get current DateTime string according to passed format\n        \n        Arguments:\n            format {str} -- date format according to strftime\n        \n        Keyword Arguments:\n            utc {bool} -- If DateTime needs to be in UTC (default: {False})\n        \n        Returns:\n            str -- current DateTime string\n        '
		if utc:A=datetime.utcnow()
		else:A=datetime.now()
		return A.strftime(format)
	@staticmethod
	def _force_bytes(value):
		'Convert value to bytes if necessary\n        \n        Arguments:\n            value {String, Bytes} -- Some value to convert to bytes\n        \n        Raises:\n            TypeError: If wrong value is passed\n        \n        Returns:\n            Bytes -- Value converted to bytes]\n        ';A=value
		if isinstance(A,str):return A.encode(_A)
		elif isinstance(A,bytes):return A
		else:raise TypeError('Expected a string value')
	def _prepare_key(C,key,password=_B):
		'Create a key out of .pem key\n        \n        Arguments:\n            key {String, Bytes} -- Private/Public key value\n        \n        Keyword Arguments:\n            password {String} -- Password to a private key (default: {None})\n        \n        Raises:\n            TypeError: If wrong value is provided for a key\n        \n        Returns:\n            cryptography.hazmat.backends.openssl.rsa._RSAPrivateKey -- Private key class instance\n        ';A=key
		if isinstance(A,(str,bytes)):
			A=C._force_bytes(A)
			try:B=default_backend();A=B.load_pem_private_key(A,password)
			except ValueError:A=B.load_pem_public_key(A)
		else:raise TypeError('Expecting a PEM-formatted key.')
		return A
	def signPKCS1v15usingSHA256(B,data,key_path,key_password=_B):'Sign passed data with private key\n        \n        Arguments:\n            data {String, Bytes} -- Data to be signed\n            key_path {String} -- Path to a file with a private key\n        \n        Keyword Arguments:\n            key_password {String} -- Password to a private key (default: {None})\n        \n        Returns:\n            String -- Base64 encoded signed with a private key string\n        ';A=data;A=B._force_bytes(A);C=B._prepare_key(open(key_path,'rb').read());D=C.sign(A,padding.PKCS1v15(),hashes.SHA256());return base64.b64encode(D).decode('utf8')
	def getDateTimeWithOffset(D,offset,format,utc=_C):
		'Return DateTime with `offset` in seconds from current DateTime according to `format`\n        \n        Arguments:\n            offset {Integer} -- Offset in seconds from current datetime\n            format {String} -- strftime format\n            utc {Bool} -- Shows if the returned value in utc\n\n        Returns:\n            String -- DateTime string according to a passed format\n        ';C=int(datetime.now().timestamp());A=C+offset
		if utc:B=datetime.utcfromtimestamp(A)
		else:B=datetime.fromtimestamp(A)
		return B.strftime(format)