'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_Y='AktiaConnectorSettings'
_X='PekaoConnectorSettings'
_W='POPPankkiConnectorSettings'
_V='SwedbankConnectorSettings'
_U='BNPParibasPolandConnectorSettings'
_T='NordeaConnectorSettings'
_S='SPankkiConnectorSettings'
_R='PKOConnectorSettings'
_Q='SEBConnectorSettings'
_P='YaConnectorSettings'
_O='KomplettConnectorSettings'
_N='LHVConnectorSettings'
_M='SEBSwedenConnectorSettings'
_L='AliorConnectorSettings'
_K='ResursConnectorSettings'
_J='AlandsbankenConnectorSettings'
_I='OPConnectorSettings'
_H='INGPolandConnectorSettings'
_G='refresh_token'
_F='access_token'
_E='consent_id'
_D='sandbox'
_C='str'
_B='connector'
_A=None
import pprint,re,six
class ConnectorSettings:
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_D:'bool',_E:_C,_F:_C,_G:_C,_B:_C};attribute_map={_D:_D,_E:'consentId',_F:'accessToken',_G:'refreshToken',_B:_B};discriminator_value_class_map={_H:_H,_I:_I,_J:_J,_K:_K,_L:_L,_M:_M,_N:_N,_O:_O,_P:_P,_Q:_Q,_R:_R,_S:_S,_T:_T,_U:_U,_V:_V,_W:_W,_X:_X,_Y:_Y}
	def __init__(A,sandbox=_A,consent_id=_A,access_token=_A,refresh_token=_A,connector=_A):'ConnectorSettings - a model defined in Swagger';A._sandbox=_A;A._consent_id=_A;A._access_token=_A;A._refresh_token=_A;A._connector=_A;A.discriminator=_B;A.sandbox=sandbox;A.consent_id=consent_id;A.access_token=access_token;A.refresh_token=refresh_token;A.connector=connector
	@property
	def sandbox(self):'Gets the sandbox of this ConnectorSettings.  # noqa: E501\n\n        Defines whether connect to sandbox or production APIs  # noqa: E501\n\n        :return: The sandbox of this ConnectorSettings.  # noqa: E501\n        :rtype: bool\n        ';return self._sandbox
	@sandbox.setter
	def sandbox(self,sandbox):
		'Sets the sandbox of this ConnectorSettings.\n\n        Defines whether connect to sandbox or production APIs  # noqa: E501\n\n        :param sandbox: The sandbox of this ConnectorSettings.  # noqa: E501\n        :type: bool\n        ';A=sandbox
		if A is _A:raise ValueError('Invalid value for `sandbox`, must not be `None`')
		self._sandbox=A
	@property
	def consent_id(self):'Gets the consent_id of this ConnectorSettings.  # noqa: E501\n\n        User consent identifier  # noqa: E501\n\n        :return: The consent_id of this ConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._consent_id
	@consent_id.setter
	def consent_id(self,consent_id):
		'Sets the consent_id of this ConnectorSettings.\n\n        User consent identifier  # noqa: E501\n\n        :param consent_id: The consent_id of this ConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=consent_id
		if A is _A:raise ValueError('Invalid value for `consent_id`, must not be `None`')
		self._consent_id=A
	@property
	def access_token(self):'Gets the access_token of this ConnectorSettings.  # noqa: E501\n\n        User access token  # noqa: E501\n\n        :return: The access_token of this ConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._access_token
	@access_token.setter
	def access_token(self,access_token):
		'Sets the access_token of this ConnectorSettings.\n\n        User access token  # noqa: E501\n\n        :param access_token: The access_token of this ConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=access_token
		if A is _A:raise ValueError('Invalid value for `access_token`, must not be `None`')
		self._access_token=A
	@property
	def refresh_token(self):'Gets the refresh_token of this ConnectorSettings.  # noqa: E501\n\n        User refresh token  # noqa: E501\n\n        :return: The refresh_token of this ConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._refresh_token
	@refresh_token.setter
	def refresh_token(self,refresh_token):
		'Sets the refresh_token of this ConnectorSettings.\n\n        User refresh token  # noqa: E501\n\n        :param refresh_token: The refresh_token of this ConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=refresh_token
		if A is _A:raise ValueError('Invalid value for `refresh_token`, must not be `None`')
		self._refresh_token=A
	@property
	def connector(self):'Gets the connector of this ConnectorSettings.  # noqa: E501\n\n        Connector identifier (discriminator)  # noqa: E501\n\n        :return: The connector of this ConnectorSettings.  # noqa: E501\n        :rtype: str\n        ';return self._connector
	@connector.setter
	def connector(self,connector):
		'Sets the connector of this ConnectorSettings.\n\n        Connector identifier (discriminator)  # noqa: E501\n\n        :param connector: The connector of this ConnectorSettings.  # noqa: E501\n        :type: str\n        ';A=connector
		if A is _A:raise ValueError('Invalid value for `connector`, must not be `None`')
		self._connector=A
	def get_real_child_model(A,data):'Returns the real base class specified by the discriminator';B=data[A.discriminator].lower();return A.discriminator_value_class_map.get(B)
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(ConnectorSettings,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,ConnectorSettings):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other