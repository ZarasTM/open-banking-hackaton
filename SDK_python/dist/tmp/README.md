# enable:Banking SDK

Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts. 

This Python package is automatically generated by the enable:Banking SDK generator
using [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- Interface version: 0.3.0
- Core version: 0.1.0
- Package version: 0.3.0
- Build package: com.enablebanking.codegen.PythonClient
- Configuration: OpenBankingHackathonPL

For more information, please visit [https://enablebanking.com](https://enablebanking.com)

## Requirements

Python 3.4+

## Installation & Usage

### pip install

```sh
pip install enablebanking-0.3.0-py3-none-any.whl
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## Author

hello@enablebanking.com

