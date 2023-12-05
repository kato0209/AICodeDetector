import logging.config
from astpy.ast_processor import AstProcessor
from astpy.basic_info_listener import BasicInfoListener
import json

def create_java_file(data):
    lines = []

    # パッケージ宣言
    lines.append(f'package {data["packageName"]};\n')

    # インポート文
    for imp in data["imports"]:
        lines.append(f'import {imp};')
    lines.append('')  # 空行

    # クラス宣言
    extends = f' extends {data["extends"]}' if data["extends"] else ''
    implements = ' implements ' + ', '.join(data["implements"]) if data["implements"] else ''
    lines.append(f'@Service')
    lines.append(f'@Transactional')
    lines.append(f'public class {data["className"]}{extends}{implements} {{\n')

    # フィールド
    for field in data["fields"]:
        lines.append(f'    @Inject')
        lines.append(f'    private {field["fieldType"]} {field["fieldDefinition"]};\n')

    # メソッド
    for method in data["methods"]:
        params = ', '.join(f'{p["paramType"]} {p["paramName"]}' for p in method["params"])
        lines.append(f'    public {method["returnType"]} {method["methodName"]}({params}) {{')
        for call in method["callMethods"]:
            lines.append(f'        // {call}')
        lines.append('    }\n')

    # クラス終了
    lines.append('}')

    return '\n'.join(lines)


json_data = '''
{
    "packageName": "org.terasoluna.tourreservation.domain.service.tourinfo",
    "className": "TourInfoServiceImpl",
    "implements": ["TourInfoService"],
    "extends": "",
    "imports": [
        "java.util.Collections",
        "java.util.List",
        "javax.inject.Inject",
        "org.springframework.data.domain.Page",
        "org.springframework.data.domain.PageImpl",
        "org.springframework.data.domain.Pageable",
        "org.springframework.stereotype.Service",
        "org.springframework.transaction.annotation.Transactional",
        "org.terasoluna.tourreservation.domain.model.TourInfo",
        "org.terasoluna.tourreservation.domain.repository.tourinfo.TourInfoRepository",
        "org.terasoluna.tourreservation.domain.repository.tourinfo.TourInfoSearchCriteria"
    ],
    "fields": [
        {"fieldType": "TourInfoRepository", "fieldDefinition": "tourInfoRepository"}
    ],
    "methods": [
        {
            "returnType": "Page<TourInfo>",
            "methodName": "searchTour",
            "params": [
                {"paramType": "TourInfoSearchCriteria", "paramName": "criteria"},
                {"paramType": "Pageable", "paramName": "pageable"}
            ],
            "callMethods": [
                "43 40 tourInfoRepository.countBySearchCriteria(criteria)",
                "46 41 tourInfoRepository.findPageBySearchCriteria(criteria,pageable)",
                "49 34 Collections.emptyList()"
            ]
        }
    ]
}
'''

data = json.loads(json_data)

if __name__ == '__main__':
    #logging_setting_path = '../resources/logging/utiltools_log.conf'
    #logging.config.fileConfig(logging_setting_path)
    logger = logging.getLogger(__file__)

    target_file_path = '/home/kato/GPTSniffer/ANTLR/src/test.java'

    ast_info = AstProcessor(logging, BasicInfoListener()).execute(target_file_path)
    
    
    
    java_code = create_java_file(data)
    print(java_code)

