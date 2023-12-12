import logging.config
from astpy.ast_processor import AstProcessor
from astpy.basic_info_listener import BasicInfoListener
import json

if __name__ == '__main__':
    #logging_setting_path = '../resources/logging/utiltools_log.conf'
    #logging.config.fileConfig(logging_setting_path)
    logger = logging.getLogger(__file__)

    target_file_path = '/home/kato/GPTSniffer/ANTLR/src/test.java'

    ast_info = AstProcessor(logging, BasicInfoListener()).execute(target_file_path)
    print(ast_info)

