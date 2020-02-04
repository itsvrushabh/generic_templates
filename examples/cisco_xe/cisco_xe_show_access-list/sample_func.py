def f1(json_output, template_headers):
    no_of_records = len(json_output)
    no_of_header_attribute = len(template_headers)
    percetange_of_record = 100 / no_of_records
    percetange_of_attribute = percetange_of_record/no_of_header_attribute
    template_percetange = 0

    for i in json_output:
        for j in template_headers:
            if i[j] != '':
                template_percetange += percetange_of_attribute
    print(template_percetange)

from utils import JSON_OUTPUT, TEMPLATE_HEADERS
from sample_func import f1

f1(JSON_OUTPUT, TEMPLATE_HEADERS)
