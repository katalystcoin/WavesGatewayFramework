"""
Collection of common tokens in th Application.
"""

import pywaves
from waves_gateway.model import KeyPair
from .injector import InjectionToken
from pymongo.collection import Collection

LOGGING_HANDLER_LIST = InjectionToken('LOGGING_HANDLER_LIST', list)
MANAGED_LOGGER_LIST = InjectionToken('MANAGED_LOGGER_LIST', list)
POLLING_DELAY_SECONDS = InjectionToken('POLLING_DELAY_SECONDS', float)
CUSTOM_CURRENCY_NAME = InjectionToken('CUSTOM_CURRENCY_NAME', str)
GATEWAY_OWNER_ADDRESS = InjectionToken('GATEWAY_OWNER_ADDRESS', str)
WALLET_STORAGE_COLLECTION_NAME = InjectionToken('WALLET_STORAGE_COLLECTION_NAME', str)
MAP_STORAGE_COLLECTION_NAME = InjectionToken('MAP_STORAGE_COLLECTION_NAME', str)
KEY_VALUE_STORAGE_COLLECTION_NAME = InjectionToken('KEY_VALUE_STORAGE_COLLECTION_NAME', str)
TRANSACTION_ATTEMPT_LIST_STORAGE_COLLECTION_NAME = InjectionToken('TRANSACTION_ATTEMPT_LIST_STORAGE_COLLECTION_NAME',
                                                                  str)
GATEWAY_COIN_ADDRESS_SECRET = InjectionToken('GATEWAY_COIN_ADDRESS_SECRET', KeyPair)
GATEWAY_COIN_ADDRESS = InjectionToken('GATEWAY_COIN_ADDRESS', str)
WAVES_NODE = InjectionToken('WAVES_NODE', str)
COIN_NODE = InjectionToken('COIN_NODE', str)
WAVES_ASSET_ID = InjectionToken('WAVES_ASSET_ID', str)
WAVES_CHAIN = InjectionToken('WAVES_CHAIN', str)
ONLY_ONE_TRANSACTION_RECEIVER = InjectionToken('ONLY_ONE_TRANSACTION_RECEIVER', bool)
COIN_TRANSACTION_WEB_LINK = InjectionToken('COIN_TRANSACTION_WEB_LINK', str)
WAVES_TRANSACTION_WEB_LINK = InjectionToken('WAVES_TRANSACTION_WEB_LINK', str)
COIN_ADDRESS_WEB_LINK = InjectionToken('COIN_ADDRESS_WEB_LINK', str)
WAVES_ADDRESS_WEB_LINK = InjectionToken('WAVES_ADDRESS_WEB_LINK', str)
ATTEMPT_LIST_MAX_COMPLETION_TRIES = InjectionToken('ATTEMPT_LIST_MAX_COMPLETION_TRIES', int)
GATEWAY_WAVES_ADDRESS_SECRET = InjectionToken('GATEWAY_WAVES_ADDRESS_SECRET', KeyPair)
GATEWAY_WAVES_ADDRESS = InjectionToken('GATEWAY_WAVES_ADDRESS', str)
NUM_ATTEMPT_LIST_WORKERS = InjectionToken('NUM_ATTEMPT_LIST_WORKERS', int)
GATEWAY_HOST = InjectionToken('GATEWAY_HOST', str)
GATEWAY_PORT = InjectionToken('GATEWAY_PORT', int)
WALLET_STORAGE_COLLECTION = InjectionToken('WALLET_STORAGE_COLLECTION', Collection)
MAP_STORAGE_COLLECTION = InjectionToken('MAP_STORAGE_COLLECTION', Collection)
KEY_VALUE_STORAGE_COLLECTION = InjectionToken('KEY_VALUE_STORAGE_COLLECTION', Collection)
TRANSACTION_ATTEMPT_LIST_STORAGE_COLLECTION = InjectionToken('TRANSACTION_ATTEMPT_LIST_STORAGE_COLLECTION', Collection)
GATEWAY_PYWAVES_ADDRESS = InjectionToken('GATEWAY_PYWAVES_ADDRESS', pywaves.Address)
COIN_CHAIN_QUERY_SERVICE_CONVERTER_PROXY = InjectionToken('COIN_CHAIN_QUERY_SERVICE_CONVERTER_PROXY')
WAVES_CHAIN_QUERY_SERVICE_CONVERTER_PROXY = InjectionToken('WAVES_CHAIN_QUERY_SERVICE_CONVERTER_PROXY')
FLASK_NAME = InjectionToken('FLASK_NAME', str)
COIN_MAX_HANDLE_TRANSACTION_TRIES = InjectionToken('COIN_MAX_HANDLE_TRANSACTION_TRIES', int)
WAVES_MAX_HANDLE_TRANSACTION_TRIES = InjectionToken('WAVES_MAX_HANDLE_TRANSACTION_TRIES', int)
WAVES_LAST_BLOCK_DISTANCE = InjectionToken('WAVES_LAST_BLOCK_DISTANCE', int)
COIN_LAST_BLOCK_DISTANCE = InjectionToken('COIN_LAST_BLOCK_DISTANCE', int)
WEB_PRIMARY_COLOR = InjectionToken('WEB_PRIMARY_COLOR', str)