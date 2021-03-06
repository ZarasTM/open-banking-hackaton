'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_F='key_path'
_E='cert_path'
_D='client_secret'
_C='client_id'
_B='str'
_A=None
import pprint,re,six
from enablebanking.models.connector_settings import ConnectorSettings
class SEBSwedenConnectorSettings(ConnectorSettings):
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_C:_B,_D:_B,_E:_B,_F:_B};attribute_map={_C:'clientId',_D:'clientSecret',_E:'certPath',_F:'keyPath'}
	def __init__(A,client_id=_A,client_secret=_A,cert_path=_A,key_path=_A):'SEBSwedenConnectorSettings - a model defined in Swagger';A._client_id=_A;A._client_secret=_A;A._cert_path=_A;A._key_path=_A;A.discriminator=_A;A.client_id=client_id;A.client_secret=client_secret;A.cert_path=cert_path;A.key_path=key_path
	@property
	def client_id(self):'Gets the client_id of this SEBSwedenConnectorSettings.  # noqa: E501\n\n        API client ID (obtained from SEB Developer Portal)  # noqa: E501\n\n        :return: The client_id of this SEBSwedenConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._client_id
	@client_id.setter
	def client_id(self,client_id):
		'Sets the client_id of this SEBSwedenConnectorSettings.\n\n        API client ID (obtained from SEB Developer Portal)  # noqa: E501\n\n        :param client_id: The client_id of this SEBSwedenConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=client_id
		if A is _A:raise ValueError('Invalid value for `client_id`, must not be `None`')
		self._client_id=A
	@property
	def client_secret(self):'Gets the client_secret of this SEBSwedenConnectorSettings.  # noqa: E501\n\n        API client secret (obtained from SEB Developer Portal)  # noqa: E501\n\n        :return: The client_secret of this SEBSwedenConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._client_secret
	@client_secret.setter
	def client_secret(self,client_secret):
		'Sets the client_secret of this SEBSwedenConnectorSettings.\n\n        API client secret (obtained from SEB Developer Portal)  # noqa: E501\n\n        :param client_secret: The client_secret of this SEBSwedenConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=client_secret
		if A is _A:raise ValueError('Invalid value for `client_secret`, must not be `None`')
		self._client_secret=A
	@property
	def cert_path(self):'Gets the cert_path of this SEBSwedenConnectorSettings.  # noqa: E501\n\n        Path to QWAC certificate in PEM format. Test certificate (for accessing sandbox environment) is available here: https://github.com/sebgroup/openbanking/tree/master/psd2testcertificates   # noqa: E501\n\n        :return: The cert_path of this SEBSwedenConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._cert_path
	@cert_path.setter
	def cert_path(self,cert_path):
		'Sets the cert_path of this SEBSwedenConnectorSettings.\n\n        Path to QWAC certificate in PEM format. Test certificate (for accessing sandbox environment) is available here: https://github.com/sebgroup/openbanking/tree/master/psd2testcertificates   # noqa: E501\n\n        :param cert_path: The cert_path of this SEBSwedenConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=cert_path
		if A is _A:raise ValueError('Invalid value for `cert_path`, must not be `None`')
		self._cert_path=A
	@property
	def key_path(self):'Gets the key_path of this SEBSwedenConnectorSettings.  # noqa: E501\n\n        Path to QWAC certificate private key in PEM format.   # noqa: E501\n\n        :return: The key_path of this SEBSwedenConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._key_path
	@key_path.setter
	def key_path(self,key_path):
		'Sets the key_path of this SEBSwedenConnectorSettings.\n\n        Path to QWAC certificate private key in PEM format.   # noqa: E501\n\n        :param key_path: The key_path of this SEBSwedenConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=key_path
		if A is _A:raise ValueError('Invalid value for `key_path`, must not be `None`')
		self._key_path=A
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(SEBSwedenConnectorSettings,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,SEBSwedenConnectorSettings):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other