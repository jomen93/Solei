import os
import uuid
import sys 

from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings

account_name = ""
account_key  = ""


def initialize_storage_account(account_name, account_key):
	try:
		global service_client

		service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)

	except Exception as e:
		print(e)