'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_D='str'
_C='sub_code'
_B='code'
_A=None
import pprint,re,six
class BankTransactionCode:
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_B:_D,_C:_D};attribute_map={_B:_B,_C:'subCode'}
	def __init__(A,code=_A,sub_code=_A):
		'BankTransactionCode - a model defined in Swagger';B=sub_code;A._code=_A;A._sub_code=_A;A.discriminator=_A
		if code is not _A:A.code=code
		if B is not _A:A.sub_code=B
	@property
	def code(self):'Gets the code of this BankTransactionCode.  # noqa: E501\n\n        ISO20022: Specifies the family of a transaction within the domain   # noqa: E501\n\n        :return: The code of this BankTransactionCode.  # noqa: E501\n        :rtype: str\n        ';return self._code
	@code.setter
	def code(self,code):
		'Sets the code of this BankTransactionCode.\n\n        ISO20022: Specifies the family of a transaction within the domain   # noqa: E501\n\n        :param code: The code of this BankTransactionCode.  # noqa: E501\n        :type: str\n        ';A=code
		if A is not _A and len(A)>4:raise ValueError('Invalid value for `code`, length must be less than or equal to `4`')
		self._code=A
	@property
	def sub_code(self):'Gets the sub_code of this BankTransactionCode.  # noqa: E501\n\n        ISO20022: Specifies the sub-product family of a transaction within a specific family   # noqa: E501\n\n        :return: The sub_code of this BankTransactionCode.  # noqa: E501\n        :rtype: str\n        ';return self._sub_code
	@sub_code.setter
	def sub_code(self,sub_code):
		'Sets the sub_code of this BankTransactionCode.\n\n        ISO20022: Specifies the sub-product family of a transaction within a specific family   # noqa: E501\n\n        :param sub_code: The sub_code of this BankTransactionCode.  # noqa: E501\n        :type: str\n        ';A=sub_code
		if A is not _A and len(A)>4:raise ValueError('Invalid value for `sub_code`, length must be less than or equal to `4`')
		self._sub_code=A
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(BankTransactionCode,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,BankTransactionCode):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other