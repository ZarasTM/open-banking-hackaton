from enablebanking.api_client import ApiException
class CoreException(ApiException):
	def __init__(A,code,message):super().__init__();A.code=code;A.message=message
	def __str__(A):return A.message
class HttpException(CoreException):
	def __init__(A,code,message,api_response):B=api_response;A.response_headers=[(A.name,A.value)for A in(B.headers)];A.response_body=B.content;super().__init__(code,message='%s %s.\nHeaders: %s,\nBody: %s'%(code,message,A.response_headers,A.response_body))
class DataRetrievalException(HttpException):0
class InsufficientScopeException(DataRetrievalException):0
class NotImplementedException(CoreException):0