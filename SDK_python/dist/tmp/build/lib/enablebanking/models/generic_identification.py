'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_E='scheme_name'
_D='str'
_C='issuer'
_B='identification'
_A=None
import pprint,re,six
class GenericIdentification:
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_B:_D,_E:_D,_C:_D};attribute_map={_B:_B,_E:'schemeName',_C:_C}
	def __init__(A,identification=_A,scheme_name=_A,issuer=_A):
		'GenericIdentification - a model defined in Swagger';B=issuer;A._identification=_A;A._scheme_name=_A;A._issuer=_A;A.discriminator=_A;A.identification=identification;A.scheme_name=scheme_name
		if B is not _A:A.issuer=B
	@property
	def identification(self):'Gets the identification of this GenericIdentification.  # noqa: E501\n\n        API Identifier  # noqa: E501\n\n        :return: The identification of this GenericIdentification.  # noqa: E501\n        :rtype: str\n        ';return self._identification
	@identification.setter
	def identification(self,identification):
		'Sets the identification of this GenericIdentification.\n\n        API Identifier  # noqa: E501\n\n        :param identification: The identification of this GenericIdentification.  # noqa: E501\n        :type: str\n        ';A=identification
		if A is _A:raise ValueError('Invalid value for `identification`, must not be `None`')
		if A is not _A and len(A)>70:raise ValueError('Invalid value for `identification`, length must be less than or equal to `70`')
		self._identification=A
	@property
	def scheme_name(self):'Gets the scheme_name of this GenericIdentification.  # noqa: E501\n\n        Name of the identification scheme. Partially based on ISO20022 external code list  # noqa: E501\n\n        :return: The scheme_name of this GenericIdentification.  # noqa: E501\n        :rtype: str\n        ';return self._scheme_name
	@scheme_name.setter
	def scheme_name(self,scheme_name):
		'Sets the scheme_name of this GenericIdentification.\n\n        Name of the identification scheme. Partially based on ISO20022 external code list  # noqa: E501\n\n        :param scheme_name: The scheme_name of this GenericIdentification.  # noqa: E501\n        :type: str\n        ';A=scheme_name
		if A is _A:raise ValueError('Invalid value for `scheme_name`, must not be `None`')
		B=['BANK','COID','SREN','SRET','NIDN','OAUT','CPAN','BBAN']
		if A not in B:raise ValueError('Invalid value for `scheme_name` ({0}), must be one of {1}'.format(A,B))
		self._scheme_name=A
	@property
	def issuer(self):'Gets the issuer of this GenericIdentification.  # noqa: E501\n\n        ISO20022: Entity that assigns the identification. this could a country code or any organisation name or identifier that can be recognized by both parties   # noqa: E501\n\n        :return: The issuer of this GenericIdentification.  # noqa: E501\n        :rtype: str\n        ';return self._issuer
	@issuer.setter
	def issuer(self,issuer):
		'Sets the issuer of this GenericIdentification.\n\n        ISO20022: Entity that assigns the identification. this could a country code or any organisation name or identifier that can be recognized by both parties   # noqa: E501\n\n        :param issuer: The issuer of this GenericIdentification.  # noqa: E501\n        :type: str\n        ';A=issuer
		if A is not _A and len(A)>35:raise ValueError('Invalid value for `issuer`, length must be less than or equal to `35`')
		self._issuer=A
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(GenericIdentification,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,GenericIdentification):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other