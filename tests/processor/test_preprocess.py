import unittest
from dwetl.reader.list_reader import ListReader
from dwetl.writer.list_writer import ListWriter
from dwetl.job_info import JobInfo
from dwetl.processor.preprocess import Preprocess
import pdb
import pprint

class TestPreprocess(unittest.TestCase):
    def test_preprocess(self):
        """
        tests the case where there's no whitespace
        """
        sample_data = [
            {   # pk data
                'db_operation_cd': 'U',
                'dw_stg_2_aleph_lbry_name': 'mai60',
                'em_create_dw_prcsng_cycle_id': '-1',
                # z00 don't have trims
                'in_z00_doc_number': '000019087',
                'in_z00_no_lines': '0011',
                'in_z00_data_len': '000400',
                # z13 has trims
                'in_z13_title': 'A literary history of America',
                'in_z13_author': 'Wendell, Barrett, 1855-1921',
                'in_z13_imprint': 'New York, Haskell House Publishers, 1968'
            }
        ]



        reader = ListReader(sample_data)
        writer = ListWriter()

        job_info = JobInfo(-1, 'test_user', '1', '1')

        logger = None

        sample_json_config = {
            'z00_doc_number': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "N/A",
                    "pre_detailed_instructions": "N/A"
                }
            },
            'z00_no_lines': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "N/A",
                    "pre_detailed_instructions": "N/A"
                }
            },
            'in_z00_data_len': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "N/A",
                    "pre_detailed_instructions": "N/A"
                }
            },
            'z13_title': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "Trim",
                    "pre_detailed_instructions": "Remove leading and trailing spaces"
                }
            },
            'z13_author': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "Trim",
                    "pre_detailed_instructions": "Remove leading and trailing spaces"
                }
            },
            'z13_imprint': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "Trim",
                    "pre_detailed_instructions": "Remove leading and trailing spaces"
                }
            }
        }


        pk_list = ['db_operation_cd', 'dw_stg_2_aleph_lbry_name', 'in_z00_doc_number', 'em_create_dw_prcsng_cycle_id']

        step = Preprocess(reader, writer, job_info, logger, sample_json_config, pk_list)
        step.execute()
        results = step.writer.list

        expected_keys = sorted([
                'in_z00_doc_number', 'pp_z00_doc_number', 'dw_stg_2_aleph_lbry_name', 'db_operation_cd',
                'pp_z00_no_lines', 'pp_z13_title', 'pp_z13_author',
                'pp_z00_data_len', 'pp_z13_imprint',
                'em_update_dw_prcsng_cycle_id', 'em_update_dw_job_exectn_id',
                'em_update_dw_job_name', 'em_update_dw_job_version_no',
                'em_update_user_id', 'em_update_tmstmp', 'em_create_dw_prcsng_cycle_id'
                ])

        self.assertEqual(expected_keys, sorted(list(results[0].keys())))
        self.assertEqual("000019087", results[0]['pp_z00_doc_number'])
        self.assertEqual('0011', results[0]['pp_z00_no_lines'])
        self.assertEqual('000400', results[0]['pp_z00_data_len'])



    def test_preprocess_lots_of_whitespace_and_none(self):
        """
        tests the case where whitespace exists
        """
        sample_data = [
            {
                # pk data
                'db_operation_cd': 'U',
                'dw_stg_2_aleph_lbry_name': 'mai60',
                'em_create_dw_prcsng_cycle_id': '-1',
                # z00 don't have trims
                'in_z00_doc_number': '  000019087 ',
                'in_z00_no_lines': None,
                'in_z00_data_len': None,
                # z13 has trims
                'in_z13_title': '  A literary history of America   ',
                'in_z13_author': '  Wendell, Barrett, 1855-1921  ',
                'in_z13_imprint': '  New York, Haskell House Publishers, 1968     '
            }
        ]

        reader = ListReader(sample_data)
        writer = ListWriter()

        job_info = JobInfo(-1, 'test_user', '1', '1')

        logger = None

        sample_json_config = {
            'z00_doc_number': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "N/A",
                    "pre_detailed_instructions": "N/A"
                }
            },
            'z00_no_lines': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "N/A",
                    "pre_detailed_instructions": "N/A"
                }
            },
            'z00_data_len': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "N/A",
                    "pre_detailed_instructions": "N/A"
                }
            },
            'z13_title': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "Trim",
                    "pre_detailed_instructions": "Remove leading and trailing spaces"
                }
            },
            'z13_author': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "Trim",
                    "pre_detailed_instructions": "Remove leading and trailing spaces"
                }
            },
            'z13_imprint': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "Trim",
                    "pre_detailed_instructions": "Remove leading and trailing spaces"
                }
            }
        }


        pk_list = ['db_operation_cd', 'dw_stg_2_aleph_lbry_name', 'in_z00_doc_number', 'em_create_dw_prcsng_cycle_id']

        step = Preprocess(reader, writer, job_info, logger, sample_json_config, pk_list)
        step.execute()
        results = step.writer.list

        expected_keys = sorted([
            'in_z00_doc_number', 'pp_z00_doc_number', 'dw_stg_2_aleph_lbry_name', 'db_operation_cd',
            'pp_z00_no_lines', 'pp_z13_title', 'pp_z13_author',
            'pp_z00_data_len', 'pp_z13_imprint',
            'em_update_dw_prcsng_cycle_id', 'em_update_dw_job_exectn_id',
            'em_update_dw_job_name', 'em_update_dw_job_version_no',
            'em_update_user_id', 'em_update_tmstmp', 'em_create_dw_prcsng_cycle_id'
        ])
        self.assertEqual(expected_keys, sorted(list(results[0].keys())))
        self.assertEqual("  000019087 ", results[0]['pp_z00_doc_number'])
        self.assertEqual("A literary history of America", results[0]['pp_z13_title'])
        self.assertEqual("Wendell, Barrett, 1855-1921", results[0]['pp_z13_author'])
        self.assertEqual(None, results[0]['pp_z00_no_lines'])
        self.assertEqual(None, results[0]['pp_z00_data_len'])

    def test_z00_pp(self):

        sample_data = [
            {
             'db_operation_cd': 'U',
             'in_z00_data': '',
             'in_z00_data_len': '001726',
             'in_z00_doc_number': '000181506',
             'in_z00_no_lines': '0038',
             'dw_stg_2_aleph_lbry_name': 'mai01',
             'em_create_dw_prcsng_cycle_id': '-1',
             }
        ]

        reader = ListReader(sample_data)
        writer = ListWriter()

        job_info = JobInfo(-1, 'test_user', '1', '1')

        logger = None

        sample_json_config =    {'z00_doc_number': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "N/A",
                    "pre_detailed_instructions": "N/A"
                }
            },
            'z00_no_lines': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "N/A",
                    "pre_detailed_instructions": "N/A"
                }
            },
            'z00_data_len': {
                "preprocessing_info": {
                    "pre_or_post_dq": "N/A",
                    "pre_action": "N/A",
                    "pre_detailed_instructions": "N/A"
                }
            }}

        pk_list = ['db_operation_cd', 'dw_stg_2_aleph_lbry_name', 'in_z00_doc_number', 'em_create_dw_prcsng_cycle_id']

        step = Preprocess(reader, writer, job_info, logger, sample_json_config, pk_list)
        step.execute()
        results = step.writer.list

        expected_keys = sorted([
            'in_z00_doc_number', 'pp_z00_doc_number', 'dw_stg_2_aleph_lbry_name', 'db_operation_cd',
            'pp_z00_no_lines',
            'pp_z00_data_len', 'pp_z00_data',
            'em_update_dw_prcsng_cycle_id', 'em_update_dw_job_exectn_id',
            'em_update_dw_job_name', 'em_update_dw_job_version_no',
            'em_update_user_id', 'em_update_tmstmp', 'em_create_dw_prcsng_cycle_id'
        ])
        self.assertEqual(False, Preprocess.need_preprocess(sample_json_config, ''))
        self.assertEqual(expected_keys, sorted(list(results[0].keys())))
        self.assertEqual("000181506", results[0]['pp_z00_doc_number'])
        self.assertEqual("0038", results[0]['pp_z00_no_lines'])
        self.assertEqual("001726", results[0]['pp_z00_data_len'])
        self.assertEqual("", results[0]['pp_z00_data'])










    def test_z13_pp(self):


        sample_data = [
            {
             'db_operation_cd': 'U',
            # 'dq_z13_author': None,
            # 'dq_z13_imprint': None,
            # 'dq_z13_isbn_issn': None,
            # 'dq_z13_isbn_issn_code': None,
            # 'dq_z13_open_date': None,
            # 'dq_z13_title': None,
            # 'dq_z13_update_date': None,
            # 'dq_z13_year': None,
             'dw_stg_2_aleph_lbry_name': 'mai01',
             'em_create_dw_job_exectn_id': 1,
             'em_create_dw_job_name': 'CopyStage1ToStage2',
             'em_create_dw_job_version_no': '1.0.0',
             'em_create_dw_prcsng_cycle_id': 3,
             #'em_create_tmstmp': datetime.datetime(2019, 12, 20, 12, 33, 32, 469542),
             'em_create_user_id': 'nimaasadi',
             'em_update_dw_job_exectn_id': None,
             'em_update_dw_job_name': None,
             'em_update_dw_job_version_no': None,
             'em_update_dw_prcsng_cycle_id': None,
             'em_update_tmstmp': None,
             'em_update_user_id': None,
             'in_z13_author': 'Economic indicators (Washington, D.C. : 1948)',
             'in_z13_author_code': '     ',
             'in_z13_call_no': 'Y 4.EC 7:EC 7/',
             'in_z13_call_no_code': 'PST3 ',
             'in_z13_call_no_key': '',
             'in_z13_imprint': 'Washington : U.S. G.P.O. : For sale by the Supt. of Docs',
             'in_z13_imprint_code': '     ',
             'in_z13_isbn_issn': '0013-0125',
             'in_z13_isbn_issn_code': '  0220 ',
             'in_z13_open_date': '20021124',
             'in_z13_rec_key': '000479040',
             'in_z13_title': 'Economic indicators',
             'in_z13_title_code': '     ',
             'in_z13_upd_time_stamp': '201709291709185',
             'in_z13_update_date': '20161222',
             'in_z13_year': '1948',
             'pp_z13_author': None,
             'pp_z13_imprint': None,
             'pp_z13_isbn_issn': None,
             'pp_z13_isbn_issn_code': None,
             'pp_z13_open_date': None,
             'pp_z13_title': None,
             'pp_z13_update_date': None,
             'pp_z13_year': None,
             'rm_dq_check_excptn_cnt': 0,
             'rm_suspend_rec_flag': 'N',
             'rm_suspend_rec_reason_cd': None
             }
        ]






        reader = ListReader(sample_data)
        writer = ListWriter()

        job_info = JobInfo(-1, 'test_user', '1', '1')
        logger = None

        sample_json_config =    {



        "z13_author": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "Trim",
            "pre_detailed_instructions": "Remove leading and trailing spaces"
        } },
        "z13_imprint": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "Trim",
            "pre_detailed_instructions": "Remove leading and trailing spaces"
        } },
        "z13_isbn_issn_code": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "Trim",
            "pre_detailed_instructions": "Remove leading and trailing spaces"
        } },
        "z13_isbn_issn": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "Trim",
            "pre_detailed_instructions": "Remove leading and trailing spaces"
        } },
        "z13_open_date": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "N/A",
            "pre_detailed_instructions": "N/A"
        } },
        "z13_update_date": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "N/A",
            "pre_detailed_instructions": "N/A"
        } }

        }



        pk_list = ['db_operation_cd', 'dw_stg_2_aleph_lbry_name', 'in_z13_rec_key', 'em_create_dw_prcsng_cycle_id']
        step = Preprocess(reader, writer, job_info, logger, sample_json_config, pk_list)
        step.execute()
        results = step.writer.list
        expected_keys = sorted([
         'db_operation_cd', 'dw_stg_2_aleph_lbry_name', 'em_create_dw_job_exectn_id', 'em_create_dw_job_name',
         'em_create_dw_job_version_no', 'em_create_dw_prcsng_cycle_id', 'em_create_user_id', 'em_update_dw_job_exectn_id',
         'em_update_dw_job_name', 'em_update_dw_job_version_no', 'em_update_dw_prcsng_cycle_id', 'em_update_tmstmp',
         'em_update_user_id', 'in_z13_rec_key', 'pp_z13_author', 'pp_z13_author_code', 'pp_z13_call_no',
         'pp_z13_call_no_code', 'pp_z13_call_no_key', 'pp_z13_imprint', 'pp_z13_imprint_code',
         'pp_z13_isbn_issn', 'pp_z13_isbn_issn_code', 'pp_z13_open_date', 'pp_z13_rec_key',
         'pp_z13_title', 'pp_z13_title_code', 'pp_z13_upd_time_stamp', 'pp_z13_update_date', 'pp_z13_year'
        ])

        self.assertEqual(False, Preprocess.need_preprocess(sample_json_config, ''))
        self.assertEqual(expected_keys, sorted(list(results[0].keys())))
        #self.assertEqual('', results[0]['pp_z13_author_code'])
        self.assertEqual("20021124", results[0]['pp_z13_open_date'])
        #self.assertEqual("0038", results[0]['pp_z13_author'])
        self.assertEqual("", results[0]['pp_z13_call_no_key'])
        self.assertEqual("0220", results[0]['pp_z13_isbn_issn_code'])







    def test_z00_field_pp(self):


        sample_data = [
            {
             'db_operation_cd': 'U',
            # 'dq_z13_author': None,
            # 'dq_z13_imprint': None,
            # 'dq_z13_isbn_issn': None,
            # 'dq_z13_isbn_issn_code': None,
            # 'dq_z13_open_date': None,
            # 'dq_z13_title': None,
            # 'dq_z13_update_date': None,
            # 'dq_z13_year': None,
             'dw_stg_2_aleph_lbry_name': 'mai01',
             'em_create_dw_job_exectn_id': 1,
             'em_create_dw_job_name': 'CopyStage1ToStage2',
             'em_create_dw_job_version_no': '1.0.0',
             'em_create_dw_prcsng_cycle_id': 3,
             #'em_create_tmstmp': datetime.datetime(2019, 12, 20, 12, 33, 32, 469542),
             'em_create_user_id': 'nimaasadi',
             'em_update_dw_job_exectn_id': None,
             'em_update_dw_job_name': None,
             'em_update_dw_job_version_no': None,
             'em_update_dw_prcsng_cycle_id': None,
             'em_update_tmstmp': None,
             'em_update_user_id': None,
             'in_z13_author': 'Economic indicators (Washington, D.C. : 1948)',
             'in_z13_author_code': '     ',
             'in_z13_call_no': 'Y 4.EC 7:EC 7/',
             'in_z13_call_no_code': 'PST3 ',
             'in_z13_call_no_key': '',
             'in_z13_imprint': 'Washington : U.S. G.P.O. : For sale by the Supt. of Docs',
             'in_z13_imprint_code': '     ',
             'in_z13_isbn_issn': '0013-0125',
             'in_z13_isbn_issn_code': '  0220 ',
             'in_z13_open_date': '20021124',
             'in_z13_rec_key': '000479040',
             'in_z13_title': 'Economic indicators',
             'in_z13_title_code': '     ',
             'in_z13_upd_time_stamp': '201709291709185',
             'in_z13_update_date': '20161222',
             'in_z13_year': '1948',
             'pp_z13_author': None,
             'pp_z13_imprint': None,
             'pp_z13_isbn_issn': None,
             'pp_z13_isbn_issn_code': None,
             'pp_z13_open_date': None,
             'pp_z13_title': None,
             'pp_z13_update_date': None,
             'pp_z13_year': None,
             'rm_dq_check_excptn_cnt': 0,
             'rm_suspend_rec_flag': 'N',
             'rm_suspend_rec_reason_cd': None
             }
        ]






        reader = ListReader(sample_data)
        writer = ListWriter()

        job_info = JobInfo(-1, 'test_user', '1', '1')
        logger = None

        sample_json_config =    {



        "z13_author": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "Trim",
            "pre_detailed_instructions": "Remove leading and trailing spaces"
        } },
        "z13_imprint": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "Trim",
            "pre_detailed_instructions": "Remove leading and trailing spaces"
        } },
        "z13_isbn_issn_code": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "Trim",
            "pre_detailed_instructions": "Remove leading and trailing spaces"
        } },
        "z13_isbn_issn": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "Trim",
            "pre_detailed_instructions": "Remove leading and trailing spaces"
        } },
        "z13_open_date": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "N/A",
            "pre_detailed_instructions": "N/A"
        } },
        "z13_update_date": {
        "preprocessing_info": {
            "pre_or_post_dq": "N/A",
            "pre_action": "N/A",
            "pre_detailed_instructions": "N/A"
        } }

        }



        pk_list = ['db_operation_cd', 'dw_stg_2_aleph_lbry_name', 'in_z13_rec_key', 'em_create_dw_prcsng_cycle_id']
        step = Preprocess(reader, writer, job_info, logger, sample_json_config, pk_list)
        step.execute()
        results = step.writer.list
        expected_keys = sorted([
         'db_operation_cd', 'dw_stg_2_aleph_lbry_name', 'em_create_dw_job_exectn_id', 'em_create_dw_job_name',
         'em_create_dw_job_version_no', 'em_create_dw_prcsng_cycle_id', 'em_create_user_id', 'em_update_dw_job_exectn_id',
         'em_update_dw_job_name', 'em_update_dw_job_version_no', 'em_update_dw_prcsng_cycle_id', 'em_update_tmstmp',
         'em_update_user_id', 'in_z13_rec_key', 'pp_z13_author', 'pp_z13_author_code', 'pp_z13_call_no',
         'pp_z13_call_no_code', 'pp_z13_call_no_key', 'pp_z13_imprint', 'pp_z13_imprint_code',
         'pp_z13_isbn_issn', 'pp_z13_isbn_issn_code', 'pp_z13_open_date', 'pp_z13_rec_key',
         'pp_z13_title', 'pp_z13_title_code', 'pp_z13_upd_time_stamp', 'pp_z13_update_date', 'pp_z13_year'
        ])

        self.assertEqual(False, Preprocess.need_preprocess(sample_json_config, ''))
        self.assertEqual(expected_keys, sorted(list(results[0].keys())))
        #self.assertEqual('', results[0]['pp_z13_author_code'])
        self.assertEqual("20021124", results[0]['pp_z13_open_date'])
        #self.assertEqual("0038", results[0]['pp_z13_author'])
        self.assertEqual("", results[0]['pp_z13_call_no_key'])
        self.assertEqual("0220", results[0]['pp_z13_isbn_issn_code'])








