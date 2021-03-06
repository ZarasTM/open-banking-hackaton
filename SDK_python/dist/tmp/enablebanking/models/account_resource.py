'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_O='links'
_N='psu_status'
_M='cash_account_type'
_L='linked_account'
_K='account_id'
_J='bic_fi'
_I='resource_id'
_H='balances'
_G='currency'
_F='product'
_E='usage'
_D='details'
_C='name'
_B='str'
_A=None
import pprint,re,six
from enablebanking.models.account_identification import AccountIdentification
from enablebanking.models.account_links import AccountLinks
from enablebanking.models.balance_resource import BalanceResource
from enablebanking.models.resource_id import ResourceId
class AccountResource:
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_I:'ResourceId',_J:_B,_K:'AccountIdentification',_C:_B,_D:_B,_L:_B,_E:_B,_M:_B,_F:_B,_G:_B,_H:'list[BalanceResource]',_N:_B,_O:'AccountLinks'};attribute_map={_I:'resourceId',_J:'bicFi',_K:'accountId',_C:_C,_D:_D,_L:'linkedAccount',_E:_E,_M:'cashAccountType',_F:_F,_G:_G,_H:_H,_N:'psuStatus',_O:'_links'}
	def __init__(A,resource_id=_A,bic_fi=_A,account_id=_A,name=_A,details=_A,linked_account=_A,usage=_A,cash_account_type=_A,product=_A,currency=_A,balances=_A,psu_status=_A,links=_A):
		'AccountResource - a model defined in Swagger';J=psu_status;I=balances;H=product;G=usage;F=linked_account;E=details;D=account_id;C=bic_fi;B=resource_id;A._resource_id=_A;A._bic_fi=_A;A._account_id=_A;A._name=_A;A._details=_A;A._linked_account=_A;A._usage=_A;A._cash_account_type=_A;A._product=_A;A._currency=_A;A._balances=_A;A._psu_status=_A;A._links=_A;A.discriminator=_A
		if B is not _A:A.resource_id=B
		if C is not _A:A.bic_fi=C
		if D is not _A:A.account_id=D
		A.name=name
		if E is not _A:A.details=E
		if F is not _A:A.linked_account=F
		if G is not _A:A.usage=G
		A.cash_account_type=cash_account_type
		if H is not _A:A.product=H
		A.currency=currency
		if I is not _A:A.balances=I
		if J is not _A:A.psu_status=J
		A.links=links
	@property
	def resource_id(self):'Gets the resource_id of this AccountResource.  # noqa: E501\n\n\n        :return: The resource_id of this AccountResource.  # noqa: E501\n        :rtype: ResourceId\n        ';return self._resource_id
	@resource_id.setter
	def resource_id(self,resource_id):'Sets the resource_id of this AccountResource.\n\n\n        :param resource_id: The resource_id of this AccountResource.  # noqa: E501\n        :type: ResourceId\n        ';self._resource_id=resource_id
	@property
	def bic_fi(self):'Gets the bic_fi of this AccountResource.  # noqa: E501\n\n        ISO20022: Code allocated to a financial institution by the ISO 9362 Registration Authority as described in ISO 9362 "Banking - Banking telecommunication messages - Business identification code (BIC)".   # noqa: E501\n\n        :return: The bic_fi of this AccountResource.  # noqa: E501\n        :rtype: str\n        ';return self._bic_fi
	@bic_fi.setter
	def bic_fi(self,bic_fi):
		'Sets the bic_fi of this AccountResource.\n\n        ISO20022: Code allocated to a financial institution by the ISO 9362 Registration Authority as described in ISO 9362 "Banking - Banking telecommunication messages - Business identification code (BIC)".   # noqa: E501\n\n        :param bic_fi: The bic_fi of this AccountResource.  # noqa: E501\n        :type: str\n        ';A=bic_fi
		if A is not _A and not re.search('^[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}$',A):raise ValueError('Invalid value for `bic_fi`, must be a follow pattern or equal to `/^[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}$/`')
		self._bic_fi=A
	@property
	def account_id(self):'Gets the account_id of this AccountResource.  # noqa: E501\n\n\n        :return: The account_id of this AccountResource.  # noqa: E501\n        :rtype: AccountIdentification\n        ';return self._account_id
	@account_id.setter
	def account_id(self,account_id):'Sets the account_id of this AccountResource.\n\n\n        :param account_id: The account_id of this AccountResource.  # noqa: E501\n        :type: AccountIdentification\n        ';self._account_id=account_id
	@property
	def name(self):'Gets the name of this AccountResource.  # noqa: E501\n\n        Label of the PSU account In case of a delayed debit card transaction set, the name shall specify the holder name and the imputation date   # noqa: E501\n\n        :return: The name of this AccountResource.  # noqa: E501\n        :rtype: str\n        ';return self._name
	@name.setter
	def name(self,name):
		'Sets the name of this AccountResource.\n\n        Label of the PSU account In case of a delayed debit card transaction set, the name shall specify the holder name and the imputation date   # noqa: E501\n\n        :param name: The name of this AccountResource.  # noqa: E501\n        :type: str\n        ';A=name
		if A is _A:raise ValueError('Invalid value for `name`, must not be `None`')
		if A is not _A and len(A)>70:raise ValueError('Invalid value for `name`, length must be less than or equal to `70`')
		self._name=A
	@property
	def details(self):'Gets the details of this AccountResource.  # noqa: E501\n\n        Specifications that might be provided by the ASPSP - characteristics of the account - characteristics of the relevant card   # noqa: E501\n\n        :return: The details of this AccountResource.  # noqa: E501\n        :rtype: str\n        ';return self._details
	@details.setter
	def details(self,details):
		'Sets the details of this AccountResource.\n\n        Specifications that might be provided by the ASPSP - characteristics of the account - characteristics of the relevant card   # noqa: E501\n\n        :param details: The details of this AccountResource.  # noqa: E501\n        :type: str\n        ';A=details
		if A is not _A and len(A)>140:raise ValueError('Invalid value for `details`, length must be less than or equal to `140`')
		self._details=A
	@property
	def linked_account(self):'Gets the linked_account of this AccountResource.  # noqa: E501\n\n        Case of a set of pending card transactions, the APSP will provide the relevant cash account the card is set up on.  # noqa: E501\n\n        :return: The linked_account of this AccountResource.  # noqa: E501\n        :rtype: str\n        ';return self._linked_account
	@linked_account.setter
	def linked_account(self,linked_account):
		'Sets the linked_account of this AccountResource.\n\n        Case of a set of pending card transactions, the APSP will provide the relevant cash account the card is set up on.  # noqa: E501\n\n        :param linked_account: The linked_account of this AccountResource.  # noqa: E501\n        :type: str\n        ';A=linked_account
		if A is not _A and len(A)>70:raise ValueError('Invalid value for `linked_account`, length must be less than or equal to `70`')
		self._linked_account=A
	@property
	def usage(self):'Gets the usage of this AccountResource.  # noqa: E501\n\n        Specifies the usage of the account  # noqa: E501\n\n        :return: The usage of this AccountResource.  # noqa: E501\n        :rtype: str\n        ';return self._usage
	@usage.setter
	def usage(self,usage):
		'Sets the usage of this AccountResource.\n\n        Specifies the usage of the account  # noqa: E501\n\n        :param usage: The usage of this AccountResource.  # noqa: E501\n        :type: str\n        ';A=usage;B=['PRIV','ORGA']
		if A not in B:raise ValueError('Invalid value for `usage` ({0}), must be one of {1}'.format(A,B))
		self._usage=A
	@property
	def cash_account_type(self):'Gets the cash_account_type of this AccountResource.  # noqa: E501\n\n        Specifies the type of the account  # noqa: E501\n\n        :return: The cash_account_type of this AccountResource.  # noqa: E501\n        :rtype: str\n        ';return self._cash_account_type
	@cash_account_type.setter
	def cash_account_type(self,cash_account_type):
		'Sets the cash_account_type of this AccountResource.\n\n        Specifies the type of the account  # noqa: E501\n\n        :param cash_account_type: The cash_account_type of this AccountResource.  # noqa: E501\n        :type: str\n        ';A=cash_account_type
		if A is _A:raise ValueError('Invalid value for `cash_account_type`, must not be `None`')
		B=['CACC','CASH','CARD','LOAN']
		if A not in B:raise ValueError('Invalid value for `cash_account_type` ({0}), must be one of {1}'.format(A,B))
		self._cash_account_type=A
	@property
	def product(self):'Gets the product of this AccountResource.  # noqa: E501\n\n        Product Name of the Bank for this account, proprietary definition   # noqa: E501\n\n        :return: The product of this AccountResource.  # noqa: E501\n        :rtype: str\n        ';return self._product
	@product.setter
	def product(self,product):
		'Sets the product of this AccountResource.\n\n        Product Name of the Bank for this account, proprietary definition   # noqa: E501\n\n        :param product: The product of this AccountResource.  # noqa: E501\n        :type: str\n        ';A=product
		if A is not _A and len(A)>35:raise ValueError('Invalid value for `product`, length must be less than or equal to `35`')
		self._product=A
	@property
	def currency(self):'Gets the currency of this AccountResource.  # noqa: E501\n\n        Currency used for the account  # noqa: E501\n\n        :return: The currency of this AccountResource.  # noqa: E501\n        :rtype: str\n        ';return self._currency
	@currency.setter
	def currency(self,currency):
		'Sets the currency of this AccountResource.\n\n        Currency used for the account  # noqa: E501\n\n        :param currency: The currency of this AccountResource.  # noqa: E501\n        :type: str\n        ';A=currency
		if A is _A:raise ValueError('Invalid value for `currency`, must not be `None`')
		if A is not _A and len(A)>3:raise ValueError('Invalid value for `currency`, length must be less than or equal to `3`')
		self._currency=A
	@property
	def balances(self):'Gets the balances of this AccountResource.  # noqa: E501\n\n        list of balances provided by the ASPSP  # noqa: E501\n\n        :return: The balances of this AccountResource.  # noqa: E501\n        :rtype: list[BalanceResource]\n        ';return self._balances
	@balances.setter
	def balances(self,balances):'Sets the balances of this AccountResource.\n\n        list of balances provided by the ASPSP  # noqa: E501\n\n        :param balances: The balances of this AccountResource.  # noqa: E501\n        :type: list[BalanceResource]\n        ';self._balances=balances
	@property
	def psu_status(self):'Gets the psu_status of this AccountResource.  # noqa: E501\n\n        Relationship between the PSU and the account - Account Holder - Co-account Holder - Attorney  # noqa: E501\n\n        :return: The psu_status of this AccountResource.  # noqa: E501\n        :rtype: str\n        ';return self._psu_status
	@psu_status.setter
	def psu_status(self,psu_status):
		'Sets the psu_status of this AccountResource.\n\n        Relationship between the PSU and the account - Account Holder - Co-account Holder - Attorney  # noqa: E501\n\n        :param psu_status: The psu_status of this AccountResource.  # noqa: E501\n        :type: str\n        ';A=psu_status
		if A is not _A and len(A)>35:raise ValueError('Invalid value for `psu_status`, length must be less than or equal to `35`')
		self._psu_status=A
	@property
	def links(self):'Gets the links of this AccountResource.  # noqa: E501\n\n\n        :return: The links of this AccountResource.  # noqa: E501\n        :rtype: AccountLinks\n        ';return self._links
	@links.setter
	def links(self,links):
		'Sets the links of this AccountResource.\n\n\n        :param links: The links of this AccountResource.  # noqa: E501\n        :type: AccountLinks\n        ';A=links
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
		if issubclass(AccountResource,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,AccountResource):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other