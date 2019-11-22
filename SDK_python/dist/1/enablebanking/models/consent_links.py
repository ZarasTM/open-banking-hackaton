'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_E='_self'
_D='GenericLink'
_C='status'
_B='redirect'
_A=None
import pprint,re,six
from enablebanking.models.generic_link import GenericLink
class ConsentLinks:
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_B:_D,_E:_D,_C:_D};attribute_map={_B:_B,_E:'self',_C:_C}
	def __init__(A,redirect=_A,_self=_A,status=_A):
		'ConsentLinks - a model defined in Swagger';D=status;C=_self;B=redirect;A._redirect=_A;A.__self=_A;A._status=_A;A.discriminator=_A
		if B is not _A:A.redirect=B
		if C is not _A:A._self=C
		if D is not _A:A.status=D
	@property
	def redirect(self):'Gets the redirect of this ConsentLinks.  # noqa: E501\n\n\n        :return: The redirect of this ConsentLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self._redirect
	@redirect.setter
	def redirect(self,redirect):'Sets the redirect of this ConsentLinks.\n\n\n        :param redirect: The redirect of this ConsentLinks.  # noqa: E501\n        :type: GenericLink\n        ';self._redirect=redirect
	@property
	def _self(self):'Gets the _self of this ConsentLinks.  # noqa: E501\n\n\n        :return: The _self of this ConsentLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self.__self
	@_self.setter
	def _self(self,_self):'Sets the _self of this ConsentLinks.\n\n\n        :param _self: The _self of this ConsentLinks.  # noqa: E501\n        :type: GenericLink\n        ';self.__self=_self
	@property
	def status(self):'Gets the status of this ConsentLinks.  # noqa: E501\n\n\n        :return: The status of this ConsentLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self._status
	@status.setter
	def status(self,status):'Sets the status of this ConsentLinks.\n\n\n        :param status: The status of this ConsentLinks.  # noqa: E501\n        :type: GenericLink\n        ';self._status=status
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(ConsentLinks,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,ConsentLinks):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other