'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_J='payment_auth_state'
_I='payment_auth_redirect_uri'
_H='sign_pub_key_serial'
_G='sign_key_path'
_F='key_path'
_E='cert_path'
_D='x_api_key'
_C='client_id'
_B='str'
_A=None
import pprint,re,six
from enablebanking.models.connector_settings import ConnectorSettings
class KomplettConnectorSettings(ConnectorSettings):
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_C:_B,_D:_B,_E:_B,_F:_B,_G:_B,_H:_B,_I:_B,_J:_B};attribute_map={_C:'clientId',_D:'xApiKey',_E:'certPath',_F:'keyPath',_G:'signKeyPath',_H:'signPubKeySerial',_I:'paymentAuthRedirectUri',_J:'paymentAuthState'}
	def __init__(A,client_id=_A,x_api_key=_A,cert_path=_A,key_path=_A,sign_key_path=_A,sign_pub_key_serial=_A,payment_auth_redirect_uri=_A,payment_auth_state=_A):
		'KomplettConnectorSettings - a model defined in Swagger';C=payment_auth_state;B=payment_auth_redirect_uri;A._client_id=_A;A._x_api_key=_A;A._cert_path=_A;A._key_path=_A;A._sign_key_path=_A;A._sign_pub_key_serial=_A;A._payment_auth_redirect_uri=_A;A._payment_auth_state=_A;A.discriminator=_A;A.client_id=client_id;A.x_api_key=x_api_key;A.cert_path=cert_path;A.key_path=key_path;A.sign_key_path=sign_key_path;A.sign_pub_key_serial=sign_pub_key_serial
		if B is not _A:A.payment_auth_redirect_uri=B
		if C is not _A:A.payment_auth_state=C
	@property
	def client_id(self):'Gets the client_id of this KomplettConnectorSettings.  # noqa: E501\n\n          # noqa: E501\n\n        :return: The client_id of this KomplettConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._client_id
	@client_id.setter
	def client_id(self,client_id):
		'Sets the client_id of this KomplettConnectorSettings.\n\n          # noqa: E501\n\n        :param client_id: The client_id of this KomplettConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=client_id
		if A is _A:raise ValueError('Invalid value for `client_id`, must not be `None`')
		self._client_id=A
	@property
	def x_api_key(self):'Gets the x_api_key of this KomplettConnectorSettings.  # noqa: E501\n\n          # noqa: E501\n\n        :return: The x_api_key of this KomplettConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._x_api_key
	@x_api_key.setter
	def x_api_key(self,x_api_key):
		'Sets the x_api_key of this KomplettConnectorSettings.\n\n          # noqa: E501\n\n        :param x_api_key: The x_api_key of this KomplettConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=x_api_key
		if A is _A:raise ValueError('Invalid value for `x_api_key`, must not be `None`')
		self._x_api_key=A
	@property
	def cert_path(self):'Gets the cert_path of this KomplettConnectorSettings.  # noqa: E501\n\n          # noqa: E501\n\n        :return: The cert_path of this KomplettConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._cert_path
	@cert_path.setter
	def cert_path(self,cert_path):
		'Sets the cert_path of this KomplettConnectorSettings.\n\n          # noqa: E501\n\n        :param cert_path: The cert_path of this KomplettConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=cert_path
		if A is _A:raise ValueError('Invalid value for `cert_path`, must not be `None`')
		self._cert_path=A
	@property
	def key_path(self):'Gets the key_path of this KomplettConnectorSettings.  # noqa: E501\n\n          # noqa: E501\n\n        :return: The key_path of this KomplettConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._key_path
	@key_path.setter
	def key_path(self,key_path):
		'Sets the key_path of this KomplettConnectorSettings.\n\n          # noqa: E501\n\n        :param key_path: The key_path of this KomplettConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=key_path
		if A is _A:raise ValueError('Invalid value for `key_path`, must not be `None`')
		self._key_path=A
	@property
	def sign_key_path(self):'Gets the sign_key_path of this KomplettConnectorSettings.  # noqa: E501\n\n          # noqa: E501\n\n        :return: The sign_key_path of this KomplettConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._sign_key_path
	@sign_key_path.setter
	def sign_key_path(self,sign_key_path):
		'Sets the sign_key_path of this KomplettConnectorSettings.\n\n          # noqa: E501\n\n        :param sign_key_path: The sign_key_path of this KomplettConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=sign_key_path
		if A is _A:raise ValueError('Invalid value for `sign_key_path`, must not be `None`')
		self._sign_key_path=A
	@property
	def sign_pub_key_serial(self):'Gets the sign_pub_key_serial of this KomplettConnectorSettings.  # noqa: E501\n\n        Public serial key of the QSeal certificate located in signKeyPath. The serial must be presented as a decimal string. The following command can be use for extracting it from QSeal certificate in PEM format:  <code>echo "obase=10; ibase=16; \\`openssl x509 -in qseal-crt.pem -serial -noout \\| awk -F "=" \'{print $2}\'\\`" \\| bc</code>   # noqa: E501\n\n        :return: The sign_pub_key_serial of this KomplettConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._sign_pub_key_serial
	@sign_pub_key_serial.setter
	def sign_pub_key_serial(self,sign_pub_key_serial):
		'Sets the sign_pub_key_serial of this KomplettConnectorSettings.\n\n        Public serial key of the QSeal certificate located in signKeyPath. The serial must be presented as a decimal string. The following command can be use for extracting it from QSeal certificate in PEM format:  <code>echo "obase=10; ibase=16; \\`openssl x509 -in qseal-crt.pem -serial -noout \\| awk -F "=" \'{print $2}\'\\`" \\| bc</code>   # noqa: E501\n\n        :param sign_pub_key_serial: The sign_pub_key_serial of this KomplettConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=sign_pub_key_serial
		if A is _A:raise ValueError('Invalid value for `sign_pub_key_serial`, must not be `None`')
		self._sign_pub_key_serial=A
	@property
	def payment_auth_redirect_uri(self):'Gets the payment_auth_redirect_uri of this KomplettConnectorSettings.  # noqa: E501\n\n          # noqa: E501\n\n        :return: The payment_auth_redirect_uri of this KomplettConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._payment_auth_redirect_uri
	@payment_auth_redirect_uri.setter
	def payment_auth_redirect_uri(self,payment_auth_redirect_uri):'Sets the payment_auth_redirect_uri of this KomplettConnectorSettings.\n\n          # noqa: E501\n\n        :param payment_auth_redirect_uri: The payment_auth_redirect_uri of this KomplettConnectorSettings.  # noqa: E501\n        :type: str\n        ';self._payment_auth_redirect_uri=payment_auth_redirect_uri
	@property
	def payment_auth_state(self):'Gets the payment_auth_state of this KomplettConnectorSettings.  # noqa: E501\n\n          # noqa: E501\n\n        :return: The payment_auth_state of this KomplettConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._payment_auth_state
	@payment_auth_state.setter
	def payment_auth_state(self,payment_auth_state):'Sets the payment_auth_state of this KomplettConnectorSettings.\n\n          # noqa: E501\n\n        :param payment_auth_state: The payment_auth_state of this KomplettConnectorSettings.  # noqa: E501\n        :type: str\n        ';self._payment_auth_state=payment_auth_state
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(KomplettConnectorSettings,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,KomplettConnectorSettings):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other