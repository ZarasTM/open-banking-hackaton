'\n    enable:Banking SDK\n\n    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501\n\n    API version: 0.3.0\n    Contact: hello@enablebanking.com\n    Generated by enable:Banking SDK generator using Swagger Codegen project\n'
_D='GenericLink'
_C='consent_approval'
_B='confirmation'
_A=None
import pprint,re,six
from enablebanking.models.generic_link import GenericLink
class PaymentRequestResourceCreationLinks:
	'NOTE: This class is auto generated by the swagger code generator program.\n\n    Do not edit the class manually.\n    ';'\n    Attributes:\n      swagger_types (dict): The key is attribute name\n                            and the value is attribute type.\n      attribute_map (dict): The key is attribute name\n                            and the value is json key in definition.\n    ';swagger_types={_C:_D,_B:_D};attribute_map={_C:'consentApproval',_B:_B}
	def __init__(A,consent_approval=_A,confirmation=_A):
		'PaymentRequestResourceCreationLinks - a model defined in Swagger';C=confirmation;B=consent_approval;A._consent_approval=_A;A._confirmation=_A;A.discriminator=_A
		if B is not _A:A.consent_approval=B
		if C is not _A:A.confirmation=C
	@property
	def consent_approval(self):'Gets the consent_approval of this PaymentRequestResourceCreationLinks.  # noqa: E501\n\n        URL to be used by the PISP in order to start the ASPSP authentication and consent management process   # noqa: E501\n\n        :return: The consent_approval of this PaymentRequestResourceCreationLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self._consent_approval
	@consent_approval.setter
	def consent_approval(self,consent_approval):'Sets the consent_approval of this PaymentRequestResourceCreationLinks.\n\n        URL to be used by the PISP in order to start the ASPSP authentication and consent management process   # noqa: E501\n\n        :param consent_approval: The consent_approval of this PaymentRequestResourceCreationLinks.  # noqa: E501\n        :type: GenericLink\n        ';self._consent_approval=consent_approval
	@property
	def confirmation(self):'Gets the confirmation of this PaymentRequestResourceCreationLinks.  # noqa: E501\n\n        Link to the payment confirmation API endpoint   # noqa: E501\n\n        :return: The confirmation of this PaymentRequestResourceCreationLinks.  # noqa: E501\n        :rtype: GenericLink\n        ';return self._confirmation
	@confirmation.setter
	def confirmation(self,confirmation):'Sets the confirmation of this PaymentRequestResourceCreationLinks.\n\n        Link to the payment confirmation API endpoint   # noqa: E501\n\n        :param confirmation: The confirmation of this PaymentRequestResourceCreationLinks.  # noqa: E501\n        :type: GenericLink\n        ';self._confirmation=confirmation
	def to_dict(D):
		'Returns the model properties as a dict';E='to_dict';B={}
		for (C,G) in six.iteritems(D.swagger_types):
			A=getattr(D,C)
			if isinstance(A,list):B[C]=list(map(lambda x:x.to_dict()if hasattr(x,E)else x,A))
			elif hasattr(A,E):B[C]=A.to_dict()
			elif isinstance(A,dict):B[C]=dict(map(lambda item:(item[0],item[1].to_dict())if hasattr(item[1],E)else item,A.items()))
			else:B[C]=A
		if issubclass(PaymentRequestResourceCreationLinks,dict):
			for (F,A) in D.items():B[F]=A
		return B
	def to_str(A):'Returns the string representation of the model';return pprint.pformat(A.to_dict())
	def __repr__(A):'For `print` and `pprint`';return A.to_str()
	def __eq__(B,other):
		'Returns true if both objects are equal';A=other
		if not isinstance(A,PaymentRequestResourceCreationLinks):return False
		return B.__dict__==A.__dict__
	def __ne__(A,other):'Returns true if both objects are not equal';return not A==other