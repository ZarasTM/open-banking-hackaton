'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_G='scope'
_F='refresh_token'
_E='expires_in'
_D='token_type'
_C='access_token'
_B='str'
_A=None
import pprint,re,six
class Token:
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_C:_B,_D:_B,_E:'int',_F:_B,_G:_B};attribute_map={_C:_C,_D:_D,_E:_E,_F:_F,_G:_G}
	def __init__(A,access_token=_A,token_type=_A,expires_in=_A,refresh_token=_A,scope=_A):
		'Token - a model defined in Swagger';F=scope;E=refresh_token;D=expires_in;C=token_type;B=access_token;A._access_token=_A;A._token_type=_A;A._expires_in=_A;A._refresh_token=_A;A._scope=_A;A.discriminator=_A
		if B is not _A:A.access_token=B
		if C is not _A:A.token_type=C
		if D is not _A:A.expires_in=D
		if E is not _A:A.refresh_token=E
		if F is not _A:A.scope=F
	@property
	def access_token(self):'Gets the access_token of this Token.  # noqa: E501\n\n        The access token value  # noqa: E501\n\n        :return: The access_token of this Token.  # noqa: E501\n        :rtype: str\n        ';return self._access_token
	@access_token.setter
	def access_token(self,access_token):'Sets the access_token of this Token.\n\n        The access token value  # noqa: E501\n\n        :param access_token: The access_token of this Token.  # noqa: E501\n        :type: str\n        ';self._access_token=access_token
	@property
	def token_type(self):'Gets the token_type of this Token.  # noqa: E501\n\n        Type of the token is set to "Bearer"  # noqa: E501\n\n        :return: The token_type of this Token.  # noqa: E501\n        :rtype: str\n        ';return self._token_type
	@token_type.setter
	def token_type(self,token_type):
		'Sets the token_type of this Token.\n\n        Type of the token is set to "Bearer"  # noqa: E501\n\n        :param token_type: The token_type of this Token.  # noqa: E501\n        :type: str\n        ';A=token_type;B=['Bearer']
		if A not in B:raise ValueError('Invalid value for `token_type` ({0}), must be one of {1}'.format(A,B))
		self._token_type=A
	@property
	def expires_in(self):'Gets the expires_in of this Token.  # noqa: E501\n\n        The lifetime in seconds of the access token  # noqa: E501\n\n        :return: The expires_in of this Token.  # noqa: E501\n        :rtype: int\n        ';return self._expires_in
	@expires_in.setter
	def expires_in(self,expires_in):'Sets the expires_in of this Token.\n\n        The lifetime in seconds of the access token  # noqa: E501\n\n        :param expires_in: The expires_in of this Token.  # noqa: E501\n        :type: int\n        ';self._expires_in=expires_in
	@property
	def refresh_token(self):'Gets the refresh_token of this Token.  # noqa: E501\n\n        The refresh token value  # noqa: E501\n\n        :return: The refresh_token of this Token.  # noqa: E501\n        :rtype: str\n        ';return self._refresh_token
	@refresh_token.setter
	def refresh_token(self,refresh_token):'Sets the refresh_token of this Token.\n\n        The refresh token value  # noqa: E501\n\n        :param refresh_token: The refresh_token of this Token.  # noqa: E501\n        :type: str\n        ';self._refresh_token=refresh_token
	@property
	def scope(self):'Gets the scope of this Token.  # noqa: E501\n\n        Scopes of the token  # noqa: E501\n\n        :return: The scope of this Token.  # noqa: E501\n        :rtype: str\n        ';return self._scope
	@scope.setter
	def scope(self,scope):'Sets the scope of this Token.\n\n        Scopes of the token  # noqa: E501\n\n        :param scope: The scope of this Token.  # noqa: E501\n        :type: str\n        ';self._scope=scope
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(Token,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,Token):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other