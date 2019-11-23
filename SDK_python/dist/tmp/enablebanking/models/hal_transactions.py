'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_C='links'
_B='transactions'
_A=None
import pprint,re,six
from enablebanking.models.transaction import Transaction
from enablebanking.models.transactions_links import TransactionsLinks
class HalTransactions:
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_B:'list[Transaction]',_C:'TransactionsLinks'};attribute_map={_B:_B,_C:'_links'}
	def __init__(A,transactions=_A,links=_A):'HalTransactions - a model defined in Swagger';A._transactions=_A;A._links=_A;A.discriminator=_A;A.transactions=transactions;A.links=links
	@property
	def transactions(self):'Gets the transactions of this HalTransactions.  # noqa: E501\n\n        List of transactions  # noqa: E501\n\n        :return: The transactions of this HalTransactions.  # noqa: E501\n        :rtype: list[Transaction]\n        ';return self._transactions
	@transactions.setter
	def transactions(self,transactions):
		'Sets the transactions of this HalTransactions.\n\n        List of transactions  # noqa: E501\n\n        :param transactions: The transactions of this HalTransactions.  # noqa: E501\n        :type: list[Transaction]\n        ';A=transactions
		if A is _A:raise ValueError('Invalid value for `transactions`, must not be `None`')
		self._transactions=A
	@property
	def links(self):'Gets the links of this HalTransactions.  # noqa: E501\n\n\n        :return: The links of this HalTransactions.  # noqa: E501\n        :rtype: TransactionsLinks\n        ';return self._links
	@links.setter
	def links(self,links):
		'Sets the links of this HalTransactions.\n\n\n        :param links: The links of this HalTransactions.  # noqa: E501\n        :type: TransactionsLinks\n        ';A=links
		if A is _A:raise ValueError('Invalid value for `links`, must not be `None`')
		self._links=A
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(HalTransactions,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,HalTransactions):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other