"""

tiff's work below

"""





        def test_z13u_pp(self):

            sample_data = [ {
                'db_operation_cd': 'I',
                'dw_stg_2_aleph_lbry_name': 'mai01',
                'em_create_dw_job_exectn_id': 1,
                'em_create_dw_job_name': 'CopyStage1ToStage2',
                'em_create_dw_job_version_no': '1.0.0',
                'em_create_dw_prcsng_cycle_id': 2,
                'in_z13u_user_defined_2': '',
                'in_z13u_user_defined_2_code': '     ',
                'in_z13u_user_defined_3': '^^^^^nam^^22^^^^^3u^4500',
                'in_z13u_user_defined_3_code': 'LDR  ',
                'in_z13u_user_defined_6': 'CIRC-CREATED SUPPRESSED ||',
                'in_z13u_user_defined_6_code': '     ',
                }
            ]

            reader = ListReader(sample_data)
            writer = ListWriter()

            job_info = JobInfo(-1, 'test_user', '1', '1')

            logger = None

            sample_json_config = [
                {'z13u_user_defined_2': {
                    'preprocessing_info': {'pre_action': 'Trim',
                                           'pre_detailed_instructions': 'Remove '
                                           'leading '
                                           'and '
                                           'trailing '
                                           'spaces',
                                           'pre_or_post_dq': 'Pre'
                                           }},
                    'z13u_user_defined_3': {
                        'preprocessing_info': {'pre_action': '',
                                               'pre_detailed_instructions': '',
                                               'pre_or_post_dq': 'N/A'}},
                    'z13u_user_defined_6': {
                        'preprocessing_info': {'pre_action': 'Trim',
                                               'pre_detailed_instructions': 'Remove '
                                               'leading '
                                               'and '
                                               'trailing '
                                               'spaces',
                                               'pre_or_post_dq': 'N/A'}
                                                }
                }]



            pk_list = ['db_operation_cd', 'dw_stg_2_aleph_lbry_name', 'in_z13u_rec_key', 'em_create_dw_prcsng_cycle_id']

            step = Preprocess(reader, writer, job_info, logger, sample_json_config, pk_list)
            step.execute()
            results = step.writer.list

            expected_keys = sorted([
                'dw_stg_2_aleph_lbry_name', 'db_operation_cd',
                'in_z13u_rec_key',
                'pp_z13u_user_defined_2',
                'pp_z13u_user_defined_3',
                'pp_z13u_user_defined_3_code',
                'pp_z13u_user_defined_6',
                'pp_z13u_user_defined_6_code',
                'em_update_dw_prcsng_cycle_id', 'em_update_dw_job_exectn_id',
                'em_update_dw_job_name', 'em_update_dw_job_version_no',
                'em_update_user_id', 'em_update_tmstmp', 'em_create_dw_prcsng_cycle_id'
            ])
            self.assertEqual(False, Preprocess.need_preprocess(sample_json_config, ''))
            self.assertEqual(expected_keys, sorted(list(results[0].keys())))
            self.assertEqual("000181506", results[0]['pp_z00_doc_number'])
            self.assertEqual("0038", results[0]['pp_z00_no_lines'])
            self.assertEqual("001726", results[0]['pp_z00_data_len'])
            self.assertEqual("", results[0]['pp_z00_data'])
