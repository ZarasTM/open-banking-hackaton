'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_H='parent_list'
_G='_self'
_F='prev'
_E='next'
_D='last'
_C='first'
_B='GenericLink'
_A=None
import pprint,re,six
from enablebanking.models.generic_link import GenericLink
class BeneficiariesLinks:
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_G:_B,_H:_B,_C:_B,_D:_B,_E:_B,_F:_B};attribute_map={_G:'self',_H:'parent-list',_C:_C,_D:_D,_E:_E,_F:_F}
	def __init__(A,_self=_A,parent_list=_A,first=_A,last=_A,next=_A,prev=_A):
		'BeneficiariesLinks - a model defined in Swagger';C=first;B=parent_list;A.__self=_A;A._parent_list=_A;A._first=_A;A._last=_A;A._next=_A;A._prev=_A;A.discriminator=_A;A._self=_self
		if B is not _A:A.parent_list=B
		if C is not _A:A.first=C
		if last is not _A:A.last=last
		if next is not _A:A.next=next
		if prev is not _A:A.prev=prev
	@property
	def _self(self):'Gets the _self of this BeneficiariesLinks.  # noqa: E501\n\n        link to the beneficiaries  # noqa: E501\n\n        :return: The _self of this BeneficiariesLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self.__self
	@_self.setter
	def _self(self,_self):
		'Sets the _self of this BeneficiariesLinks.\n\n        link to the beneficiaries  # noqa: E501\n\n        :param _self: The _self of this BeneficiariesLinks.  # noqa: E501\n        :type: GenericLink\n        ';A=_self
		if A is _A:raise ValueError('Invalid value for `_self`, must not be `None`')
		self.__self=A
	@property
	def parent_list(self):'Gets the parent_list of this BeneficiariesLinks.  # noqa: E501\n\n        link to the list of all available accounts  # noqa: E501\n\n        :return: The parent_list of this BeneficiariesLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self._parent_list
	@parent_list.setter
	def parent_list(self,parent_list):'Sets the parent_list of this BeneficiariesLinks.\n\n        link to the list of all available accounts  # noqa: E501\n\n        :param parent_list: The parent_list of this BeneficiariesLinks.  # noqa: E501\n        :type: GenericLink\n        ';self._parent_list=parent_list
	@property
	def first(self):'Gets the first of this BeneficiariesLinks.  # noqa: E501\n\n        link to the first page of the beneficiaries result  # noqa: E501\n\n        :return: The first of this BeneficiariesLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self._first
	@first.setter
	def first(self,first):'Sets the first of this BeneficiariesLinks.\n\n        link to the first page of the beneficiaries result  # noqa: E501\n\n        :param first: The first of this BeneficiariesLinks.  # noqa: E501\n        :type: GenericLink\n        ';self._first=first
	@property
	def last(self):'Gets the last of this BeneficiariesLinks.  # noqa: E501\n\n        link to the last page of the beneficiaries result  # noqa: E501\n\n        :return: The last of this BeneficiariesLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self._last
	@last.setter
	def last(self,last):'Sets the last of this BeneficiariesLinks.\n\n        link to the last page of the beneficiaries result  # noqa: E501\n\n        :param last: The last of this BeneficiariesLinks.  # noqa: E501\n        :type: GenericLink\n        ';self._last=last
	@property
	def next(self):'Gets the next of this BeneficiariesLinks.  # noqa: E501\n\n        link to the next page of the beneficiaries result  # noqa: E501\n\n        :return: The next of this BeneficiariesLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self._next
	@next.setter
	def next(self,next):'Sets the next of this BeneficiariesLinks.\n\n        link to the next page of the beneficiaries result  # noqa: E501\n\n        :param next: The next of this BeneficiariesLinks.  # noqa: E501\n        :type: GenericLink\n        ';self._next=next
	@property
	def prev(self):'Gets the prev of this BeneficiariesLinks.  # noqa: E501\n\n        link to the previous page of the beneficiaries result  # noqa: E501\n\n        :return: The prev of this BeneficiariesLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self._prev
	@prev.setter
	def prev(self,prev):'Sets the prev of this BeneficiariesLinks.\n\n        link to the previous page of the beneficiaries result  # noqa: E501\n\n        :param prev: The prev of this BeneficiariesLinks.  # noqa: E501\n        :type: GenericLink\n        ';self._prev=prev
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(BeneficiariesLinks,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,BeneficiariesLinks):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other