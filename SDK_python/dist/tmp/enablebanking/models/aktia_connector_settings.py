'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_G='sandbox_safeguard'
_F='sandbox_payment_id'
_E='tpp_redirect_uri'
_D='client_secret'
_C='client_id'
_B='str'
_A=None
import pprint,re,six
from enablebanking.models.connector_settings import ConnectorSettings
class AktiaConnectorSettings(ConnectorSettings):
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_C:_B,_D:_B,_E:_B,_F:_B,_G:'bool'};attribute_map={_C:'clientId',_D:'clientSecret',_E:'tppRedirectUri',_F:'sandboxPaymentId',_G:'sandboxSafeguard'}
	def __init__(A,client_id=_A,client_secret=_A,tpp_redirect_uri=_A,sandbox_payment_id=_A,sandbox_safeguard=_A):
		'AktiaConnectorSettings - a model defined in Swagger';D=sandbox_safeguard;C=sandbox_payment_id;B=tpp_redirect_uri;A._client_id=_A;A._client_secret=_A;A._tpp_redirect_uri=_A;A._sandbox_payment_id=_A;A._sandbox_safeguard=_A;A.discriminator=_A;A.client_id=client_id;A.client_secret=client_secret
		if B is not _A:A.tpp_redirect_uri=B
		if C is not _A:A.sandbox_payment_id=C
		if D is not _A:A.sandbox_safeguard=D
	@property
	def client_id(self):'Gets the client_id of this AktiaConnectorSettings.  # noqa: E501\n\n        API client ID (obtained from Aktia Developer Portal)  # noqa: E501\n\n        :return: The client_id of this AktiaConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._client_id
	@client_id.setter
	def client_id(self,client_id):
		'Sets the client_id of this AktiaConnectorSettings.\n\n        API client ID (obtained from Aktia Developer Portal)  # noqa: E501\n\n        :param client_id: The client_id of this AktiaConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=client_id
		if A is _A:raise ValueError('Invalid value for `client_id`, must not be `None`')
		self._client_id=A
	@property
	def client_secret(self):'Gets the client_secret of this AktiaConnectorSettings.  # noqa: E501\n\n        API client secret (obtained from Aktia Developer Portal)  # noqa: E501\n\n        :return: The client_secret of this AktiaConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._client_secret
	@client_secret.setter
	def client_secret(self,client_secret):
		'Sets the client_secret of this AktiaConnectorSettings.\n\n        API client secret (obtained from Aktia Developer Portal)  # noqa: E501\n\n        :param client_secret: The client_secret of this AktiaConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=client_secret
		if A is _A:raise ValueError('Invalid value for `client_secret`, must not be `None`')
		self._client_secret=A
	@property
	def tpp_redirect_uri(self):'Gets the tpp_redirect_uri of this AktiaConnectorSettings.  # noqa: E501\n\n          # noqa: E501\n\n        :return: The tpp_redirect_uri of this AktiaConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._tpp_redirect_uri
	@tpp_redirect_uri.setter
	def tpp_redirect_uri(self,tpp_redirect_uri):'Sets the tpp_redirect_uri of this AktiaConnectorSettings.\n\n          # noqa: E501\n\n        :param tpp_redirect_uri: The tpp_redirect_uri of this AktiaConnectorSettings.  # noqa: E501\n        :type: str\n        ';self._tpp_redirect_uri=tpp_redirect_uri
	@property
	def sandbox_payment_id(self):'Gets the sandbox_payment_id of this AktiaConnectorSettings.  # noqa: E501\n\n          # noqa: E501\n\n        :return: The sandbox_payment_id of this AktiaConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._sandbox_payment_id
	@sandbox_payment_id.setter
	def sandbox_payment_id(self,sandbox_payment_id):'Sets the sandbox_payment_id of this AktiaConnectorSettings.\n\n          # noqa: E501\n\n        :param sandbox_payment_id: The sandbox_payment_id of this AktiaConnectorSettings.  # noqa: E501\n        :type: str\n        ';self._sandbox_payment_id=sandbox_payment_id
	@property
	def sandbox_safeguard(self):'Gets the sandbox_safeguard of this AktiaConnectorSettings.  # noqa: E501\n\n          # noqa: E501\n\n        :return: The sandbox_safeguard of this AktiaConnectorSettings.  # noqa: E501\n        :rtype: bool\n        ';return self._sandbox_safeguard
	@sandbox_safeguard.setter
	def sandbox_safeguard(self,sandbox_safeguard):'Sets the sandbox_safeguard of this AktiaConnectorSettings.\n\n          # noqa: E501\n\n        :param sandbox_safeguard: The sandbox_safeguard of this AktiaConnectorSettings.  # noqa: E501\n        :type: bool\n        ';self._sandbox_safeguard=sandbox_safeguard
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(AktiaConnectorSettings,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,AktiaConnectorSettings):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other